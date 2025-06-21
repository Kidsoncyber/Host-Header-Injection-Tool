# Host Header Injection Tester  

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python)  
![License](https://img.shields.io/badge/License-MIT-green)  
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)  

A lightweight Python tool to identify and exploit Host Header Injection vulnerabilities in web applications.

## Features  

✔ Detects reflected Host header values  
✔ Supports single URL and bulk file testing  
✔ Custom headers injection  
✔ SSL verification toggle  
✔ Verbose output mode  

## Installation  

### Prerequisites  
- Python 3.6+  
- pip package manager  

### Quick Setup  
```bash
git clone https://github.com/kidsoncyber/host-header-injection-tool.git
cd host-header-injector
pip install -r requirements.txt

## Usage

### Basic Commands

```bash
# Test single URL
python host.py -u https://example.com

# Test multiple URLs from file (one per line)
python host.py -f urls.txt

# Enable verbose output mode
python host.py -u https://example.com -v
