import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redash-client",
    version="0.1.0",
    author="Kento.Yamada",
    author_email="",
    description="Redash Client for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ymd65536/redash_client.git",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)