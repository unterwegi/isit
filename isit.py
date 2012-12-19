#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Isit help you to guess your runtime environment in order
to adapt your software in consequences."""
import os
import sys
import platform
import struct
from subprocess import Popen
from subprocess import PIPE as _PIPE

if sys.version < '3':
  import codecs
  def _u(x):
    return codecs.unicode_escape_decode(x)[0]
else:
  def _u(x):
    return x

##########
# Python #
##########
py2 = (sys.version_info[0] == 2)
py3 = (sys.version_info[0] == 3)
py30 = (py3 and sys.version_info[1] == 0)
py31 = (py3 and sys.version_info[1] == 1)
py32 = (py3 and sys.version_info[1] == 2)
py33 = (py3 and sys.version_info[1] == 3)
py34 = (py3 and sys.version_info[1] == 4)
py27 = (py2 and sys.version_info[1] == 7)
py26 = (py2 and sys.version_info[1] == 6)
py25 = (py2 and sys.version_info[1] == 5)
py24 = (py2 and sys.version_info[1] == 4)
pypy = ('pypy' in sys.version_info)
jython = ('java' in sys.version_info)
ironpython = ('iron' in sys.version_info)
cpython = not any((pypy, jython, ironpython))

########
# Arch #
########
bit32 = struct.calcsize('P') * 8 == 32
bit64 = struct.calcsize('P') * 8 == 64

##############
# Endianness #
##############
little_endian = sys.byteorder == 'little'
big_endian = sys.byteorder == 'big'

######
# Os #
######
# Linux
linux = platform.system().lower() == 'linux'
linux_version = None
linux2 = False
linux3 = False
if linux:
  if py3:
    from subprocess import getoutput
    linux_version = _u(getoutput('uname -r'))
  else:
    linux_version = _u(Popen('uname -r', stdout=_PIPE, stderr=_PIPE, shell=True).stdout.read()[:-1])
  linux2 = '2' in linux_version[0]
  linux3 = '3' in linux_version[0]
# Osx
osx = platform.system().lower() == 'darwin'
osx = None
if osx:
  osx_version = _u(platform.mac_ver()[0])
# Windows
windows = ('win32' in str(sys.platform).lower())
# Other
hpux = ('hpux' in str(sys.platform).lower())
solaris = ('sunos' in str(sys.platform).lower())

#################
# Distributions #
#################
# Ubuntu
ubuntu = False
ubuntu_version = None
ubuntu_release = None
ubuntu_lts = None
if os.path.exists('/proc/version'):
  _proc_version_file = open('/proc/version')
  _proc_version_lines = [_line.replace('\n', '') for _line in _proc_version_file.readlines()]
  _proc_version_file.close()
  ubuntu = 'ubuntu' in _proc_version_lines[0].lower()
if ubuntu:
  _lsb_release_file = open('/etc/lsb-release')
  _lsb_release_lines = [_line.replace('\n', '') for _line in _lsb_release_file.readlines()]
  _lsb_release_file.close()
  ubuntu_version = _u(_lsb_release_lines[3].split('=')[-1].split(' ')[1])
  if len(_lsb_release_lines[3].split('=')[-1].split(' ')[1].split('.')) == 3:
    ubuntu_release = _u(_lsb_release_lines[3].split('=')[-1].split(' ')[1].split('.')[2])
  ubuntu_lts = ubuntu_version.split('.')[1] == "04"
  ubuntu_codename = _u(_lsb_release_lines[2].split('=')[1])
# Debian
debian = os.path.exists('/etc/debian_version') and not ubuntu
debian_version = None
debian_release = None
if debian:
  _debian_version_file = open('/etc/debian_version')
  _debian_version_lines = [_line.replace('\n', '') for _line in _debian_version_file.readlines()]
  _debian_version_file.close()
  debian_version = _u(_debian_version_lines[0])
  debian_release = _u(debian_version.split('.')[-1])
# Archlinux
archlinux = os.path.exists('/etc/arch-release')
archlinux_version = None
archlinux_release = None
# Centos
centos = 'centos' in platform.dist()[0].lower()
centos_version = None
centos_release = None
if centos:
  centos_version = _u(platform.dist()[1])
  centos_release = _u(centos_version.split('.')[-1])
# Redhat
redhat = 'redhat' in platform.dist()[0].lower()
redhat_version = None
redhat_release = None
if redhat:
  redhat_version = _u(platform.dist()[1])
  redhat_release = _u(redhat_version.split('.')[-1])

############
# Packages #
############
package_deb = ubuntu or debian
package_rpm = centos or redhat
