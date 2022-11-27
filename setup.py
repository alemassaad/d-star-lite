from setuptools import setup, find_packages

setup(
    name='d-star-lite',
    version='1.0',
    description='python implementation of the D* Lite Algorithm',
    author='Matt Deyo',
    author_email='',
    url='https://github.com/alemassaad/d-star-lite',
    packages=find_packages(),
    entry_points={
        'console_scripts' : [
            'd-star-cli=d-star-lite.main:main'
        ]
    }
)
