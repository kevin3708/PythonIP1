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


    @classmethod
    def from_input(cls):
        return cls(
            input('Twitter username: '),
            input('Instagram username: '),
            input('Email address: '),
            input('Snapchat username: '),
        )
    def delete_user(self):
        '''
        delete_user method deletes an added username 
        '''
        User.remove(self)
user=User.from_input()

