import requests
import re


site_line = requests.get('http://www.columbia.edu/~fdc/sample.html').text.splitlines()
res_text = []
for line in site_line:
    match = re.compile(r"<h3.*>(.*)</h3>").search(line)
    if match:
        res_text.append(match.group(1))
print(res_text)