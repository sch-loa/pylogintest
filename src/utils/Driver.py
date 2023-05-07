from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from exceptions import InvalidUsername, InvalidPassword

#Generic Web Management
class WebDriverEssentials:
    # Initializes the Edge WebDriver with the required parameters.
    def __init__(self, edgedriver):
        self.service = Service(edgedriver)
        self.options = Options()

        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument('start-maximized')
        self.options.add_argument('--incognito')

        self.driver = webdriver.Edge(service = self.service, options = self.options)
        self.wait = WebDriverWait(self.driver, 5)

    # Navigates to the given webpage link.
    def goTo(self, webpage_link):
        self.driver.get(webpage_link)
        self._waitFor('//body')

    # Closes WebDriver
    def quit(self):
        self.driver.quit()
    
    # Moves to another tab
    def _moveTo(self, window):
        self.driver.switch_to.window(self.driver.window_handles[window])

    # Returns a single element that satisfies a given XPATH
    def _get_element(self, el_xpath):
        self._waitFor(el_xpath)
        return self.driver.find_element(By.XPATH, el_xpath)
    
    # Returns a list of elements that satisfy a given XPATH
    def _get_elements(self, el_xpath):
        self._waitFor(el_xpath)
        return self.driver.find_elements(By.XPATH, el_xpath)
    
    # Waits for a given element to load in the webpage.
    # If it doesn't load within the specified 15 seconds, it raises an exception.
    def _waitFor(self, el_xpath):
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, el_xpath)))
        except TimeoutException:
            raise Exception('Loading timed out. Process was cancelled.')

class WebDriver(WebDriverEssentials):
    # Navigates to login page and starts login process with an specific user
    def log_in(self, username, password):
        self._go_to_login_form()
        self._set_username(username)
        self._set_password(password)
    
    def _go_to_login_form(self):
        login_bttn = self._get_element('//a[@href = "/login"]')
        login_bttn.click()

    def _set_username(self, username):
        username_input_xpath = '//input[@class = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]'

        username_input = self._get_element(username_input_xpath)
        username_input.send_keys(username + Keys.RETURN)

    def _set_password(self, password):
        try:
            password_input = self._get_element('//input[@type = "password"]')
        except:
            raise InvalidUsername()
        
        password_input.send_keys(password + Keys.RETURN)

    
