from setuptools import setup, find_packages

setup(
    name='soundtracktor_kafka',
    version='1.0.1',
    packages=find_packages(),
    install_requires=['kafka-python==2.0.2', 'json'],
)
