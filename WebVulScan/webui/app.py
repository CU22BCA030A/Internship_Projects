import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scanner.crawler import find_forms
from scanner.injector import load_payloads, submit_form
from scanner.detector import detect_xss, detect_sqli
from flask import Flask, render_template, request
from scanner.crawler import find_forms
from scanner.injector import load_payloads, submit_form
from scanner.detector import detect_xss, detect_sqli

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        url = request.form.get("url")
        forms = find_forms(url)
        xss_payloads = load_payloads("payloads/xss.txt")
        sqli_payloads = load_payloads("payloads/sqli.txt")

        for form in forms:
            for payload in xss_payloads:
                response = submit_form(form, url, payload)
                if detect_xss(response, payload):
                    results.append({
                        "type": "XSS",
                        "payload": payload,
                        "url": url
                    })

            for payload in sqli_payloads:
                response = submit_form(form, url, payload)
                if detect_sqli(response):
                    results.append({
                        "type": "SQLi",
                        "payload": payload,
                        "url": url
                    })
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
