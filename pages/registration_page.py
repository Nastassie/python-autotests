from selenium.webdriver.common.by import By


from .base_element import BaseElement
from .base_page import BasePage

class RegistrationPage(BasePage):

    url = 'http://newtours.demoaut.com/mercuryregister.php'

    @property
    def firstName_input(self):
        locator = (By.NAME, 'firstName')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def lastName_input(self):
        locator = (By.NAME, 'lastName')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def phone_input(self):
        locator = (By.NAME, 'phone')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def email_input(self):
        locator = (By.ID, 'userName')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def address1_input(self):
        locator = (By.NAME, 'address1')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def address2_input(self):
        locator = (By.NAME, 'address2')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def city_input(self):
        locator = (By.NAME, 'city')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def state_input(self):
        locator = (By.NAME, 'state')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def postalCode_input(self):
        locator = (By.NAME, 'postalCode')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def userName_input(self):
        locator = (By.ID, 'email')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def country_selection(self):
        locator = (By.NAME, 'country')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def password_input(self):
        locator = (By.NAME, 'password')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def confirmPassword_input(self):
        locator = (By.NAME, 'confirmPassword')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def submit_button(self):
        locator = (By.NAME, 'register')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    