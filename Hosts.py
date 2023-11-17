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
104.21.60.135 172.67.196.220   ienaccount.sayyaminvestments.in



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
152.199.39.242 aadcdn.msftauth.net
40.126.17.134 20.190.145.140 40.126.17.135 20.190.145.143 40.126.17.132 40.126.17.131 20.190.145.142 login.live.com 
20.189.173.16 browser.events.data.microsoft.com
52.98.123.242 52.98.57.162 52.98.59.18 52.98.58.34 substrate.office.com
52.123.168.211 pub-ent-jpea-08-t.trouter.teams.microsoft.com
13.107.6.163 fpc.msedge.net
52.123.128.14 52.123.129.14 statics.teams.cdn.office.net
52.123.128.14 52.123.129.14 tr-tmc-afd.office.com
13.107.3.254 s-ring.msedge.net
52.98.58.34 40.99.9.50 40.99.31.130 52.98.34.194 outlook.office.com
23.213.109.92 cxcs.cdn.office.net
52.123.128.14 52.123.129.14 tr-tmc-geo.office.com tr-tmc-afdmira.office.com
52.123.253.103 52.123.253.106 52.123.253.98 52.123.253.100 52.123.253.104 52.123.253.105 52.123.253.97 52.123.253.102 tr-tmc-mira.office.com

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
101.226.28.187 101.226.28.185 101.226.28.186 101.226.28.182 101.226.28.148 101.226.28.183 101.226.28.188 s4.zhenrongbao.com


# Google login
142.250.183.237 142.250.196.13 accounts.google.com
142.250.182.3 www.gstatic.com
216.58.196.163 gstatic.com
142.250.195.99 accounts.google.co.in
172.217.166.99 ssl.gstatic.com
142.250.182.35 fonts.gstatic.com
142.250.196.161 lh3.googleusercontent.com
172.217.166.110 play.google.com
142.250.196.78 accounts.youtube.com
142.250.196.46 aa.google.com
142.250.193.170 peoplestack-pa.clients6.google.com
172.217.163.202 172.217.166.106 142.250.77.138 142.250.77.170 142.250.182.10 142.250.182.42 142.250.182.74 142.250.182.106 142.250.182.138 142.250.183.234 142.250.193.106 142.250.193.138 142.250.193.170 142.250.205.234 172.217.31.202 142.250.195.74 content.googleapis.com 
142.250.77.106 142.250.77.170 142.250.182.10 142.250.182.42 142.250.182.74 142.250.182.106 142.250.182.138 142.250.183.234 142.250.193.106 142.250.193.138 142.250.193.170 142.250.205.234 172.217.167.138 172.217.31.202 142.250.71.42 142.250.195.42 signaler-pa.googleapis.com
142.250.195.106 peoplestackwebexperiments-pa.clients6.google.com
142.250.77.174 apis.google.com
142.250.196.35 accounts.google.co.in
142.250.182.74 addons-pa.clients6.google.com
142.250.182.46 contacts.google.com
142.250.183.238 ogs.google.com
142.250.195.138 espresso-pa.clients6.google.com
142.250.77.138 fonts.googleapis.com 
172.217.160.129 lh3.googleusercontent.com
172.217.163.173 myaccount.google.com
142.250.193.138 ajax.googleapis.com
142.250.195.78 www.google-analytics.com
35.241.11.240 kstatic.googleusercontent.com
142.250.77.142 http://crl.pki.goog
142.250.77.142 http://crls.pki.goog
142.250.71.10 142.250.195.42 142.250.195.74 142.250.195.106 142.250.195.138 142.250.195.170 142.250.195.202 142.250.195.234 142.250.196.10 142.250.196.42 142.250.196.74 142.250.196.170 142.250.77.106 142.250.77.170 142.250.182.10 142.250.182.42 oauth2.googleapis.com
142.250.196.42 142.250.196.74 142.250.196.170 172.217.163.170 172.217.163.202 142.250.76.74 142.250.77.106 142.250.77.138 142.250.77.170 142.250.182.10 142.250.182.42 142.250.182.74 142.250.182.106 142.250.182.138 142.250.183.234 142.250.193.106 https://oauth2.googleapis.com


# Outlook
52.96.229.242 52.96.223.2 52.96.172.98 52.96.214.50 52.96.111.82 52.96.228.130 52.96.222.226 52.96.91.34 outlook.com
13.107.246.58 13.107.213.58 wcpstatic.microsoft.com
20.72.243.62 fpt.microsoft.com
106.51.42.40 106.51.42.34 cdn-dynmedia-1.microsoft.com
104.97.25.161 www.microsoft.com
20.190.146.38 20.190.146.34 20.190.146.32 40.126.18.33 40.126.18.32 20.190.146.33 20.190.146.36 login.live.com
152.199.40.6 logincdn.msftauth.net
152.199.40.6 lgincdnvzeuno.azureedge.net
13.107.246.58 13.107.213.58 lgincdnmsftuswe2.azureedge.net
152.199.40.6 logincdn.msftauth.net 
40.99.9.50 52.98.88.66 52.98.123.194 52.98.123.242 outlook.office365.com
13.107.246.58 13.107.213.58 aadcdn.msauth.net
152.199.39.108 res.cdn.office.net
13.107.246.58 13.107.213.58 csp.microsoft.com
52.111.232.7 webshell.suite.office.com
20.190.145.170 20.190.145.171 20.190.145.169 graph.microsoft.com
40.80.89.238 clients.config.office.net
51.11.192.50 eu-office.events.data.microsoft.com
106.51.42.35 106.51.42.56 106.51.42.26 106.51.42.27 106.51.42.33 106.51.42.58 106.51.42.10 ow1.res.office365.com
23.203.63.11 125.56.222.49 res-1.cdn.office.net
13.107.6.156 www.office.com 
13.107.136.10 13.107.138.10 sayyamipl.sharepoint.com 
184.51.195.41 184.51.195.113 cdn.fluidpreview.office.net 
13.107.6.156 admin.microsoft.com
13.107.246.58 13.107.213.58 amcdn.msftauth.net
13.107.6.156 portal.office.com
52.109.64.31 thor.aesir.office.com
20.214.217.93 api.mfs.microsoft.com
23.57.47.132 static2.sharepointonline.com
13.107.6.163 upload.fp.measure.office.com
20.24.121.134 arc.msn.com
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
