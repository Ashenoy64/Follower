from tkinter import *
import instaloader
master=Tk()

master.title("Following Back")
master.geometry("500x300")
    

def search():
    notice.config(text="")
    global body
    if username.get()=="":
        notice.config(text="Username must not be Empty")
        return 
    elif password=="":
        notice.config(text="Password shoudnt be Empty")
        return
    
    
    loader=instaloader.Instaloader()
        
    try:
        loader.login(username.get(),password.get())  
    except:
        notice.config(text="Login Failed")
        return
    
    notice.config(text="Login Successfull")
    
    try:
        profile=instaloader.Profile.from_username(loader.context,username.get())
    except:
        notice.config(text="Failed to get list of followers and followings")
        return
    followers_iterator=profile.get_followers()
    followers=set()

    for f in followers_iterator:
        followers.add(f.username)

    notice.config(text="Obtained List of followers")

    following=set()
    for i in profile.get_followees():
        following.add(i.username)
    notice.config(text="Obtained List of followings")

    not_following=following-followers
    number_of_not_following=len(not_following)

    for i in not_following:
        body = body + i + "\n"

    loader.close()
    notice.config(text="")

    body=body+"No of People:"+str(number_of_not_following)    


    Result=Toplevel(master)
    Result.title('Result')
    out=Label(Result,text=body,padx="2",pady="2",width="50")
    out.pack()

#All the widets
dumy_label=Label(master,padx="2",pady="2") 

details_label=Label(master,text="Please Fill the below Details",padx="2",pady="2")  

username_label=Label(master,text="Enter your Instagram username",padx="2",pady="2")     
username=Entry(master,) 

password_label=Label(master,text="Enter Your Instagram Password",padx="2",pady="2")  
password=Entry(master,show="*",) 



search=Button(master,text="Find",command=search,padx="2",pady="2")

notice=Label(master,fg="red",padx="2",pady="2")


#Placement of the widgets

dumy_label.grid(column=0,row=0)

details_label.grid(column=0,row=1)


username_label.grid(column=0,row=4,sticky=W)
username.grid(column=2,row=4,sticky=E)

password_label.grid(column=0,row=5,sticky=W)
password.grid(column=2,row=5)


search.grid(row=10,columnspan=2,sticky=E)

notice.grid(row=11,columnspan=2)


master.mainloop()
