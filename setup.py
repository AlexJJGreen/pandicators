from setuptools import setup, find_packages

setup(
    name="pandicators",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    author="Alex JJ Green",
    author_email="alexjjgreen@gmail.com",
    description="A package of financial indicators for use with pandas",
    keywords="finance pandas analysis indicators"
)