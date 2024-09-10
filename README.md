
# Path Stability Analysis Using Traceroute and Autonomous System Mapping

This project is focused on analyzing Autonomous System (AS) and router-level path stability using traceroute measurements. It includes various scripts and data collection processes to measure and visualize path stability in terms of delay and network hops.

## Project Overview
This project collects daily traceroute measurements, processes the results, and visualizes the stability of network paths at both the AS and router levels. The goal is to understand how paths change over time, particularly focusing on delay and route stability.

## Directory Structure
- **11_21_23 to 11_26_23**: Folders containing daily traceroute measurements for the respective dates.
- **AS_Level_Plots/**: Contains visualizations showing the stability of paths at the AS level.
- **Delay_Stability_Plots/**: Visualizations that show the delay stability of end-to-end paths, focusing on how delays change over time.
- **Router_Level_Plots/**: Visualizations depicting the stability of network paths at the router level.
- **as_numbers.py**: A script that processes the traceroute measurement files, maps IP addresses to Autonomous System (AS) numbers using bulk WHOIS lookup, and outputs enriched data with AS information and latencies to a CSV file.
- **data_collection.sh**: A script for collecting data, possibly invoking traceroute or other network measurement tools.
- **ips_for_whois.txt**: A text file containing the list of IP addresses used for bulk WHOIS lookups.
- **traceroute_analysis.csv**: The aggregated results of traceroute measurements, including AS numbers and corresponding latencies.
- **AON_PROJECT2_REPORT_HarshithaBatta.pdf**: The project report detailing objectives, methods, and results.

## Requirements
To run the scripts and process the data, the following tools are required:
- Python 3.x
- `matplotlib` (for visualizing the data)
- `requests` (for making network requests if needed for WHOIS lookups)

You can install the required Python libraries using:

```bash
pip install matplotlib requests
```

## How to Use
1. **Data Collection**: The script `data_collection.sh` collects the traceroute measurements. You can run this script to gather fresh data.
   
   ```bash
   bash data_collection.sh
   ```

2. **Process Data**: Use `as_numbers.py` to process the traceroute data and enrich it with AS-level information.
   
   ```bash
   python as_numbers.py
   ```

3. **View Results**: Explore the visualizations in the `AS_Level_Plots`, `Router_Level_Plots`, and `Delay_Stability_Plots` directories to analyze path stability over time.

## Features
- **Traceroute Measurements**: Daily measurements across multiple dates for analyzing path stability.
- **AS Mapping**: Enrich traceroute data by mapping IP addresses to their respective AS numbers.
- **Stability Analysis**: Visualize the stability of paths at both the router and AS levels.

## Authors
This project was developed by Harshitha Batta as part of the AON Project.
