#!/bin/bash
# sends a request to a URL passed as an arg displays status cpde
curl -s -w "%{http_code}" "$1" -o /dev/null
