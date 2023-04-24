#!/bin/bash
# script that sends a request to an ip address
curl -s -X PUT -d 'user_id=98' 0.0.0.0:5000/catch_me -L
