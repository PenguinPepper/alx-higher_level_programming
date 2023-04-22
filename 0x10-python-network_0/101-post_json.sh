#!/bin/bash
# script that sends a JSON POST request to a URL using curl
curl -s $1 -X POST -d @$2 -H 'Content-Type: application/json'
