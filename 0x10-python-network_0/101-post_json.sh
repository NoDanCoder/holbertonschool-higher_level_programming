#!/bin/bash
# Sends a JSON file and print the return message
curl "$1" -sX POST -H "Content-Type: application/json" -d @"$2"
