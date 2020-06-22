import requests

url = "https://classroom.google.com/u/1/v7/rubric/list?_reqid=1163629&rt=j"

payload = {'f.req': '[[null,[["52609649719","102616360750"]]]]',
'token': 'ABFGqemQrjMFXA3O5fs39DRRATi_wxbNow:1591663228646'}
files = [

]
headers = {
  'Cookie': 'ANID=AHWqTUkSA4GcxQeoHirJKjy25AYtkMAZho7SNuxJ97xBt0d0R6U-Wk6X_44JkpbK; CONSENT=YES+US.en+20171003-07-0; HSID=A1Q99c4uOj7fTrBgX; SSID=AxIeOcY1fr28EpHCE; APISID=NP5Et1Fb-YNVsKqV/AnOoFBmuaYj4ElfbL; SAPISID=7h36qWjf3VH-0SHL/AWYa3iYfpAIJjjvWW; __Secure-HSID=A1Q99c4uOj7fTrBgX; __Secure-SSID=AxIeOcY1fr28EpHCE; __Secure-APISID=NP5Et1Fb-YNVsKqV/AnOoFBmuaYj4ElfbL; __Secure-3PAPISID=7h36qWjf3VH-0SHL/AWYa3iYfpAIJjjvWW; NID=204=vdbUXuv0p8wSICHgbfvdc7sMznKoxdke3rGgnTloVJIgwcbQUs_kTlt-A2vNjXl4amkMygZjuTs1n-Ar1GsiCjNf1smPZcSNtuqPkpH-jTA3DFwAtcnnJ52BlSezzihheoE1bshkje7h2ovDNRj_425s0Xb-SM4hg5cMC_ypF-Uhr-p3l1NvZJbU4Ts2xtdMX_RLKUVI02C-R3sSnQU1lUo8HXEnkNaTbWmCfJsu6r-TCpRfQY4qQcOm0YqH062XIk7RRZSRXPsEP36Urval9zLvHuNs; 1P_JAR=2020-6-22-5; SID=yQe4Fnoo3pKCQa9ZxsVYiE8_ra4_rfWZa30hIr6I6-qQIuTOYxuh_Fq4YAVHAy0GgwaO5A.; __Secure-3PSID=yQe4Fnoo3pKCQa9ZxsVYiE8_ra4_rfWZa30hIr6I6-qQIuTO3Wb15U1v-OXaSb6xb1H67Q.; OTZ=5508341_84_88_104280_84_446940; SIDCC=AJi4QfFPy5yZ4Bg0FOgHVB7l2Yp7cgbk69NE1RFfpGorEg5t_cl1cFbeMlxYjedCorvTgP2cmA',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Authorization': 'Bearer ya29.a0AfH6SMCgCyleO0o2MS0Gu8rryJyYYkT-PKKmPENFPYWTgjL6cjrlOzhG_ebyH5rmiQACLPIgyz59sxqdvGqhe77vAXEQIc96ucK295-2TiDD6XV2DAE22b4NsEp9dsw7BP4QIE5MwhSaPi6cdoogfGzXPcUG5My1OV8'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
