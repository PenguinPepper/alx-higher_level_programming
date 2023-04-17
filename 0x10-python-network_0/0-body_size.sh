#!/bin/bash
# bash script that takes in URL and returns the size of the body of the response
curl -s -D $1 | grep content-length > /dev/null
