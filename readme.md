# Pre-trained Faster-Grad-CAM Demo

This program takes images of hands as an input and displays whether these hands are open or closed.

## Preparing virtual environment

### Using virtualenv

This section assumes that you have Python 3.7-3.9 installed since it is required by TensorFlow. Otherwise, skip this step and go to the next one.

First, install <b>virtualenv</b> by running

```
    pip install virtualenv
```

If you have Debian/Ubuntu system, you will also have to install python3-venv by:

```
    sudo apt install python3.9-venv
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
    demo_env/Scripts/activate
```

on Windows and

```
    . demo_env/bin/activate
```

on Linux.

### Using conda

If you did the previous step, skip this one. This section assumes you have <b>Anaconda</b> or <b>Miniconda</b> installed.

Create a new virtual environment and activate it by executing following commands:

```
    conda create -n demo_env python=3.9.6

    conda activate demo_env
```

## Installing the package from a local copy

These are the instructions on how to install the package using downloaded repository on your own machine.

### Downloading the code

You can either download the archive by clicking <b>Code</b>-><b>Download ZIP</b> and extract it or clone this branch using git:

```
git clone --branch Week-1.2 https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git

cd Pre-trained-Faster-Grad-CAM-demo
```

### Building the package

You do not have to build the package yourself, since it has already been built, but if you still wish to do so, follow the instructions below. If you do not want to do it, go to the next step.

To build the package, you have to install `build` module:

```
    pip install build
```

Then you can build the package by runnung

```
    python -m build
```

on Windows and

```
    python3 -m build
```

on Linux.

### Installing the package

All you have left to do is actually installing the package. Do it by running

```
    pip install dist/PreTrainedFasterGradCAMDemo-0.1.2.tar.gz
```

## Installing the package directly from the repository

Alternatively, if you do not want to download the code, you can just execute the following command:

```
    pip install git+https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git@Week-1.2
```

## Running the script

You can finally run the script. Do it by running the following command:

```
    demo
```