#!/bin/bash
# takes URL as arg sends GET request with additional info
curl -sH "X-School-User-Id: 98" "$1"
