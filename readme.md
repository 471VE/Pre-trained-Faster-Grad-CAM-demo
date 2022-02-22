# Pre-trained Faster-Grad-CAM Demo

This program takes images of hands as an input and displays whether these hands are open or closed.

The following tutorial explains how to install the package (<b>step 2</b>) and how to set up the project for local development (<b>step 3</b>). Fulfillment of <b>step 1</b> is required for both purposes.

# 1. Preparing virtual environment

### 1.1) Using virtualenv

This section assumes that you have Python 3.7-3.9 installed since it is required by TensorFlow. Otherwise, skip this step and go to the next one.

First, install <b>virtualenv</b> by running

```
    pip install virtualenv
```

If you have Debian/Ubuntu system, you will also have to install python3-venv by:

```
    sudo apt install python3.9-venv
```

Second, create a new virtual environment `.venv` by running

```
    python -m venv .venv
```

on Windows and

```
    python3 -m venv .venv
```

on Linux. Next, activate it:

```
    .venv/Scripts/activate
```

on Windows and

```
    . .venv/bin/activate
```

on Linux.

### 1.2) Using conda

If you did the previous step, skip this one. This section assumes you have <b>Anaconda</b> or <b>Miniconda</b> installed.

Create a new virtual environment and activate it by executing following commands:

```
    conda create -n demo_env python=3.9.6

    conda activate demo_env
```
# 2. Installing the package

If you wish just to install the package and execute its script, follow the instructions below.

## 2.1) Installing the package from a local copy

These are the instructions on how to install the package using downloaded repository on your own machine.

### 2.1.1) Downloading the code

You can either download the archive by clicking <b>Code</b>-><b>Download ZIP</b> and extract it or clone this branch using git:

```
    git clone --branch Week-2.1 https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git

    cd Pre-trained-Faster-Grad-CAM-demo
```

### 2.1.2) Building the package

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

### 2.1.3) Installing the package

All you have left to do is actually installing the package. Do it by running

```
    pip install dist/PreTrainedFasterGradCAMDemo-0.2.1.tar.gz
```

## 2.2) Installing the package directly from the repository

Alternatively, if you do not want to download the code, you can just execute the following command:

```
    pip install git+https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git@Week-2.1
```

## 2.3) Running the script

You can finally run the script to check whether it was installed correctly. Do it by running the following command:

```
    demo
```

# 3. Setting up the project for local development

### 3.1) Downloading the code

You can either download the archive by clicking <b>Code</b>-><b>Download ZIP</b> and extract it or clone this branch using git:

```
    git clone --branch Week-2.1 https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo.git

    cd Pre-trained-Faster-Grad-CAM-demo
```

### 3.2) Installing dependencies

Install project dependencies:
```
    pip install -r requirements.txt
```

### 3.3) Installing ```pre-commit```

Install ```pre-commit``` module onto your machine by running:

```
    pip install pre-commit
```

### 3.4) Configure files (optional)

All of the files are already configured, but if you wish to change some of them, here is where settings are located for different checking tools:

- ".pre-commit-config.yaml" for ```pre-commit```;
- "pyproject.toml" for ```black``` and ```isort```;
- "setup.cfg" for ```flake8```.

### 3.5) Install git hooks

Install git hooks into your git hooks folder:
```
    pre-commit install
```

### 3.6) Running checks

Styling checks are now run automatically every time you try to commit your code. If all of the tests are successfully passed, commit process will proceed as usual. However, if some of the tests are failed, commit will not be finished. Stylistic errors will either be corrected automatically (i.e. in case of ```black```) or must be manually corrected (i.e. in case of ```flake8```). Be aware that you will have to stage changes again after failing a test.

If you want to style check your code without commiting, run

```
    pre-commit run -a
```

### 3.7) Running checks separately

Alternatively, you may choose to install the checking tools manually and run them separately when needed. Installation:
```
    pip install -r requirements_dev.txt
```
Then you can run checks by executing the following commands:
```
    black .

    isort .

    flake8 .
```

# 4. Testing and making CI pipeline

![Tests](https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo/actions/workflows/tests.yml/badge.svg)
