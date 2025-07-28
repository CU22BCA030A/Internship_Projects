def detect_xss(response, payload):
    return payload in response.text

def detect_sqli(response):
    errors = ["you have an error in your sql syntax", "sql error", "warning: mysql", "unclosed quotation"]
    for error in errors:
        if error.lower() in response.text.lower():
            return True
    return False
