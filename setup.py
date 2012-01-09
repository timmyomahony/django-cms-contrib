import os
from setuptools import setup, find_packages

from parsnip import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-cms-contrib',
    version=".".join(map(str, VERSION)),
    description='A collection of useful code snippets, apps and other bits and pieces that a normal Content Management System usually requires. ',
    long_description=readme,
    author="Timmy O'Mahony",
    author_email='timmy@pastylegs.com',
    url='https://github.com/pastylegs/django-cms-contrib',
    packages=find_packages(),
    package_data = {
        'cms_contrib': [
        ],
    },
)