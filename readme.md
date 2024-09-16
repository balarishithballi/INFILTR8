# Infiltr8

![Infiltr8 Banner](/assets/Banner.png) <!-- Replace with actual banner image URL -->

Infiltr8 is a comprehensive penetration testing tool designed to automate the execution of various security tools and generate detailed results for security assessments. Developed by r3tr0, Infiltr8 simplifies the process of running multiple security scans and consolidates the results into a single directory for easy review.

## Features

- **Automated Scanning**: Executes a suite of popular security tools including SQLmap, Nikto, Gobuster, Dirb, and more.
- **Comprehensive Results**: Stores output from each tool in a dedicated directory for easy access and analysis.
- **Customizable**: Easily add or modify tools and their configurations to suit specific needs.
- **Cross-Platform**: Designed to run on Linux systems.

## Tools Included

- **SQLmap**: Automated SQL injection and database takeover tool.
- **Nikto**: Web server scanner to identify vulnerabilities.
- **Gobuster**: Directory and file brute-forcer.
- **Amass**: Subdomain enumeration tool.
- **WPScan**: WordPress vulnerability scanner.
- **Metasploit**: Penetration testing framework.
- **XSStrike**: Cross-site scripting (XSS) vulnerability scanner.
- **CVE Search**: Searches for CVE information.
- **Impacket**: Collection of Python classes for working with network protocols.
- **Nmap**: Network discovery and security auditing tool.
- **Wapiti**: Web application vulnerability scanner.

## Installation

### Prerequisites

Ensure the following tools are installed on your system:

- **SQLmap**
- **Nikto**
- **Gobuster**
- **Amass**
- **WPScan**
- **Metasploit Framework**
- **XSStrike**
- **CVE Search**
- **Impacket**
- **Nmap**
- **Wapiti**

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/balarishithballi/INFILTR8.git
   cd INFILTR8
Run the Installation Script

Ensure that the script.sh file is executable and then run it to install any additional dependencies:

```bash
  chmod +x setup.sh
  ./setup.sh
```
This script will handle the installation of required Python packages and other dependencies.

Usage
To run Infiltr8, use the following command:

```bash
python3 infiltr8.py {target_url} #note url==> HTTP (OR) HTTPS
```
Replace {target_url} with the URL of the target you want to scan.

Example
```bash
python3 infiltr8.py http://example.com
```
This command will initiate a series of scans against the provided target URL and store the results in the results directory.

## Future Plans

- **GUI Interface**: Develop a graphical user interface (GUI) for easier configuration and result visualization.
- **Advanced Reporting**: Implement advanced reporting features, including customizable reports and interactive data visualizations.
- **Integration with CI/CD**: Integrate Infiltr8 with continuous integration/continuous deployment (CI/CD) pipelines for automated security assessments during development.
- **Extended Tool Support**: Add support for additional security tools and frameworks based on user feedback and emerging security trends.
- **Enhanced Configuration**: Provide a more flexible configuration system to allow users to customize tool settings and scan parameters more easily.


Contributing
Contributions to Infiltr8 are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
Infiltr8 is licensed under the MIT License. See the LICENSE file for more information.

Contact
For any questions or feedback, please contact:

Author: r3tr0
Email: balligowri70@gmail.com
GitHub: https://github.com/BALARISHITHBALLI
Infiltr8 is a tool designed for ethical hacking and security assessments. Ensure you have permission before using it on any system or network.

### Notes
- **Replace placeholders**: Make sure to replace placeholder text (like image URLs and email addresses) with actual content.
- **Update tool paths**: Verify the paths in the `script.sh` and ensure they are correctly set in the `infiltr8.py` script.
