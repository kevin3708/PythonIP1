#!/usr/bin/env python3.8
from user import User
from credentials import Credentials
def create_user(t_username,i_username,e_address,s_username):
    new_user = User(t_username,i_username,e_address,s_username)
    return new_user
def save_users(User):
    User.save_user()
def delete_users(User):
    User.delete_user()

def create_credentials(t_password,i_password,e_password,s_password):
    new_credentials = Credentials(t_password,i_password,e_password,s_password)
    return new_credentials
def save_credential(Credentials):
    Credentials.save_credentials()
def delete_credentials(credentials):
    credentials.delete_credentials()


def main():
    print("Hello welcome to your password locker. What would you like to do?")
    print("use these short codes: cu - create a new username, du - delete a username, cc - create new credentials, dc - delete credentials, ex -  exit the password locker")
    short_code = input().lower()

    if short_code == 'cu':
        print("New Username")
        t_username = input()
        i_username = input()
        e_address = input()
        s_username = input()
        

        save_users(create_user(t_username,i_username,e_address,s_username))
        print("New Usernames created.")
  
    elif short_code == 'du':
        print("Enter the username you wish to delete")
        del_user = input()
        if delete_users(del_user):
            User.user_list.remove(User)
       
        else:
            print("That user does not exist")
      
    if short_code == 'cc':
        print("New Credentials")
        t_password = input()
        i_password = input()
        e_password = input()
        s_password = input()
        
        save_credential(create_credentials(t_password,i_password,e_password,s_password))
        print("New Passwords created.")
    elif short_code == 'dc':
        print("Enter the credentials you wish to delete")
        del_credentials = input()
        if delete_credentials(del_credentials):
            Credentials.credentials_list.remove(Credentials)
        
        else:
            print("Those credentials do not exist")
          
    
        if short_code == 'ex':
            print("Goodbye")
    
     
        else:
            print("I didn't get that, please use the short codes")
   
        
if __name__ == '__main__':
    main()