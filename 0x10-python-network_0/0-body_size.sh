#!/bin/bash
# bash script that takes in URL and returns the size of the body of the response
curl -s $1 -o /dev/null -w "%{size_download}\n"
