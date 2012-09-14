#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import platform
import struct
from subprocess import Popen, PIPE

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
big_endian    = sys.byteorder == 'big'

######
# Os #
######
# Linux
linux      = platform.system().lower() == 'linux'
linux_vers = None
linux2     = False
linux3     = False
if linux:
	if py3:
		from subprocess import getoutput
		linux_vers = getoutput('uname -r')
	else:
		linux_vers = Popen('uname -r',stdout=PIPE,stderr=PIPE,shell=True).stdout.read()[:-1]
		del PIPE
	linux2 = '2' in linux_vers[0]
	linux3 = '3' in linux_vers[0]
# Osx
osx        = platform.system().lower() == 'darwin'
osx_vers   = platform.mac_ver()[0] or None
# Windows
windows    = ('win32' in str(sys.platform).lower())
# Other
hpux       = ('hpux' in str(sys.platform).lower())
solaris    = ('sunos' in str(sys.platform).lower())

################
# Distribution #
################
# Ubuntu
ubuntu = False
ubuntu_vers = None
if os.path.exists('/proc/version'):
	ubuntu = 'ubuntu' in open('/proc/version').read().lower()
if ubuntu:
	ubuntu_vers = open('/etc/lsb-release').readlines()[1].split('=')[1].replace('\n','')
# Debian
debian = os.path.exists('/etc/debian_version')
debian_vers = None
if debian:
	debian_vers = open('/etc/debian_version').read().replace('\n','')
# Archlinux
archlinux = os.path.exists('/etc/arch-release')
archlinux_vers = None
# Centos
centos = 'centos' in platform.dist()[0].lower()
centos_vers = None
if centos_vers:
	centos_vers = platform.dist()[1].split('.')[0]
# Redhat
redhat = 'redhat' in platform.dist()[0].lower()
redhat_vers = None
if redhat:
	redhat_vers = platform.dist()[1].split('.')[0]
