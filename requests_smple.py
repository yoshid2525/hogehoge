import requests

#r=requests.get("https://ja.wikipedia.org/")
#print(r.status_code)
"""
r=requests.get("https://hatena.blog")

print(r.status_code)
print(r.text[:100])
"""
r=requests.get(
    'https://weather.tsukumijima.net/api/forecast/?city=130010'
)

print(r.status_code)
print(r.headers)
print(r.json())