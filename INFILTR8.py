import subprocess
import sys
import os

def run_tool(command, tool_name, output_file):
    """Run a tool and store its output in a file."""
    print(f"Running {tool_name}...")
    try:
        with open(output_file, 'w') as file:
            subprocess.run(command, shell=True, stdout=file, stderr=subprocess.STDOUT)
        print(f"{tool_name} completed. Results stored in {output_file}")
    except Exception as e:
        print(f"Failed to run {tool_name}: {e}")

def main(target_url):
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
        'nikto': (f'nikto -h {target_url} -Tuning 12345678 -output results/nikto.txt', 'Nikto'),
        'gobuster': (f'gobuster dir -u {target_url} -w /path/to/wordlist.txt -t 50 -o results/gobuster.txt', 'Gobuster'),
        'dirb': (f'dirb {target_url} /path/to/wordlist.txt -r -x .php,.html -o results/dirb.txt', 'Dirb'),
        'amass': (f'amass enum -d {target_url} -brute -o results/amass.txt', 'Amass'),
        'wpscan': (f'wpscan --url {target_url} --enumerate u,p,t --disable-tls-checks --output results/wpscan.txt', 'Wpscan'),
        'nuclei': (f'nuclei -u {target_url} -t /path/to/templates/ -o results/nuclei.txt', 'Nuclei'),
        'metasploit': (f'msfconsole -q -x "use auxiliary/scanner/http/http_version; set RHOSTS {target_url}; run; exit" > results/metasploit.txt', 'Metasploit'),
        'testssl': (f'./testssl.sh --quiet --no-failed {target_url} > results/testssl.txt', 'TestSSL'),
        'openvas': (f'openvas-start && omp -u admin -w password -h localhost -p 9390 -T xml -f results/openvas.xml', 'OpenVAS'),
        'xsstrike': (f'xsstrike -u {target_url} --crawl --follow-redirects -o results/xsstrike.txt', 'XSStrike'),
        'cve_search': (f'cve-search -q {target_url} --all -o results/cve_search.txt', 'CVE Search'),
        'sublist3r': (f'sublist3r -d {target_url} -o results/sublist3r.txt -v', 'Sublist3r'),
        'theHarvester': (f'theHarvester -d {target_url} -b all -l 200 -s -v -f results/theharvester.txt', 'theHarvester'),
        'impacket': (f'impacket-smbexec -target {target_url} -no-pass -debug > results/impacket.txt', 'Impacket'),
        'nmap': (f'nmap -sS -p- -A -T4 -oN results/nmap.txt {target_url}', 'Nmap'),
        'wapiti': (f'wapiti -u {target_url} -m all -o results/wapiti.txt', 'Wapiti')
    }

    # Run each tool
    for command, tool_name in tools.values():
        run_tool(command, tool_name, f'results/{tool_name.lower().replace(" ", "_")}.txt')

    print("All tools executed. Check the 'results' directory for output.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 INFILTR8.py {targeturl}")
        sys.exit(1)

    target_url = sys.argv[1]
    main(target_url)
