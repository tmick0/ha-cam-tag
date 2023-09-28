
from setuptools import setup
from pathlib import Path

setup(
    name="ha-cam-tag",
    version="0.0.1",
    author="travis mick",
    author_email="root@lo.calho.st",
    description="Recognizes QR codes in a camera stream and sends them to Home Assistant",
    license="MIT",
    url="https://github.com/tmick0/ha-cam-tag",
    python_requires='>=3.9',
    install_requires=["pyyaml", "homeassistant_api", "opencv-python-headless"],
    packages=["ha_cam_tag"],
    entry_points={
        'console_scripts': ['ha_cam_tag=ha_cam_tag.main:main'],
    }
)
