#!/bin/sh

if [ ! -f "main.py" ]; then
    echo "main.py not found"
    exit 1
fi

if [ -z "$GEMINI_APIKEY" ]; then
    echo "GEMINI_APIKEY not set"
    exit 1
fi

while true; do echo 'edit main.py and improve it to make the world's best texas hold'em poker game' | aider --analytics-disable --yes --model gemini/gemini-1.5-flash-latest --map-tokens 1024; done
