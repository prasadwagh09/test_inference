import requests

url = "https://trp-kepler.cloud.databricks.com/driver-proxy-api/o/4081298629713390/0717-182324-1bm6jlnr/7777"
# url = "http://localhost:8000/"

headers = {
    "Authorization": "Bearer REPLACE_ME"
}

with requests.get(url, headers=headers, stream=True) as r:
    for chunk in r.iter_content(1024):  # or, for line in r.iter_lines():
        print(chunk)