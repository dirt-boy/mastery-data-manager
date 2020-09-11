import page_util as page

def readsrc(url):
    
    creds = page.get_login()
    html = page.get_page(*creds, url)
    #test
    #print(html)
    #page.prt_scr('page1')
    print(html)
    with open('submission.html', 'w') as o:
        o.write(html)


readsrc('https://classroom.google.com/u/0/g/tg/NTQ5NzUyNTc2NjJa/MTIyNTAxNjE2Nzc1#u=MTYzNzQ0Mzk4NjRa&t=f')
