from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from instaloader import Instaloader,Profile
from threading import Thread

class Follower():
    
    password=""
    username=""
    follower="Default"
    
    def assign(self,user,password):
        self.user=user
        self.password=password

    def find(self):
        loader=Instaloader()
        try:
            loader.login(self.username,self.password)
            profile=Profile.from_username(loader.context,self.username)

            followers_iterator=profile.get_followers()
            followers=set()
            for f in followers_iterator:
                followers.add(f.username)

            followees_iterator = profile.get_followees()
            following=set()
            for i in followees_iterator:
                following.add(i.username)

            not_following=following-followers
            number=len(not_following)
            for i in not_following:
                body=body+i+"\n"
            loader.close()
            self.follower=body+"No of People:"+str(number)
        except:
            self.follower="FAILED"

class Window(AnchorLayout):
    followerObject=Follower()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_followers(self,button,user,password):
        button.disabled=True
        self.followerObject.assign(user.text,password.text)
        obj=Thread(target=self.followerObject.find)
        obj.start()
        obj.join()
        print(self.followerObject.follower)

class FollowerApp(App):
    pass

FollowerApp().run()
