#!/usr/bin/env python3.8
from user import User
from credentials import Credentials
def create_user(t_username,i_username,e_address,s_username):
    new_user = User(t_username,i_username,e_address,s_username)
    return new_user
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()

def create_credentials(t_password,i_password,e_password,s_password):
    new_credentials = Credentials(t_password,i_password,e_password,s_password)
    return new_credentials
def save_credentials(credentials):
    credentials.save_credentials()
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
        

        save_user(create_user(t_username,i_username,e_address,s_username))
        print("New Usernames created.")
        print('\n')
    elif short_code == 'du':
        print("Enter the username you wish to delete")
        del_user = input()
        if delete_user(del_user):
            User.user_list.remove(User)
            print('\n')
        else:
            print("That user does not exist")
            print('\n')
    if short_code == 'cc':
        print("New Credentials")
        t_password = input()
        i_password = input()
        e_password = input()
        s_password = input()
        
        save_credentials(create_credentials(t_password,i_password,e_password,s_password))
        print("New Passwords created.")
    elif short_code == 'dc':
        print("Enter the credentials you wish to delete")
        del_credentials = input()
        if delete_credentials(del_credentials):
            Credentials.credentials_list.remove(Credentials)
            print('\n')
        else:
            print("Those credentials do not exist")
            print('\n')
    
    elif short_code == 'ex':
        print("Goodbye")
        print('\n')
    
     
    else:
        print("I didn't get that, please use the short codes")
        print('\n')
        
if __name__ == '__main__':
    main()