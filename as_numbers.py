import os
import re
import csv
import subprocess
from collections import defaultdict
import subprocess
def extract_url_from_filename(filename):
    # This regex will match the URL part before '_measurement'
    match = re.match(r"www\.(.+?)_measurement", filename)
    if match:
        return match.group(1).replace('_', '.')
    return "URL Not Found"
def bulk_whois_lookup(ip_list, whois_server):
    with open('ips_for_whois.txt', 'rb') as f:
        file_contents = f.read()
    result = subprocess.run(['netcat', whois_server, '43'], 
                            input=file_contents, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE)
    if result.stderr:
        print(f"Error: {result.stderr.decode('utf-8')}")
        return {}
    sorted_result = sorted(result.stdout.decode('utf-8').splitlines())

    as_info = {}
    for line in sorted_result:
        parts = line.split('|')
        if len(parts) > 1 and re.match(r'\d+\.\d+\.\d+\.\d+', parts[1].strip()):
            ip = parts[1].strip()
            as_number = parts[0].strip()
            as_info[ip] = as_number

    return as_info
def parse_traceroute(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    hop_data = []
    ip_pattern = re.compile(r'\((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\)')
    for line in lines:
        hop_number_match = re.findall(r'^\s*(\d+)', line)
        if not hop_number_match:
            print(f"No hop number match for line: {line}")
            continue
        hop_number = hop_number_match[0]
        ips = ip_pattern.findall(line)
        if not ips:
            print(f"No IP address match for line: {line}")
            continue
        ip = ips[0]

        # Extract the latencies
        latencies = re.findall(r'(\d+\.\d+)\s+ms', line)
        if not latencies:
            print(f"No latency match for line: {line}")

        hop_data.append((hop_number, ip, latencies))
    return hop_data

root_dir = '/mnt/c/users/bhars/documents/aon_project'
output_csv = '/mnt/c/users/bhars/documents/aon_project/traceroute_analysis.csv'

unique_ips = set()

for subdir, dirs, files in os.walk(root_dir):
    for filename in files:
        if not filename.endswith('.txt'):
            continue
        file_path = os.path.join(subdir, filename)
        hop_data = parse_traceroute(file_path)
        for hop_number, ip, latencies in hop_data:
            unique_ips.add(ip)

as_info = bulk_whois_lookup(list(unique_ips), 'whois.cymru.com')
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Added 'URL' to the header
    writer.writerow(['Date', 'Hop Number', 'IP Address', 'AS Number', 'Latency 1', 'Latency 2', 'Latency 3', 'URL'])
    for subdir, dirs, files in os.walk(root_dir):
        date = os.path.basename(subdir)
        for filename in files:
            if not filename.endswith('.txt'):
                continue
            url = extract_url_from_filename(filename)
            file_path = os.path.join(subdir, filename)
            hop_data = parse_traceroute(file_path)
            for hop_number, ip, latencies in hop_data:
                latencies.extend([''] * (3 - len(latencies)))  # Pad latencies to ensure 3 values
                # Added the URL to the row data
                writer.writerow([date, hop_number, ip, as_info.get(ip, 'AS Not Found')] + latencies + [url])

print(f"Data has been written to {output_csv}")
