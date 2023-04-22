#!/bin/bash
# script that displays all HTTP methods the server of a url will accept
curl -s $1 -D /dev/null | grep -q "allow"
