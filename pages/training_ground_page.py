from selenium.webdriver.common.by import By
from .Base_element import BaseElement
from .Base_page import BasePage

class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground'
    
    @property
    def button1(self):
        locator = (by.ID, 'b1')
        return BaseElement(
            driver = self.driver
            by = locator[0]
            value = locator[1]
            )