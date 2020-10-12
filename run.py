import random
from user import User


def create_user(account,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(account,username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(account):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_account_name(account)

def check_existing_user(username):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(username)

def display_users(account):
    '''
    Funtion that returns all the saved users
    '''
    return User.display_users()


def user_exist(username,password):
    '''
    Function that checks if an account really exists
    '''
    User.user_exist(username)
    return username


def main():
	print(' ')
	print('Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n Cr-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			account = input('Enter your account - ').strip()
			username = input('Enter your username - ').strip()
			password = input('Enter your password - ').strip()
			save_users(create_user(account,username,password))
			print(" ")
			print(f'New Account Created for: {account} {username} using password: {password}')
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, enter your user details:')
			account = input('Enter your account - ').strip()
			password = str(input('Enter your password - '))
			user_exists = (username,password)
			if user_exists == username:
				print(" ")
				print(f'Welcome {username}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display User Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {username}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your user details:')
						account = input('Enter the account\'s name- ').strip()
						username = input('Enter your username - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_users(create_user(account,username,password))
						print(' ')
						print(f'User Created: Account Name: {account} - Account Name: {username} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_users(username):
							print('Here is a list of all your credentials')
							print(' ')
							for user in display_users(account):
								print(f'account: {account} - username: {username} - Password: {password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any accounts yet,please create one")
							print(' ')
					
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')

if __name__ == '__main__':
	main()