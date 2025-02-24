import requests

#values = {'key1':'value1','key2':'value2','key3':'value3'}

#respomse = requests.get("https://httpbin.org/get",params=values)

#print(f"\n[+] url final: {respomse.url}")
#print(respomse.text)

headers = {'User-Agent':'Nina'}
response = requests.get('https://google.es',headers=headers)

print(f"{response.request.headers}")
