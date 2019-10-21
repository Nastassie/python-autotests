from selenium.webdriver.common.by import By


from .base_element import BaseElement
from .base_page import BasePage

class SignInPage(BasePage):

    url = 'http://newtours.demoaut.com/mercurysignon.php'

    @property
    def userName_input(self):
        locator = (By.NAME, 'userName')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def password_input(self):
        locator = (By.NAME, 'password')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def submit_button(self):
        locator = (By.NAME, 'login')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
