from setuptools import find_packages, setup
from glob import glob
import os.path as osp
import io
import re

def get_version():
    current_dir = osp.abspath(osp.dirname(__file__))
    version_file = osp.join(current_dir, "src/PreTrainedFasterGradCAMDemo/__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        text = f.read()
    return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", text, re.M).group(1)


def get_dependencies():
    current_dir = osp.abspath(osp.dirname(__file__))
    requirements_file = osp.join(current_dir, "requirements.txt")
    with io.open(requirements_file, encoding="utf-8") as f:
        dependencies = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
    return dependencies


def get_long_description():
    current_dir = osp.abspath(osp.dirname(__file__))
    description_file = osp.join(current_dir, "readme.md")
    with io.open(description_file, encoding="utf-8") as f:
        long_description = f.read()
    return long_description


def get_data():
    current_dir = osp.abspath(osp.dirname(__file__))
    data = glob(current_dir + "/src/PreTrainedFasterGradCAMDemo/*/*")
    data = ['\\'.join(elem.split('\\')[-2:]) for elem in data]
    return data


setup(name="PreTrainedFasterGradCAMDemo",
      version=get_version(),
      author="471VE",
      author_email="zherebiatnikov.ivan@gmail.com",
      description="Pre-trained Faster-Grad-CAM Demo",
      long_description=get_long_description(),
      long_description_content_type="text/markdown",
      url="https://github.com/471VE/Pre-trained-Faster-Grad-CAM-demo",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=get_dependencies(),
      python_requires=">=3.7,<3.10",
      entry_points={"console_scripts": ["demo=PreTrainedFasterGradCAMDemo.demo:main"]},
      package_data={"PreTrainedFasterGradCAMDemo": get_data()})

