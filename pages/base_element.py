from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value= value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element  = None
        self.find()

    def find(self):
        element = WebDriverWait(
            self.driver, 10).until(
                EC.visibility_of_element_located(locator = self.locator))
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(
                EC.element_to_be_clickable(locator = self.locator))
        element.click()
        return None
    
    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
        
    @property
    def text(self):
        return self.web_element.text

    def select(self, value):
        return Select(self.web_element).select_by_visible_text(value)
    

        

