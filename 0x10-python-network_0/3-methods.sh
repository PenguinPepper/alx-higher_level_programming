#!/bin/bash
# script that displays all HTTP methods the server of a url will accept
curl -s -D "$1" | grep -q "allow"
