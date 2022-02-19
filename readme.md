# Pre-trained Faster-Grad-CAM Demo

This program takes images of hands as an input and displays whether these hands are open or closed. You can add your own `.jpg` or `.png` images to the `hand_images` directory.

## Downloading the code

You can either download the archive by clicking <b>Code</b>-><b>Download ZIP</b> and extract it or clone this branch using git:

```
git clone --branch Week-1.1 https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git

cd Pre-trained-Faster-Grad-CAM-demo
```

## Running the program

### Using virtualenv

The following tutorial assumes that you have Python 3.7-3.9 installed since it is required by TensorFlow. Otherwise, skip this step and go to the next one.

First, install <b>virtualenv</b> by running

```
    pip install virtualenv
```

Second, create a new virtual environment `demo_env` by running

```
    python -m venv demo_env
```

on Windows and

```
    python3 -m venv demo_env
```

on Linux. Next, activate it:

```
    demo_env\Scripts\activate
```

on Windows and

```
    demo_env\bin\activate
```

on Linux.

### Using conda

If you did the previous step, skip this one. This step assumes you have <b>Anaconda</b> or <b>Miniconda</b> installed.

Create a new virtual environment and activate it by executing following commands:

```
    conda create -n demo_env python=3.9.6

    conda activate demo_env
```

### Dependencies

Last, install dependencies:

```
    pip install -r requirements.txt
```

You can finally run the script. Do it by running

```
    python demo.py
```

on Windows and

```
    python3 demo.py
```

on Linux.