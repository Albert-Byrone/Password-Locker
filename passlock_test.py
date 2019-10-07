import unittest
from passlock import User,Credentials
import pyperclip
class TestClass(unittest.TestCase):
    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User("AlbertByrone","qwertykey")
        
    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.username,'AlbertByrone')
        self.assertEqual(self.new_user.password,'qwertykey')
        
    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has neen created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        '''
        Method that runs before each individual credentials test methods run.
        '''
        self.new_credentials = Credentials('Gmail','AlbertByrone','qwertykey')
        
    def test_ini_(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        
        self.assertEqual(self.new_credentials.account,'Gmail')
        self.assertEqual(self.new_credentials.userName,'AlbertByrone')
        self.assertEqual(self.new_credentials.password,'qwertykey') 
        

# class UserTest(unittest.TestCase):
#     def setUp(self):
#         """
#         a method that runs before the test
#         """
#         self.new_user = User("AlbertByrone","qwertykey")
        
# def test_init(self):
    