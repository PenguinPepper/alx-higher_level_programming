#!/bin/bash
# bash script that takes in URL and returns the size of the body of the response
curl -s -w "% {size_download}" "$1"
