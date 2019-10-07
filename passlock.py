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
    
    
#     def __init__(self,username,password):
#         """
#         a method that defines the properties on the class object 
#         """
        
#         self.username = username
#         self.password = password
        
    
        