FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential \
    python3.8 python3-pip python3.8-venv python3.8-dev
RUN apt-get install -y --fix-missing ffmpeg libsm6 libxext6
RUN rm -rf /var/cache/apt/archives \
    && rm -rf /var/lib/apt/lists

RUN python3 -m pip install --upgrade pip

COPY dist/PreTrainedFasterGradCAMDemo-0.3.1-py3-none-any.whl .
RUN python3 -m pip install PreTrainedFasterGradCAMDemo-0.3.1-py3-none-any.whl

WORKDIR /web_demo
COPY src/PreTrainedFasterGradCAMDemo/app.py /web_demo

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD [ "app.py"]
