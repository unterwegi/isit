#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()

setup(
	name			= 'isit',
	version			= '0.1.0',
	description 		= 'Environment detection',
	long_description	= open('README.rst').read(), 
	author 			= 'Geoffrey Lehée',
	author_email 		= 'geoffrey@lehee.name',
	url 			= '## Set url',
	keywords 		= 'python linux env variable windows arch distribution',
	py_modules 		= ['isit'],
	include_package_data	= True,
	classifiers		= [
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
