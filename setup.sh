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
sudo apt install -y sqlmap wapiti nikto gobuster amass wpscan nmap

# Install Impacket using pip
pip3 install impacket

# Install XSStrike
if [ ! -d "XSStrike" ]; then
    git clone https://github.com/s0md3v/XSStrike.git
    cd XSStrike
    chmod +x *
    pip3 install -r requirements.txt
    sudo ln -s $(pwd)/xsstrike.py /usr/local/bin/xsstrike
    cd ..
fi

# Install CVE-Search
if [ ! -d "cve-search" ]; then
    git clone https://github.com/cve-search/cve-search.git
    cd cve-search
    chmod +x *
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
