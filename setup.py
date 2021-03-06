#!/usr/bin/env python
import io
import os

from setuptools import setup, find_packages

def read(fname, encoding='utf-8'):
    path = os.path.join(os.path.dirname(__file__), fname)
    with io.open(path, encoding=encoding) as f:
        return f.read()


setup(
    name='django-u2f',
    description="FIDO U2F security token support for Django",
    long_description=read('README.rst'),
    url='https://github.com/gavinwahl/django-u2f',

    packages=find_packages(exclude=['testproj']),
    include_package_data=True,

    install_requires=[
        'django-argonauts',
        'django>=1.8',
        'qrcode',
        'six',
    ],
    # u2f support is an extra for now because m2crypt doesn't support python 3.
    # This allows using the rest of the authentication methods without u2f.
    extras_require={
        'u2f': ['python-u2flib-server'],
    },
    author='Gavin Wahl',
    author_email='gavinwahl@gmail.com',
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
    ],
)
