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
        
    def test_save_credentials(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
        
    def test_save_many_account(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("Twitter","atemba","Mfh45hfk")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
        

# class UserTest(unittest.TestCase):
#     def setUp(self):
#         """
#         a method that runs before the test
#         """
#         self.new_user = User("AlbertByrone","qwertykey")
        
# def test_init(self):
    