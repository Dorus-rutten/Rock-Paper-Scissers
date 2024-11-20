from setuptools import setup, find_packages

setup(
    name="RPS",
    version="0.1.0",
    author="Dorus Rutten",
    author_email="Dorsrutten@gmail.com",
    description="A AI that plays Rock Papier Scissers with u using the camera",
    url="https://github.com/Dorus-rutten/Rock-Paper-Scissors",
    packages=find_packages(),
    install_requires=[
        "opencv-contrib-python==4.8.0.74",
        "opencv-python==4.8.0.74",
        "mediapipe==0.10.14",
        "numpy==1.25.1"
    ],
    python_requires='==3.9.20',
)
