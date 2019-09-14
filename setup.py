from __future__ import print_function

from setuptools import setup, find_packages


__version__ = '0.0.1'
name = '1d1Python'


def read_long_description(filename="README.md"):
    with open(filename) as f:
        return f.read().strip()


setup(
    name=name,
    version=__version__,
    author='jjori-master',
    author_email='jjori.master@gmail.com',
    url='https://github.com/jjori-master/1d1Python',
    description='1 day 1 Python practice',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    package_data={
        name: [
        ],
    },
    license='MIT',
    keywords='python 1 day practice',
    long_description=read_long_description(),
    install_requires=[
    ],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    extras_require={
        'tests': [
            'mamba',
            'expects',
            'codecov',
            'coveralls',
            'coverage',
            'pytest',
            'pytest-bdd',
            'pytest-runner',
            'pytest-cov',
            'py',                   # via pytest
            'flake8',
            'pyflakes',             # via flake8
            'pep8',                 # via flake8
            'mccabe',               # via flake8
            'mock',
            'six',                  # via mock
            'pbr',                  # via mock
            'funcsigs',             # via mock
        ],
    }
)