import pytest

from Driver import WebDriver
from exceptions import InvalidUsername, InvalidPassword

# The tests assume the given input matches the requirements
def login(username, password):
    driver = WebDriver('./EdgeDriver_win64/msedgedriver')
    driver.goTo('https://www.twitter.com')

    driver.log_in(username, password)
    driver.login_was_successful()

    driver.quit()

# VALID CREDENTIALS
def test_valid_username_and_password():
    login('','')

# INVALID CREDENTIALS
## Invalid username
def test_invalid_username():
    with pytest.raises(InvalidUsername):
        login('','')

## Valid username, invalid password
def test_valid_username_invalid_password():
    with pytest.raises(InvalidPassword):
        login('','')
