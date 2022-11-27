from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='d-star-lite',
    version='1.0',
    description='python implementation of the D* Lite Algorithm',
    author='Matt Deyo',
    author_email='',
    url='https://github.com/alemassaad/d-star-lite',
    packages=find_packages()
)
