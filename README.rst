Isit
====

Description
-----------

Detect environment variables, such ``linux``, ``distribution``, ``python``, etc...

::

  >>> import isit
  >>> isit.linux
  True
  >>> isit.linux2
  True
  >>> isit.linux3
  False
  >>> isit.py2
  True
  >>> isit.py27
  False
  >>> isit.debian
  True
  >>> isit.debian_version
  '6.0.5'
  >>> isit.debian_release
  '5'
  >>> isit.bit32
  True
  >>> isit.pypy
  False
  >>> isit.cpython
  True

You can do ``help(isit)`` for list.

Installation
------------

::

	pip install isit


Heavily inspired by `its`_ from `Kenneth Reitz`_. But with moar!

.. _its: https://github.com/kennethreitz/its.py
.. _Kenneth Reitz: https://github.com/kennethreitz
