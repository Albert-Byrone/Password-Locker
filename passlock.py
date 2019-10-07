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
        
    
    
#     def __init__(self,username,password):
#         """
#         a method that defines the properties on the class object 
#         """
        
#         self.username = username
#         self.password = password
        
    
        