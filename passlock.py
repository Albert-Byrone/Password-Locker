import pyperclip
import random
import string

class User:
    """
    create a class that generetes an instance of a user
    """
    user_list = []
    
    
    def __init__(self,username,password):
        """
        a method that defines the properties on the class object 
        """
        
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        test case to check if the user is added to the user list
        '''
        User.user_list.append(self)
    @classmethod   
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)    
class Credentials:
    """
    credential class to help create a new instance of credentials
    """
    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user
    
    def __init__(self,account,userName,password):
        """
        test case that check if the credentials are initialized properlyy
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_credentials(self):
        """
        test case to add new credentials 
        """    
        Credentials.credentials_list.append(self)
        
#         self.username = username
#         self.password = password
        
    
        