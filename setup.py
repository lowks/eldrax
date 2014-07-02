from setuptools import setup, find_packages


setup(
    name="eldrax",
    version="0.1a2",
    description='Python library for interacting with Rackspace services',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "requests==1.2.3",
    ],
)
