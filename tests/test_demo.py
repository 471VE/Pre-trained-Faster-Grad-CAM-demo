import os.path as osp

import numpy as np
import pytest

from PreTrainedFasterGradCAMDemo import demo


def prepare_image_names(list_of_short_names):
    path_to_images = osp.abspath(osp.dirname(__file__)) + "/hand_images/"
    images_for_testing = [path_to_images + image for image in list_of_short_names]
    return images_for_testing


# Test for whether the processing of images returns the same result
def test_regression():
    for image in prepare_image_names(
        ["fist.jpg", "open_palm.jpg", "large_image.jpg", "small_image.jpg"]
    ):
        first_result, first_image = demo.main([image], show_image=False)
        second_result, second_image = demo.main([image], show_image=False)
        first_image, second_image = (image[0] for image in (first_image, second_image))
        # To reverse the channels of the second image, uncomment the line below:
        # second_image = second_image[:,:,::-1]
        print(type(first_image))
        assert np.array_equal(first_image, second_image) & (first_result == second_result)


# Test for whether the processing of hand-picked images returns the true result
def test_correctness_of_results():
    true_positions = ["Closed", "Open"]
    predicted_positions, _ = demo.main(
        prepare_image_names(["fist.jpg", "open_palm.jpg"]), show_image=False
    )
    assert true_positions == predicted_positions


# Tests for whether program runs without errors on large and on a small image
@pytest.mark.parametrize("image_name", ["large_image.jpg", "small_image.jpg"])
def test_for_errors_on_images_of_different_sizes(image_name):
    demo.main(prepare_image_names([image_name]), show_image=False)
