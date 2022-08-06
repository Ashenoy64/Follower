from tkinter import *
import smtplib
import instaloader
from tkinter.ttk import Progressbar
import time

from py import process
#Main Window
master=Tk()
master.title("Following Back")
master.geometry("500x300")

#Variables
res1=BooleanVar()
res2=BooleanVar()

#All the functions
def ask():
    l=password_l
    l2=password
    if res1.get():
        l.grid(column=0,row=5,sticky=W)
        l2.grid(column=2,row=5)
    else:
        l.grid_remove()
        l2.grid_remove()    
def ask2():
    if res2.get():
        ask_email.grid(column=0,row=7,sticky=W)
        gmail.grid(column=2,row=7)
    else:
        ask_email.grid_remove()
        gmail.grid_remove()    

def send():
    gmail_user='default'
    gmail_password='default password'
    sent_from=gmail_user
    subject="Instagram Followers"
    global body


    try:
        smtp=smtplib.SMTP('smtp.gmail.com',587)
        smtp.starttls()
        smtp.login(sent_from,gmail_password)    

        email_text="""\
        From:%s
        To:%s
        Subject:%s
        %s"""%(sent_from,gmail.get(),subject,body)
        smtp.sendmail(sent_from,gmail.get(),email_text)
        smtp.quit()
        mail_notice.config(text="Email has been Sent")
    except Exception as ex:
        mail_notice.config(text="Something went wrong While Sending a mail")
             
    

def search():
    global body
    body=""
    global no
    if username.get()=="":
        notice.config(text="Username must not be Empty")
    elif not res1 and password!="":
        notice.config(text="Password shoudnt be Empty")
    else:
        Searching=Toplevel(master)
        Searching.title("Searching")
        loader=instaloader.Instaloader()
        
        if res1:
           loader.login("default_userid","password")
        else:
            loader.login(username.get(),password.get())  
        profile=instaloader.Profile.from_username(loader.context,username.get())
        followers_iterator=profile.get_followers()
        followers=set()
        for f in followers_iterator:
            followers.add(f.username)
        following=set()
        for i in profile.get_followees():
            following.add(i.username)
        cheaters=following-followers
        no=len(cheaters)
        for i in cheaters:
            body=body+i+"\n"
        loader.close()
        body=body+"No of People:"+str(no)    
        if not res2:
            send()
   
        Searching.destroy()
        Result=Toplevel(master)
        Result.title('Result')
        out=Label(Result,text=body,padx="2",pady="2",width="50")
        out.pack()

#All the widets
dumy_label=Label(master,padx="2",pady="2") #
username=Entry(master,) #
password=Entry(master,show="*",) #
is_public=Checkbutton(master,variable=res1, onvalue=False,offvalue=True,command=ask,padx="2",pady="2") #
send_mail=Checkbutton(master,variable=res2,onvalue=True,offvalue=False,command=ask2,padx="2",pady="2") #
gmail=Entry(master,width=20,) #
details=Label(master,text="Please Fill the below Details",padx="2",pady="2")  #
user=Label(master,text="Enter your Instagram username",padx="2",pady="2")     #
password_l=Label(master,text="Enter Your Instagram Password",padx="2",pady="2")  #
email=Label(master,text="Do you want the non followers list to be sent to your email ?",padx="2",pady="2")#
verif=Label(master,text="Your Account is Public ?",padx="2",pady="2")                     #
process=Button(master,text="Find",command=search,padx="2",pady="2")
notice=Label(master,fg="red",padx="2",pady="2")
mail_notice=Label(master,fg="red",padx="2",pady="2")
ask_email=Label(master,text="Enter Your Email ID",padx="2",pady="2") #


#Placement of the widgets

dumy_label.grid(column=0,row=0)

details.grid(column=0,row=1)

is_public.grid(column=2,row=2 )
verif.grid(column=0,row=2,sticky=W)

user.grid(column=0,row=4,sticky=W)
username.grid(column=2,row=4,sticky=E)

email.grid(column=0,row=6)
send_mail.grid(column=2,row=6)

process.grid(row=10,columnspan=2,sticky=E)

notice.grid(row=11,columnspan=2)
mail_notice.grid(row=12,columnspan=2)




master.mainloop()