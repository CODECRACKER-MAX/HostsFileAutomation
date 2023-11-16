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

# Sayyam investments
104.21.60.135 172.67.196.220   os-lc.sayyaminvestments.in
172.67.196.220 104.21.60.135   ienaccount-new.sayyaminvestments.in

# Ms-Teams
173.223.162.97	a173-223-162-97.deploy.static.akamaitechnologies.com
52.123.128.14 52.123.129.14  teams.microsoft.com
20.190.145.140 40.126.17.135 20.190.145.141 40.126.17.132 20.190.145.142 40.126.17.133 40.126.17.134 20.190.145.160 login.microsoftonline.com 
52.113.194.133 in-api.asm.skype.com
52.168.112.66 browser.pipe.aria.microsoft.com
202.83.26.105 202.83.26.106 statics.teams.cdn.office.net
20.189.173.11 teams.events.data.microsoft.com
52.113.194.132 config.teams.microsoft.com
52.113.194.132 in-prod.asyncgw.teams.microsoft.com
52.114.40.19 in.ng.msg.teams.microsoft.com
13.107.246.58 13.107.213.58 csp.microsoft.com
52.113.194.132 ecs.office.com
52.123.160.8 presence.teams.microsoft.com
52.123.168.211 go.trouter.teams.microsoft.com
52.111.244.0 loki.delve.office.com

# Whatsapp Web
163.70.139.60  web.whatsapp.com media-tir3-2.cdn.whatsapp.net graph.whatsapp.net pps.whatsapp.net static.whatsapp.net dit.whatsapp.net mmg.whatsapp.net media.fblr22-1.fna.whatsapp.net

# some os-lc sites requirements
13.249.221.58 13.249.221.11 13.249.221.2 in-c2-aws.fastspeed.tech 

# Easebuzz
3.109.168.136 easebuzz.in

# Google Docs
142.250.183.238 docs.google.com


# osh.sayyaminvestments.in
104.21.60.135 172.67.196.220 osh.sayyaminvestments.in
138.113.130.11 za-c3.hitechset.com
52.219.160.102 3.5.208.102 52.219.156.86 52.219.158.134 52.219.158.138 52.219.160.26 3.5.212.16 india-security-pub.s3.ap-south-1.amazonaws.com
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
