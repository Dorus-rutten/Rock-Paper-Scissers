from setuptools import setup, find_packages

setup(
    name="RPS",
    version="0.1.0",  # Initial version
    author="Dorus Rutten",
    author_email="Dorsrutten@gmail.com",
    description="A AI that plays Rock Papier Scissers with u using the camera",
    long_description=open("README.md").read(),  # Reads your README.md for details
    long_description_content_type="text/markdown",
    url="https://github.com/Dorus-rutten/Rock-Paper-Scissers",  # Replace with your GitHub repo
    packages=find_packages(),  # Automatically finds your Python packages
    install_requires=[
        "opencv-contrib-python==4.8.0.74",
        "opencv-python==4.8.0.74",
        "mediapipe==0.10.14",
        "numpy==1.25.1"
    ],
    python_requires='==3.9.20',  # Corrected this line
)