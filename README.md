# PyLoginTest

The purpose of this project is to automate tests for the Twitter login page in order to verify whether it allows invalid credentials, such as incorrect usernames or passwords.
 The program navigates through the website to the login form, enters specified test credentials, and uses a validation process to determine their validity, raising an exception if necessary (i.e, when either the username or password is incorrect).

The two main test cases consist of one or two subcases:
- Valid credentials
  - Valid username, valid password
- Invalid credentials
  - Invalid username
  - Valid username, invalid password

The credentials used for the tests were deleted and replaces with empty strings (which can be easily changed). The reason is that valid/invalid credentials can change overtime (a new account can be created, an existing ccount can be deleted).

# Versions
- **Python 3.11.1**
  - selenium 4.7.2
  - pytest 7.3.1
- **EdgeDriver 113.0.1774.3 x64** 
