#!/bin/bash
# bash script that takes in URL and returns the size of the body of the response
curl -s -I $1 | grep Content-Length
