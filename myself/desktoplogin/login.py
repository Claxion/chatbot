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

# print(os.path.expanduser('~'))
# def register_user():

#     username_info = username.get()
#     password_info = password.get()

#     file = open(username_info, "w")
#     file.write(username_info + "\n")
#     file.write(password_info)
#     file.close()

#     username_entry.delete(0, END)
#     password_entry.delete(0, END)

#     Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Designing Main(first) window
def checktime_screen():
    global checktime_screen
    checktime_screen = Toplevel(main_screen)
    checktime_screen.title('퇴실시간체크')
    checktime_screen.geometry('200x100')
    Label(checktime_screen, text = '6시 전입니다.\n 진짜 퇴실하시겠습니까?').pack()
    Button(checktime_screen, text='yes',width=10, height = 1, command='').pack()
    Button(checktime_screen, text='no',width=10, height = 1, command='').pack()
    checktime_screen.lift()

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
    Label(text="").pack()
    Label(text="Password * ").pack()
    password_login_entry = Entry(main_screen, textvariable=password, show= '*')
    password_login_entry.pack()
    Label(text="").pack()
    Button(text="입실", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="퇴실", height="2", width="30", command= logout).pack()
    
    if datetime.now().hour <= 24:
        checktime_screen()
    else :
        pass
    main_screen.iconify()
    main_screen.mainloop()



homepath = os.path.expanduser('~')


main_account_screen()

#%%
