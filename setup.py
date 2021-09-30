from distutils.core import setup

setup(
    # Application name:
    name="Neural Network",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Mathew McPherson",
    author_email="Mathew.Liam.McPherson@gmail.com",

    # Packages
    packages=["src/main"],

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Project to create and train neural networks.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "tkinter",
        "numpy",
        "random",
        "math"
    ],
)