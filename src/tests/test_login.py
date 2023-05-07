import pytest

from utils.Driver import WebDriver
from utils.exceptions import InvalidUsername, InvalidPassword

# The tests assume the given input matches the requirements (both username and password exist)
def login():
    username = input('username: ')
    password = input('password: ')

    driver = WebDriver('./EdgeDriver_win64/msedgedriver')
    driver.goTo('https://www.twitter.com')
    driver.log_in(username, password)
    driver.quit()

# VALID CREDENTIALS
def test_valid_username_and_password():
    login()

# Invalid credentials

## INVALID CREDENTIALS
def test_invalid_username():
    with pytest.raises(InvalidUsername):
        login()

## Valid username, invalid password
def test_valid_username_invalid_password():
    with pytest.raises(InvalidPassword):
        login()
