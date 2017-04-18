#!/usr/bin/env python
'''
GNU GENERAL PUBLIC LICENSE v3

i3_printScreen.py
Copyright (C) <2016> JOSE (J) MARCOS <jm4rcos@gmail.com>

This program  is free software:  you  can redistribute it and/or modify it under
the  terms  of the GNU General Public License  as published by the Free Software
Foundation, either version 3  of  the  License, or  (at your option)  any  later
version.

This program  is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY;  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

See  <http://www.gnu.org/licenses/>  for  more details of the GNU General Public
License.
'''

'''
this script requires shutter installed onyour system.

'''


import os

''' Check shutter pid
'''
opid = os.popen("pgrep shutter")
pid  = opid.read().strip('\n')


if len(pid) != 0 :
    os.popen('shutter -C --disable_systray -s')

else:
    os.popen('shutter -C --disable_systray -s -e | xclip')
