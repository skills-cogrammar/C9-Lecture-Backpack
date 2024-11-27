#!bin/bash

# Create a maximum threshold variable:
THRESHOLD=80

# Determine usage and store in a variable too:
USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//')

# If the threshold is greater than usage: run sudo apt clean.
if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Warning storage is above $THRESHOLD. Clearing Cache."
    sudo apt clean
    echo "Cache Cleared"
else
    echo "Within threshold. All good."
fi

