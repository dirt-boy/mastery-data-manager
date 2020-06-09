import requests

url = "https://classroom.google.com/u/1/v7/rubric/list?_reqid=1163629&rt=j"

payload = 'f.req=%5B%5Bnull%2C%5B%5B%2252609649719%22%2C%22102616360750%22%5D%5D%5D%5D&token=ABFGqemQrjMFXA3O5fs39DRRATi_wxbNow%3A1591663228646'
headers = {
  'X-Same-Domain': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'Accept': '*/*',
  'Cookie': 'CONSENT=YES+US.en+20171003-07-0; SEARCH_SAMESITE=CgQIlY8B; __Secure-3PSIDCC=AJi4QfHh8DTV9_4ho8OznwmRLLNHubONUxiWDbyNr29_s6_8Pobpo2boHzemefCDQCVK-XBy; S=billing-ui-v3=yMTcgS8BK7AiitGuusG2ImLhaqNkwHNd:billing-ui-v3-efe=yMTcgS8BK7AiitGuusG2ImLhaqNkwHNd; ANID=AHWqTUl0W2FeTnQYEWx_wv6WuPWTsBUHxz1-Laezg8ezmouyK_pKa9crWB2epba7; SID=xwcFG7bbFUjVF_UZHA4Jky-NIojCmhk5cpXK_2VAV6RD3CS7eL333M0ceJxjsJjuENJ0mA.; __Secure-3PSID=xwcFG7bbFUjVF_UZHA4Jky-NIojCmhk5cpXK_2VAV6RD3CS7NU2cLC8Hn7hGFeaaYrklqw.; HSID=AfYHhP7GWQxzBlI_b; SSID=ARWFxjX7o7D2GBHIa; APISID=4W60Ax90-YnLEGPb/APzQ4Gr-es7grVfjO; SAPISID=mEMfu2Bio52-rx6d/AAydCbzBML3HqWhZY; __Secure-HSID=AfYHhP7GWQxzBlI_b; __Secure-SSID=ARWFxjX7o7D2GBHIa; __Secure-APISID=4W60Ax90-YnLEGPb/APzQ4Gr-es7grVfjO; __Secure-3PAPISID=mEMfu2Bio52-rx6d/AAydCbzBML3HqWhZY; NID=204=O_XN59FdhqbWB61eIiAjDHt6Vtp55C46O3X1-VOfWT-DynCHr3lVo_tYHWS_AdQOY4e3Pc6DILLefgGNYErIZL97lH6UimTSwEJW8o-1j8aD-eiptnxWS6QDBgrxvdSFbjVKlVkUkMkA9B3MRES9V6e-uxQ3w2PVu4N_SY3VxoIuTt5XC5D1NgP7mhY922-93M6Ud6_waROYCjgO0L2ZcH4nAfWz-agjXlrJTWhfji8AgODXwpRZLf1emlD7w2OA4Z5Lksr4TA; 1P_JAR=2020-6-9-0; OTZ=5489320_84_88_104280_84_446940; SIDCC=AJi4QfF3v2R3r7xKnbuhajwCsT6YMQnaNJwdO3EctCMQLpSEIEDSbpqQsQrM5GkuODYVM6sthGc',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Authorization': 'Bearer ya29.a0AfH6SMAgHiPKt9226_LUc5MGb3uSlqYvocJC5tWzINout8fGiBMo6AkdmolkObTLdcATkQDGtXJZbVY1kLvRAqwJLeSYEzpfs6pG63GE5K2RI7NMlZftQlBgAwaX4ucRbrnJeHM0Fo1Uf-dG-MVTf4T0kaTDlwZcq47EVCe9-1VwSIY',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

