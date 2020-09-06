class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = []
    def __init__(self,tPassword,iPassword,emailPassword,sPassword):

        self.tPassword=tPassword
        self.iPassword=iPassword
        self.email=emailPassword
        self.sPassword=sPassword


    @classmethod
    def from_input(cls):
        return cls(
            input('Twitter password: '),
            input('Instagram password: '),
            input('Email password: '),
            input('Snapchat password: '),
        )
credentials=Credentials.from_input()
























