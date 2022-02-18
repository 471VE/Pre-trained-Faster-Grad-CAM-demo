# Pre-trained Faster-Grad-CAM Demo

This program takes images of hands as an input and displays whether these hands are open or closed.

## Running the program

The following tutorial assumes that you have Python 3 installed.

First, install <b>virtualenv</b> by running

```
    pip install virtualenv
```

Second, create a new virtual environment `demo_env` by running

```
    python -m venv demo_env
```

and activate it:

```
    demo_env\Scripts\activate
```

on Windows and

```
    demo_env\bin\activate
```

on Linux.

Third, install dependencies:

```
    pip install -r requirements.txt
```

You can finally run the script. Do it by running

```
    python demo.py
```