#!/bin/bash
# a script to check the number of bytes in response of the body
curl -s "$1" | wc -c
