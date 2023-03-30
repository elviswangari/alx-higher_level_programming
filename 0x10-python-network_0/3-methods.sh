#!/bin/bash
#a script to return http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
