#!/bin/bash
# bash script that takes in URL and returns the size of the body of the response
curl -s -o /dev/null 2 -w '%{http_code}' $1 | grep -q '200' && curl -s -I -w '%{size_download}\n' $1
