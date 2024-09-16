import subprocess
import socket
import sys
import os
import re
from urllib.parse import urlparse

def run_tool(command, tool_name, output_file):
    """Run a tool and store its output in a file."""
    print(f"Running {tool_name}...")
    try:
        with open(output_file, 'w') as file:
            subprocess.run(command, shell=True, stdout=file, stderr=subprocess.STDOUT)
        print(f"{tool_name} completed. Results stored in {output_file}")
    except Exception as e:
        print(f"Failed to run {tool_name}: {e}")

def resolve_ip(url):
    domain = urlparse(url).netloc
    try:
        return socket.gethostbyname(domain)
    except socket.error as err:
        print(f"Error resolving IP for {domain}: {err}")
        return None

def is_valid_url(url):
    """Check if the target URL is valid."""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def main(target_url):
    if not is_valid_url(target_url):
        print(f"Invalid URL format: {target_url}")
        sys.exit(1)
    
    # Resolve the URL to an IP address
    target_ip = resolve_ip(target_url)
    if not target_ip:
        sys.exit(1)

    # Ensure results directory exists
    if not os.path.exists('results'):
        os.makedirs('results')

    print("""
    ==================================
            Infiltr8
          Made by r3tr0
    ==================================
    """)
    print("It may take some time, please wait")

    # Define tool commands and their output files
    tools = {
        'sqlmap': (f'sqlmap -u {target_url} --batch --crawl=2 --risk=3 --level=5 --output-dir=results --tamper=between', 'Sqlmap'),
        'nikto': (f'sudo nikto -h {target_url} -Tuning 12345678 -output results/nikto.txt', 'Nikto'),
        'gobuster': (f'gobuster dir -u {target_url} -w wordlist.txt -t 50 -o results/gobuster.txt', 'Gobuster'),
        'amass': (f'amass enum -d {target_url} -brute -o results/amass.txt', 'Amass'),
        'wpscan': (f'wpscan --url {target_url} --enumerate u,p,t --disable-tls-checks --output results/wpscan.txt', 'Wpscan'),
        'metasploit': (f'msfconsole -q -x "use auxiliary/scanner/http/http_version; set RHOSTS {target_url}; run; exit" > results/metasploit.txt', 'Metasploit'),
        'xsstrike': (f'python3 XSStrike/xsstrike.py -u {target_url} --crawl -o results/xsstrike.txt', 'XSStrike'),
        'cve_search': (f'./cve-search.sh {target_url}', 'CVE Search'),
        'impacket': (f'impacket-smbexec {target_ip} -no-pass -debug > results/impacket.txt', 'Impacket'),
        'nmap': (f'sudo nmap -sS -p- -T5 -oN results/nmap.txt {target_ip}', 'Nmap'),
        'wapiti': (f'wapiti -u {target_url} -m all -o results/wapiti.txt', 'Wapiti')
    }

    # Run each tool
    for command, tool_name in tools.values():
        run_tool(command, tool_name, f'results/{tool_name.lower().replace(" ", "_")}.txt')

    cve_search_script = './cve-search.sh'
    cve_search_output = 'results/cve-search-results.txt'
    run_tool(f'{cve_search_script} {target_url}', 'CVE Search', cve_search_output)

    print("All tools executed. Check the 'results' directory for output.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 INFILTR8.py http://{targeturl}/")
        sys.exit(1)

    target_url = sys.argv[1]
    main(target_url)
