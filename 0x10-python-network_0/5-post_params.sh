#!/bin/bash
# script that taks in a URL, sends a POST request to the passed url and shows response body
curl -s $1 -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
