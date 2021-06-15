import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rws-python-sdk",
    version="0.0.1",
    author="mkdir700",
    author_email="mkdir700@gmail.com",
    description="Rakuten Web Service SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkdir700/rws-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
