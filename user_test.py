import unittest # Importing unittest
from user import User # Importing class User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    Args:
         unittest.TestCase:TestCase that help in creating test cases
    """

    def setUp(self):
        """
        set up method to run before each test cases.
        """
        #
        self.new_user = User("Facebook","sharon wawira","wangila1998wawira") # Create user object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.account_name,"Facebook")
        self.assertEqual(self.new_user.login_username,"sharon wawira")
        self.assertEqual(self.new_user.user_password,"wangila1998wawira")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Instagram","shrn_wawira","wangila1998wawira")

        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("snapchat","sharonwera","sharon") # new user
        test_user.save_user()

        self.new_user.delete_user() # Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_account_name(self):
        '''
        test to check if we can find user by account name and display information
        '''
        self.new_user.save_user()
        test_user = User("facebook","sharon wawira","wangila1998wawira")
        test_user.save_user()
        found_user = User.find_by_account_name("facebook")
        self.assertEqual(found_user.account_name,test_user.account_name)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("facebook","sharon wawira","wangila1998wawira") # new user
        test_user.save_user()

        user_exists = User.user_exist("sharon wawira")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

if __name__=='__main__':
    unittest.main()