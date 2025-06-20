#!/usr/bin/env python3
"""
Host Header Injection Tester
Author: [kidsoncyber]
"""

import requests
import argparse
from urllib.parse import urlparse

def print_banner():
    print("""
  _   _           _     _____           _             _   _             
 | | | |         | |   |  __ \         | |           | | (_)            
 | |_| | ___  ___| |_  | |__) |__  _ __| |_ ___ _ __ | |_ _  ___  _ __  
 |  _  |/ _ \/ __| __| |  ___/ _ \| '__| __/ _ \ '_ \| __| |/ _ \| '_ \ 
 | | | | (_) \__ \ |_  | |  | (_) | |  | ||  __/ | | | |_| | (_) | | | |
 \_| |_/\___/|___/\__| |_|   \___/|_|   \__\___|_| |_|\__|_|\___/|_| |_|
 
 A simple Host Header Injection tester
 """)

def test_host_header_injection(url, headers=None, insecure=False):
    try:
        # Parse the URL to get the domain
        parsed_url = urlparse(url)
        original_host = parsed_url.netloc
        
        # Create malicious host header
        malicious_host = "evil.com"
        
        # Prepare headers
        test_headers = headers.copy() if headers else {}
        test_headers['Host'] = malicious_host
        
        # Make the request
        verify = not insecure
        response = requests.get(url, headers=test_headers, verify=verify)
        
        # Check if the malicious host appears in the response
        if malicious_host in response.text:
            print(f"[+] Vulnerable to Host Header Injection: {url}")
            print(f"    Injected Host: {malicious_host}")
            print(f"    Status Code: {response.status_code}")
            return True
        else:
            print(f"[-] Not vulnerable: {url}")
            return False
            
    except Exception as e:
        print(f"[!] Error testing {url}: {str(e)}")
        return False

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Host Header Injection Tester")
    parser.add_argument("-u", "--url", help="Target URL (e.g., https://example.com)")
    parser.add_argument("-f", "--file", help="File containing list of URLs")
    parser.add_argument("--insecure", action="store_true", help="Disable SSL verification")
    parser.add_argument("-H", "--header", action="append", help="Additional headers (e.g., -H 'Cookie: abc=123')")
    
    args = parser.parse_args()
    
    if not args.url and not args.file:
        parser.print_help()
        return
    
    # Process headers
    headers = {}
    if args.header:
        for header in args.header:
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()
    
    # Test single URL
    if args.url:
        test_host_header_injection(args.url, headers, args.insecure)
    
    # Test multiple URLs from file
    if args.file:
        with open(args.file) as f:
            urls = [line.strip() for line in f if line.strip()]
        
        for url in urls:
            test_host_header_injection(url, headers, args.insecure)

if __name__ == "__main__":
    main()
