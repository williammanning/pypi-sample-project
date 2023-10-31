"""Python setup.py for pypi_sample_project package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("pypi_sample_project", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="pypi_sample_project",
    version=read("pypi_sample_project", "VERSION"),
    description="Awesome pypi_sample_project created by williammanning",
    url="https://github.com/williammanning/pypi-sample-project/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="williammanning",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["pypi_sample_project = pypi_sample_project.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
