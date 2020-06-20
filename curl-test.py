import requests

url = "https://classroom.google.com/u/1/v7/rubric/list?_reqid=1163629&rt=j"

payload = 'f.req=%5B%5Bnull%2C%5B%5B%2252609649719%22%2C%22102616360750%22%5D%5D%5D%5D&token=ABFGqemQrjMFXA3O5fs39DRRATi_wxbNow%3A1591663228646'
headers = {
  'X-Same-Domain': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'Accept': '*/*',
  'Cookie': 'CONSENT=YES+US.en+20171003-07-0; SEARCH_SAMESITE=CgQIlY8B; __Secure-3PSIDCC=AJi4QfHh8DTV9_4ho8OznwmRLLNHubONUxiWDbyNr29_s6_8Pobpo2boHzemefCDQCVK-XBy',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Authorization': 'Bearer ya29.a0AfH6SMAgHiPKt9226_LUc5MGb3uSlqYvocJC5tWzINout8fGiBMo6AkdmolkObTLdcATkQDGtXJZbVY1kLvRAqwJLeSYEzpfs6pG63GE5K2RI7NMlZftQlBgAwaX4ucRbrnJeHM0Fo1Uf-dG-MVTf4T0kaTDlwZcq47EVCe9-1VwSIY',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
