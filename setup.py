# -*- coding: utf-8 -*-
"""`neutronpy_sphinx_rtd_theme` lives on `Github`_.

.. _github: https://www.github.com/neutronpy/neutronpy_sphinx_rtd_theme

"""
from setuptools import setup
from neutronpy_sphinx_rtd_theme import __version__


setup(
    name='neutronpy_sphinx_rtd_theme',
    version=__version__,
    url='https://github.com/neutronpy/neutronpy_sphinx_rtd_theme/',
    license='MIT',
    author='David M Fobes',
    author_email='pseudocubic@gmail.com',
    description='ReadTheDocs.org theme for Sphinx, 2013 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['neutronpy_sphinx_rtd_theme'],
    package_data={'neutronpy_sphinx_rtd_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*',
        'support.py'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
