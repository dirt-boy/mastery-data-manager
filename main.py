from functools import partial
from tkinter import *

#import data_options as opts
import course_util as course
import page_util as page

creds = page.get_login()


def validateLogin(username, password):
    print(creds[0]+": "+username.get())
    print(creds[1]+": "+password.get())
    if username.get()==creds[0] and password.get()==creds[1]:
        print("Login successful. Retrieving Classroom Data...")
        course.pullall()
        return

    else:
        print("Username/Password combination did not match credentials on file.")
        return



'''
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

'''

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
