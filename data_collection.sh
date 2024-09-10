#!/bin/bash
destinations=("www.google.com" "www.pitt.edu" "www.yahoo.com" "www.github.com" "www.microsoft.com")
measurements_per_destination=20

for destination in "${destinations[@]}"; do
    # Loop to collect measurements
    for ((measurement=1; measurement<=$measurements_per_destination; measurement++)); do
        filename="${destination}_measurement${measurement}.txt"
        traceroute "$destination" > "$filename"
        sleep 3 # Sleep for 1 hour (adjust as needed)
    done
done

