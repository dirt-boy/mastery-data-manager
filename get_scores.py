"""Writes grade data to 'submission.html'."""
import page_util as page


def readsrc(url):

    creds = page.get_login()
    html = page.get_page(*creds, url)
    #test
    #print(html)
    with open('submission.html', 'w') as o:
        o.write(html)


readsrc('https://classroom.google.com/u/3/c/NTQ5NzUyNTc2NjJa/a/MTIyNTAxNjE2Nzc1/submissions/by-status/and-sort-name/student/MTYzNzQ0Mzk4NjRa')
