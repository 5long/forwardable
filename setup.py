#!/usr/bin/env python

from setuptools import setup

from forwardable import __version__

setup(
    name='forwardable',
    version=__version__,
    description="Forwardable as in Ruby's stdlib",
    url='https://github.com/5long/forwardable',
    long_description=open("README.rst").read(),
    author="Whyme Lyu",
    author_email="callme5long@gmail.com",
    packages=[
        'forwardable',
        'forwardable.test',
    ],
    package_data={'': ['LICENSE', 'README.rst', 'CHANGELOG.rst']},
    include_package_data=True,
    license="MIT",
    test_suite="forwardable.test",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)
