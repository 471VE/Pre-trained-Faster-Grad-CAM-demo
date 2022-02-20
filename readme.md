# Pre-trained Faster-Grad-CAM Demo

This program takes images of hands as an input and displays whether these hands are open or closed.

## Downloading the code

You can either download the archive by clicking <b>Code</b>-><b>Download ZIP</b> and extract it or clone this branch using git:

```
git clone --branch Week-1.2 https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git

cd Pre-trained-Faster-Grad-CAM-demo
```

## Preparing virtual environment

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

Install `build` module:

```
    pip install build
```


You can finally run the script. Do it by running the following command:

```
    demo
```