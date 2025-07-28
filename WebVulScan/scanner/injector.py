import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def load_payloads(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def submit_form(form, url, payload, method="post"):
    action = form.get("action")
    post_url = urljoin(url, action)
    inputs = form.find_all("input")
    data = {}

    for input_tag in inputs:
        name = input_tag.get("name")
        input_type = input_tag.get("type")
        value = payload if input_type == "text" or input_type == "search" else "test"
        if name:
            data[name] = value

    if method == "post":
        return requests.post(post_url, data=data)
    else:
        return requests.get(post_url, params=data)
