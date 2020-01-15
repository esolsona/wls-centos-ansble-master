#!/usr/bin/python
# Author : Tim Hall
# Save Script as : create_nodemanagr_ref.py

import time
import getopt
import sys
import re

# Get location of the properties file.
properties = ''
try:
   opts, args = getopt.getopt(sys.argv[1:],"p:h::",["properies="])
except getopt.GetoptError:
   print 'create_nodemanagr_ref.py -p <path-to-properties-file>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'create_nodemanagr_ref.py -p <path-to-properties-file>'
      sys.exit()
   elif opt in ("-p", "--properties"):
      properties = arg
print 'properties=', properties

# Load the properties from the properties file.
from java.io import FileInputStream
 
propInputStream = FileInputStream(properties)
configProps = Properties()
configProps.load(propInputStream)

# Set all variables from values in properties file.
adminUsername=configProps.get("admin.username")
adminPassword=configProps.get("admin.password")
adminURL=configProps.get("admin.url")
nmName=configProps.get("nm.name")
nmAddress=configProps.get("nm.address")
nmPort=configProps.get("nm.port")

# Display the variable values.
print 'adminUsername=', adminUsername
print 'adminPassword=', adminPassword
print 'adminURL=', adminURL
print 'nmName=', nmName
print 'nmAddress=', nmAddress
print 'nmPort=', nmPort

# Connect to the AdminServer.
connect(adminUsername, adminPassword, adminURL)

edit()
startEdit()

# Create the node manager reference.
cd('/')
cmo.createUnixMachine(nmName)

cd('/Machines/' + nmName + '/NodeManager/' + nmName)
cmo.setListenAddress(nmAddress)
cmo.setListenPort(int(nmPort))

save()
activate()

disconnect()
exit()