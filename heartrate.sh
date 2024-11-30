#!/bin/bash
Age=20 # Example: current heart rate of the person
Heartrate=80 # Example: current heart rate of the person

if [ "$Age" -ge 18 ]; then
    if [ "$Heartrate" -ge 60 ] && [ "$Heartrate" -le 100 ]; then
        echo "Your heart rate is within healthy range."
    else
        echo "Your heart rate is outside healthy range."
    fi
else
    echo "Heart rate range for children and teens may differ."
fi
