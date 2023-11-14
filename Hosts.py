to_write = """
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

104.21.60.135 172.67.196.220   os-lc.sayyaminvestments.in
172.67.196.220 104.21.60.135   ienaccount-new.sayyaminvestments.in
"""

import os

host_file_location = "C:\\Windows\\System32\\drivers\\etc\\hosts"

try:
    if (os.path.isfile(host_file_location)): # If True
        os.remove(host_file_location)

        # Write the file.
        
        f = open(host_file_location,'w')
        f.write(to_write)
        
    else:
        print("Hosts file doesn't exists.")


except PermissionError:
    print("Unable to delete the hostfile permission error.")


# Change the dns address of the pc.
command = 'netsh interface ip set dns "Ethernet" static 127.0.0.1'
os.system(command)
os.system(command.replace("Ethernet","Ethernet0"))
