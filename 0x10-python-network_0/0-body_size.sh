#!/usr/bin/env bash
# bash script that takes in URL and returns the size of the body of the response
curl -size_download $1 
