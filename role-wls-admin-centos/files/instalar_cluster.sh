#!/bin/bash

# Load Envi ronment
export CONFIG_JVM_ARGS=-Djava.security.egd=file:/dev/./urandom
. $WLS_HOME/server/bin/setWLSEnv.sh

# Create the domain.
java weblogic.WLST /tmp/create_cluster.py -p /tmp/myDomain.properties