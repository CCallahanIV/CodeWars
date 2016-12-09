"""Setup for code wars katas."""

from setuptools import setup

setup(
    name="codewars-ted",
    description="",
    version=0.1,
    author="Ted Callahan",
    author_email="thisguy@gmail.com",
    license="MIT",
    package_dir={'': '401-code-katas'},
    py_modules=[""],
    install_requires=[""],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
)
