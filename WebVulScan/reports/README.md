
# 🛡️ Web Vulnerability Scanner

A Python + Flask-based tool to scan websites for common vulnerabilities such as **Cross-Site Scripting (XSS)** and **SQL Injection (SQLi)** using custom payload injection and response analysis.

---

## 🎯 Project Objective

To build a lightweight scanner that detects security flaws in web applications by:
- Crawling target websites for forms and inputs
- Injecting XSS and SQLi payloads
- Analyzing HTTP responses
- Displaying the detected vulnerabilities with context

---

## 🔧 Tech Stack

| Tool/Library     | Purpose                              |
|------------------|--------------------------------------|
| Python           | Core scripting                       |
| Flask            | Web interface                        |
| Requests         | Sending HTTP requests                |
| BeautifulSoup    | Crawling and parsing HTML            |
| Regex            | Pattern matching in response content |

---

## 📁 Project Structure

```
WebVulnScanner/
├── scanner/
│   ├── crawler.py         # Crawls URLs and input forms
│   ├── injector.py        # Injects payloads into forms
│   ├── detector.py        # Detects vulnerabilities in response
├── payloads/
│   ├── xss.txt            # XSS test payloads
│   └── sqli.txt           # SQLi test payloads
├── webui/
│   ├── app.py             # Flask web app
│   └── templates/
│       └── index.html     # Scanner UI
├── reports/               # (Optional) Saved scan reports
├── requirements.txt
└── README.md
```

---

## 🚀 How to Use

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app**
   ```bash
   python webui/app.py
   ```

3. **Visit** [http://localhost:5000](http://localhost:5000)

4. **Enter a target URL** with public forms

5. **View results** of vulnerabilities (XSS, SQLi) in the browser

---

## 🧪 Sample Payloads Used

### 🔸 XSS
```html
<script>alert(1)</script>
<svg onload=alert(1)>
```

### 🔸 SQL Injection
```sql
' OR 1=1 --
" OR "1"="1"
admin' --
```

---

## ⚠️ Disclaimer

This tool is for **educational and ethical testing** purposes **only**. Do not scan websites you do not own or have permission to test. Unauthorized scanning may be illegal.

---
