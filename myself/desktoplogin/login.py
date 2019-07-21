#https://www.simplifiedpython.net/python-gui-login/
#https://www.datacamp.com/community/tutorials/gui-tkinter-python
#import modules
# installer 는 pyinstaller로 
# 근데 적당한 크롬 드라이버 버전별로 세팅하는 것도 필요하고, 시작프로그램에 얹는 것도 필요함.

#%%file = homepath + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

from tkinter import *
from selenium import webdriver
import os
from datetime import datetime
import chromedriver_binary
import edussafylogin


def login():
    username_info = username.get()
    password_info = password.get()
    loginfile = open(homepath+'\\username.txt','w')
    loginfile.write(username_info)
    loginfile.close()
    edussafylogin.login(username_info, password_info, True)
    
def logout():
    username_info = username.get()
    password_info = password.get()
    edussafylogin.login(username_info, password_info, False)
    
def reset_screen():
    yesBtn.forget()
    noBtn.forget()
    loginBtn.pack()
    logoutBtn.pack()
    sixLabel.forget()


def logoutcheck():
    if datetime.now().hour <= 24:
        global sixLabel
        sixLabel = Label(main_screen, text = '6시 전입니다.\n 진짜 퇴실하시겠습니까?')
        sixLabel.pack()
        loginBtn.forget()
        logoutBtn.forget()
        global yesBtn
        global noBtn
        yesBtn = Button(text="Yes", height="1", width="15", command = logout)
        noBtn = Button(text="No", height="1", width="15", command=reset_screen)
        yesBtn.pack()
        noBtn.pack()
    else:
        logout()      

# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    filepath = homepath+'\\username.txt'
    if os.path.isfile(filepath):
        loginfile = open(filepath,'r')
        
    else:
        loginfile = open(filepath,'w')
    
    global username
    global password
    username = StringVar()
    password = StringVar()
    username.set(loginfile.read())

    main_screen.geometry("300x250")
    main_screen.title("간단입퇴실")
    Label(text="Username * ").pack()
    username_login_entry = Entry(main_screen, textvariable=username)
    username_login_entry.pack()
    Label(text="Password * ").pack()
    password_login_entry = Entry(main_screen, textvariable=password, show= '*')
    password_login_entry.pack()
    Label(text="").pack()
    global loginBtn
    global logoutBtn
    loginBtn = Button(text="입실", height="1", width="15", command = login)
    logoutBtn = Button(text="퇴실", height="1", width="15", command= logoutcheck)
    loginBtn.pack()
    logoutBtn.pack()

    main_screen.mainloop()


#start of program
homepath = os.path.expanduser('~')
main_account_screen()