from email.policy import default
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from instaloader import Instaloader,Profile
from threading import Thread
#Emailing is not yet Implemented

class Follower():
    email=""
    default_user="##" #Instagram user id
    default_pass="##" #Instagrm password
    p=""
    user=""
    follower="Default"
    is_public=True
    def send(self):
        pass
    def assign(self,user,p,email):
        self.user=user
        self.email=email
        if p!="":
            self.p=p
            self.is_public=False
    def find(self):
        print("works")
        loader=Instaloader()
        try:
            if self.is_public:
                loader.login(self.user,self.p)
            else:
                loader.login(self.default_user,self.default_pass)
            profile=Profile.from_username(loader.context,self.user)
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
            self.follower=body+"No of People:"+str(no)
        except:
            self.follower="FAILED"
        print(self.follower)

class Window(AnchorLayout):
    fol=Follower()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_followers(self,button,email,user,p):
        button.disabled=True
        self.fol.assign(user.text,p.text,email)
        obj=Thread(target=self.fol.find)
        obj.start()
        if email!="":
            self.fol.send()
        print(self.fol.follower)

class FollowerApp(App):
    pass

FollowerApp().run()
