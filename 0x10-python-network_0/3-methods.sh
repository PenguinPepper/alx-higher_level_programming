#!/bin/bash
# script that displays all HTTP methods the server of a url will accept
curl -s -I $1 | grep "Allow" | awk '{print $2, $3, $4}'
