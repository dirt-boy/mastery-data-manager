import requests

url = "https://classroom.google.com/u/1/v7/rubric/list?_reqid=1163629&rt=j"

payload = 'f.req=%5B%5Bnull%2C%5B%5B%2252609649719%22%2C%22102616360750%22%5D%5D%5D%5D&token=ABFGqemQrjMFXA3O5fs39DRRATi_wxbNow%3A1591663228646'
headers = {
  'Cookie': 'CONSENT=YES+US.en+20171003-07-0; SEARCH_SAMESITE=CgQIlY8B; __Secure-3PSIDCC=AJi4QfHh8DTV9_4ho8OznwmRLLNHubONUxiWDbyNr29_s6_8Pobpo2boHzemefCDQCVK-XBy; HSID=AEXu4_ZLoDKi6wUGF; SSID=AR9iFZ9ZUAuatH6Tc; APISID=yPX2AI_wc8AnBSkn/AEFaPR1ATrdLL3-J6; SAPISID=UioL0zT532HWwv8X/Ad2wyOMxO8mBMTKwR; __Secure-HSID=AEXu4_ZLoDKi6wUGF; __Secure-SSID=AR9iFZ9ZUAuatH6Tc; __Secure-APISID=yPX2AI_wc8AnBSkn/AEFaPR1ATrdLL3-J6; __Secure-3PAPISID=UioL0zT532HWwv8X/Ad2wyOMxO8mBMTKwR; SID=yAcFG9OVizREJG4pJPugt7e8fZ4TLZ5EmintA9TvxQLmbzoyVuiGDve16sxTb3TR0H_mKQ.; __Secure-3PSID=yAcFG9OVizREJG4pJPugt7e8fZ4TLZ5EmintA9TvxQLmbzoy26bfIulHVlLzJv8s9DJsHw.; NID=204=0vAXVplDD2mOTGPPlf8jkgkJi6iFWLq2wi0t9JjDaG4b7_zry2zRFhH5tY7w95hG7gChh4vi1SQLye5y-jxth1F03r6D5TpmkFcYGoXTGeA06ahQ_CQNBMpKXLQbB3bROsDuYGeGR2aGoqAMCPbnfEV6v5fPQ2FtbCRRl7mZLogzwVUUllDFuX5jDW7-aF4BBpXW0v9Eeq5qM_NcxNiQkFgXsqW-wZkuyYibZG3AFbY-qKzKP_u0xxMDQ0ZkDNzHctPtjpGT9D-5-g_ryp_JwXEIWH4LTrPhCi3s; ANID=AHWqTUnhMtH7knD1UYhuh6dG8DQ9n-r0EjUys_0YHojYGUq_N-fyU7IB3837DLdo; 1P_JAR=2020-6-19-22; OTZ=5505052_84_88_104280_84_446940; SIDCC=AJi4QfFhFjeXjkYt1SeJS7h8-OTbCHULvRhOOrRNmN6aKAtsN6p1HMy_VJHEWXFE5QtOrkrmfTPa',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

