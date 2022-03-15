from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="pythontrail",
    version="0.0.1",
    author="Madhanagopal Murthy",
    description="A test package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/madhanagopal-murthy/pythontrail/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
)

