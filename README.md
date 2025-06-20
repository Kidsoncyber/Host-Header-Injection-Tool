# Host Header Injection Tester

A simple Python tool to test for Host Header Injection vulnerabilities.

## Features

- Tests for reflected Host header values
- Supports single URL or file input
- Custom headers support
- SSL verification toggle

## Installation

```bash
git clone https://github.com/kidsoncyber/host-header-injector.git
cd host-header-injector
pip install -r requirements.txt

## Usage

# Test single URL
python host.py -u https://example.com

# Test multiple URLs from file
python host.py -f urls.txt

# Disable SSL verification
python host.py -u https://example.com --insecure

# Add custom headers
python host.py -u https://example.com -H "Cookie: session=123" -H "User-Agent: TestAgent"
