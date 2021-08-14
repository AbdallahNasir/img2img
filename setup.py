from setuptools import setup


setup(
    name='img2img',
    description="",
    version="0.1",
    packages=['img2img'],
    zip_safe=False,
    entry_points={
            "console_scripts": [
                "img2img-train = img2img_cli.train:main",
                "img2img-synthesize = img2img_cli.synthesize:main",
                "img2img-generate = img2img_cli.generate:main",
            ]
        },
    install_requires=[
        "opencv-python>=4",
        "tensorflow>=2",
        "numpy~=1.19.2",
    ]
)
