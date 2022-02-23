import glob
import os
import os.path as osp

import cv2
import joblib
import numpy as np
from tensorflow.lite.python.interpreter import Interpreter

model_path = osp.abspath(osp.dirname(__file__)) + "/model/"

if os.path.exists(model_path):
    # load csv
    print("csv loading...")
    channel_weight = np.loadtxt(model_path + "channel_weight.csv", delimiter=",")
    channel_adress = np.loadtxt(model_path + "channel_adress.csv", delimiter=",", dtype="float")
    channel_adress = channel_adress.astype(int)
    vector_pa = np.loadtxt(model_path + "vector_pa.csv", delimiter=",")
    kmeans = joblib.load(model_path + "k-means.pkl.cmp")
else:
    raise Exception("The path to the model weights does not exist.")

path_to_images = osp.abspath(osp.dirname(__file__)) + "/hand_images/"
if os.path.exists(path_to_images):
    image_names = glob.glob(f"{path_to_images}*.jpg") + glob.glob(f"{path_to_images}*.png")
else:
    print("The path to the directory with the images of hands does not exist.")


def get_score_arc(pa_vector, test):
    # cosine similarity
    cos_similarity = cosine_similarity(test, pa_vector)

    return np.max(cos_similarity)


def cosine_similarity(x1, x2):
    if x1.ndim == 1:
        x1 = x1[np.newaxis]
    if x2.ndim == 1:
        x2 = x2[np.newaxis]
    x1_norm = np.linalg.norm(x1, axis=1)
    x2_norm = np.linalg.norm(x2, axis=1)
    cosine_sim = np.dot(x1, x2.T) / (x1_norm * x2_norm + 1e-10)
    return cosine_sim


def predict_faster_gradcam(channel, vector, img, kmeans, channel_weight, channel_adress):
    channel_out = channel[0]

    # k-means and heat_map
    cluster_no = kmeans.predict(vector)
    cam = np.dot(channel_out[:, :, channel_adress[cluster_no[0]]], channel_weight[cluster_no[0]])

    # nomalize
    cam = cv2.resize(cam, (img.shape[1], img.shape[0]), cv2.INTER_LINEAR)
    cam = np.maximum(cam, 0)
    cam = cam / cam.max()

    return cam


def get_x_y_limit(heatmap, thresh):
    map_ = np.where(heatmap > thresh)
    x_max = np.max(map_[1])
    x_min = np.min(map_[1])
    y_max = np.max(map_[0])
    y_min = np.min(map_[0])

    x_max = int(x_max)
    x_min = int(x_min)
    y_max = int(y_max)
    y_min = int(y_min)
    return x_min, y_min, x_max, y_max


def bounding_box(img, x_min, y_min, x_max, y_max):
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 5)


def main(image_names=image_names, show_image=True):
    input_size = 96
    hand_thresh = 0.25
    OD_thresh = 0.8
    message1 = "Push [q] to go to the next image or to quit."
    message2 = "Push [s] to change mode."
    like_OD = False  # like object detection

    interpreter = Interpreter(model_path=model_path + "weights_weight_quant.tflite")
    try:
        interpreter.set_num_threads(4)
    except Exception:
        pass

    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    hand_positions = []
    processed_images = []

    for image_name in image_names:
        image = cv2.imread(image_name)
        img = cv2.resize(image, (input_size, input_size))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img / 255
        img = np.expand_dims(img, axis=0)
        img = img.astype(np.float32)
        interpreter.set_tensor(input_details[0]["index"], img)
        interpreter.invoke()
        channel_out = interpreter.get_tensor(output_details[0]["index"])
        test_vector = interpreter.get_tensor(output_details[1]["index"])
        score = get_score_arc(vector_pa, test_vector)

        def show_info():
            new_image = image.copy()
            if score < hand_thresh:  # hand is closed
                hand = "Closed"
                color = (255, 0, 0)
                heatmap = predict_faster_gradcam(
                    channel_out, test_vector, new_image, kmeans, channel_weight, channel_adress
                )
                if like_OD:
                    x_min, y_min, x_max, y_max = get_x_y_limit(heatmap, OD_thresh)
                    bounding_box(new_image, x_min, y_min, x_max, y_max)
                else:
                    heatmap = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
                    new_image = np.copy(cv2.addWeighted(heatmap, 0.5, new_image, 0.5, 2.2))
            else:  # hand is open
                hand = "Open"
                color = (0, 0, 255)

            # message
            cv2.putText(
                new_image,
                f"{hand}, score: {score:.1f}",
                (15, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                1,
                cv2.LINE_AA,
            )
            cv2.putText(
                new_image,
                message1,
                (15, 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                1,
                cv2.LINE_AA,
            )
            cv2.putText(
                new_image,
                message2,
                (15, 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                1,
                cv2.LINE_AA,
            )
            # display the image
            return hand, new_image

        if show_image:
            # quit or change mode
            while True:
                hand, image_to_show = show_info()
                cv2.imshow("Result", image_to_show)
                key = cv2.waitKey(10) & 0xFF
                if key == ord("q"):
                    hand_positions.append(hand)
                    processed_images.append(image_to_show)
                    break
                elif key == ord("s"):
                    if like_OD:
                        like_OD = False
                    else:
                        like_OD = True

            cv2.destroyAllWindows()
        else:
            hand, image_to_show = show_info()
            hand_positions.append(hand)
            processed_images.append(image_to_show)

    return hand_positions, processed_images


if __name__ == "__main__":
    main()
