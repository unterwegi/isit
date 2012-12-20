#!/usr/bin/env python
# coding: utf-8

import os
import sys
import isit

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()

if sys.version < '3':
  import codecs
  def u(x):
    return codecs.unicode_escape_decode(x)[0]
else:
  def u(x):
    return x

setup(
	name='isit',
	version=isit.__version__,
	description='Environment runtime detection (Python,Linux,Distribution,etc...)',
	long_description=open('README.rst').read(), 
	author=u('Geoffrey Lehée'),
	author_email='geoffrey@lehee.name',
	url='https://github.com/socketubs/isit',
	keywords='python linux env variable windows arch distribution',
	py_modules=['isit'],
	include_package_data=True,
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.4',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.0',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3']
)
