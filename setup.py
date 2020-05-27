from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aftercopy",
    version="0.1.1",
    description="A helper tool that processes text copied from PDF, removing newlines, replacing punctuation and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coolspring8/aftercopy",
    author="CoolSpring8",
    author_email="coolspring888@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="clipboard text",
    py_modules=["aftercopy"],
    python_requires=">=3.5, <4",
    install_requires=["click>=7.0", "pyperclip>=1.8.0"],
    entry_points={"console_scripts": ["aftercopy=aftercopy:main",],},
    project_urls={
        "Bug Reports": "https://github.com/coolspring8/aftercopy/issues",
        "Source": "https://github.com/coolspring8/aftercopy/",
    },
)
