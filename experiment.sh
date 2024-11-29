#!/bin/sh

while true; do echo 'edit main.py randomly and exit' | aider --analytics-disable --yes --model gemini/gemini-1.5-flash-latest --map-tokens 1024; done
