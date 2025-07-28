from crawler import find_forms
from injector import load_payloads, submit_form
from detector import detect_xss, detect_sqli

def scan_for_vulns(target_url):
    forms = find_forms(target_url)
    xss_payloads = load_payloads("payloads/xss.txt")
    sqli_payloads = load_payloads("payloads/sqli.txt")

    print(f"Found {len(forms)} form(s) on {target_url}")
    
    for form in forms:
        print("[+] Testing form...")
        for payload in xss_payloads:
            response = submit_form(form, target_url, payload)
            if detect_xss(response, payload):
                print(f"[!] XSS vulnerability detected with payload: {payload}")
        
        for payload in sqli_payloads:
            response = submit_form(form, target_url, payload)
            if detect_sqli(response):
                print(f"[!] SQL Injection vulnerability detected with payload: {payload}")

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    scan_for_vulns(url)
