import unittest
from passlock import User,Credentials
import pyperclip
class TestClass(unittest.TestCase):
    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.username,'AlbertByrone')
        self.assertEqual(self.new_user.password,'qwertykey')
        

# class UserTest(unittest.TestCase):
#     def setUp(self):
#         """
#         a method that runs before the test
#         """
#         self.new_user = User("AlbertByrone","qwertykey")
        
# def test_init(self):
    