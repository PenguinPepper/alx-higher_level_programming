#!/bin/bash
# script that sends a GET request with a custom header to a URL using curl
curl -s $1 -H "X-School-User-Id: 98"
