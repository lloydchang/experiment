#!/bin/sh -x

if [ ! -f "main.py" ]; then
    echo "main.py not found"
    exit 1
fi

if [ -z "$GEMINI_API_KEY" ]; then
    echo "GEMINI_API_KEY not set"
    exit 1
fi

while true; do echo "edit main.py and improve it to make the world's best texas hold'em poker game and exit" | aider --analytics-disable --no-attribute-author --no-attribute-committer --yes --model gemini/gemini-1.5-flash-latest --map-tokens 1024; done
