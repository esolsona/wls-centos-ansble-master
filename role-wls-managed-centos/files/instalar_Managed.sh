#!/bin/bash

# Load Environment
export CONFIG_JVM_ARGS=-Djava.security.egd=file:/dev/./urandom
. $WLS_HOME/server/bin/setWLSEnv.sh

# Create the domain.
java weblogic.WLST /tmp/create_managed_server.py -p /tmp/myDomain.properties