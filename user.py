class User:
    """
    Class that generates new instances of users.
    """
    user_list = []
    def __init__(self,tUsername,iUsername,email,sUsername):

        self.tUsername=tUsername
        self.iUsername=iUsername
        self.email=email
        self.sUsername=sUsername
   
    def save_user(self):
        User.user_list.append(self)
    def delete_user(self):
        User.user_list.remove(self)
    
    @classmethod
    def from_input(cls):
        return cls(
            input('Twitter username: '),
            input('Instagram username: '),
            input('Email address: '),
            input('Snapchat username: '),
        )
   
user=User.from_input()

