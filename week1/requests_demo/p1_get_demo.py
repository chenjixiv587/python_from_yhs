import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'

header = {}
header['user-agent'] = user_agent

r = requests.get("https://movie.douban.com/top250", headers=header)

print(r.status_code)
print(repr(r.encoding))
# print(r.text)
# print(r.headers)
# print(r.json())


payload = {'key1': 'hello', 'key2': 'world'}
r1 = requests.get('https://httpbin.org/get', params=payload, headers=header)
print(r1.json())
