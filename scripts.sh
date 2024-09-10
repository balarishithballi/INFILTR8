#!/bin/bash

# Function to add ~/.local/bin to PATH if it's not already there
add_to_path() {
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
        export PATH="$HOME/.local/bin:$PATH"
        echo "Added ~/.local/bin to PATH."
    else
        echo "~/.local/bin is already in PATH."
    fi
}

# Update package list and install system tools
sudo apt update

# Install tools
sudo apt install -y sublist3r theharvester sqlmap wapiti dirb nikto gobuster amass wpscan nmap openvas

# Install Impacket using pip
pip3 install impacket

# Download and install TestSSL (since it's a standalone script)
if [ ! -d "testssl" ]; then
    git clone https://github.com/drwetter/testssl.sh.git
    cd testssl.sh
    chmod +x testssl.sh
    sudo ln -s $(pwd)/testssl.sh /usr/local/bin/testssl
    cd ..
fi

# Install XSStrike
if [ ! -d "XSStrike" ]; then
    git clone https://github.com/s0md3v/XSStrike.git
    cd XSStrike
    pip3 install -r requirements.txt
    sudo ln -s $(pwd)/xsstrike.py /usr/local/bin/xsstrike
    cd ..
fi

# Install nuclei using bash script
if ! command -v nuclei &> /dev/null; then
    curl -s https://api.github.com/repos/projectdiscovery/nuclei/releases/latest | grep "browser_download_url.*linux_amd64.zip" | cut -d '"' -f 4 | wget -qi -
    unzip nuclei-linux_amd64.zip
    sudo mv nuclei /usr/local/bin/
    rm nuclei-linux_amd64.zip
fi

# Install CVE-Search
if [ ! -d "cve-search" ]; then
    git clone https://github.com/cve-search/cve-search.git
    cd cve-search
    pip3 install -r requirements.txt
    cd ..
fi
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python packages in virtual environment
echo "Installing Python packages in the virtual environment..."
pip3 install --upgrade pip setuptools wheel
pip3 install impacket dnspython python-dateutil pypsrp paramiko flask flask-sqlalchemy nltk

# Handle any specific version requirements to resolve conflicts
echo "Handling specific package version installations..."
pip3 install neo4j==4.1.1 xmltodict==0.12.0 termcolor==1.1.0 minikerberos==0.3.3

# Add ~/.local/bin to PATH if not already there
add_to_path

# Reload bashrc to apply the PATH changes
source ~/.bashrc

# Check for dependency conflicts
echo "Checking for dependency conflicts..."
pip check

# Print completion message
echo "All tools and dependencies have been installed successfully."
echo "Make sure to activate the virtual environment before running your scripts:"
echo "source venv/bin/activate"
