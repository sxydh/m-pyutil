import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="m_pyutil",
    version="1.7.3",
    author="sxydh",
    author_email="sxydhgg@gmail.com",
    description="NOTHING",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sxydh/m-pyutil",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require={
        'mmongo': ['pymongo>=4.9.1'],
        'mip': ['psutil>=6.0.0'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
