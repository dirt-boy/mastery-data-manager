import requests
from page_util import get_login
from page_util import get_page


def save_page():
    print("Enter URI:\n")
    url=input()
    creds = get_login()
    get_page(*creds, url)

save_page()




    

