from selenium.webdriver.common.by import By


from .base_element import BaseElement
from .base_page import BasePage

class flightFinder1(BasePage):

    url = 'http://newtours.demoaut.com/mercuryreservation.php'

    
    def flightType_select(self, type):
        locator = (By.CSS_SELECTOR, "input[type='radio'][value={}]".format(type))
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def passengers_select(self):
        locator = (By.NAME, 'passCount')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def departingFrom_select(self):
        locator = (By.NAME, 'fromPort')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def MonthOfDeparting_select(self):
        locator = (By.NAME, 'fromMonth')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def DayOfDeparting_select(self):
        locator = (By.NAME, 'fromDay')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def ArrivingIn_select(self):
        locator = (By.NAME, 'toPort')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def MonthOfReturning_select(self):
        locator = (By.NAME, 'toMonth')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def DayOfReturning_select(self):
        locator = (By.NAME, 'toDay')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

   
    def ServiceClass_select(self, type):
        locator = (By.CSS_SELECTOR, "input[type='radio'][value={}]".format(type))
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def Airline_select(self):
        locator = (By.NAME, 'airline')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def continue_button(self):
        locator = (By.NAME, 'findFlights')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

class flightFinder2(BasePage):

    url = 'http://newtours.demoaut.com/mercuryreservation2.php'

    
    def depart_select(self, type):
        locator = (By.CSS_SELECTOR, "input[type='radio'][value=\"{}\"]".format(type))
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    
    def return_select(self, type):
        locator = (By.CSS_SELECTOR, "input[type='radio'][value=\"{}\"]".format(type))
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def continue_button(self):
        locator = (By.NAME, 'reserveFlights')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

class flightPurchase(BasePage):

    url = 'http://newtours.demoaut.com/mercurypurchase.php'

    @property
    def passengerFirstName_input(self):
        locator = (By.NAME, 'passFirst0')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def passengerLastName_input(self):
        locator = (By.NAME, 'passLast0')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def meal_select(self):
        locator = (By.NAME, 'pass.0.meal')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def cardType_select(self):
        locator = (By.NAME, 'creditCard')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def cardNumber_input(self):
        locator = (By.NAME, 'creditnumber')
        return BaseElement(self.driver, by = locator[0], value = locator[1]) 

    @property
    def YearOfExpiration_select(self):
        locator = (By.NAME, 'cc_exp_dt_yr')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def MonthOfExpiration_select(self):
        locator = (By.NAME, 'cc_exp_dt_mn')
        return BaseElement(self.driver, by = locator[0], value = locator[1])  

    @property
    def CCFirstName_input(self):
        locator = (By.NAME, 'cc_frst_name')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def CCMidleName_input(self):
        locator = (By.NAME, 'cc_mid_name')
        return BaseElement(self.driver, by = locator[0], value = locator[1])  
    
    @property
    def CCLastName_input(self):
        locator = (By.NAME, 'cc_last_name')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def BillingAddress_input(self):
        locator = (By.NAME, 'billAddress1')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def BillingCity_input(self):
        locator = (By.NAME, 'billCity')
        return BaseElement(self.driver, by = locator[0], value = locator[1])  

    @property
    def BillingState_input(self):
        locator = (By.NAME, 'billState')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def BillingCode_input(self):
        locator = (By.NAME, 'billZip')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def BillingCountry_select(self):
        locator = (By.NAME, 'billCountry')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def DeliveryAddress_input(self):
        locator = (By.NAME, 'delAddress1')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def DeliveryCity_input(self):
        locator = (By.NAME, 'delCity')
        return BaseElement(self.driver, by = locator[0], value = locator[1])  

    @property
    def DeliveryState_input(self):
        locator = (By.NAME, 'delState')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def DeliveryCode_input(self):
        locator = (By.NAME, 'delZip')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def DeliveryCountry_select(self):
        locator = (By.NAME, 'delCountry')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def SecurePurchase_button(self):
        locator = (By.NAME, 'buyFlights')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    
    @property
    def Destination1_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[1]/td[1]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def Flight1Date_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[1]/td[2]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def airline1_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[3]/td[1]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def airline2_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[6]/td[1]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def flightClass_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[3]/td[2]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def Flight2Date_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[4]/td[2]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def Destination2_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Summary")]/../../../../../../following-sibling::tr[1]/td/table/tbody[1]/tr[4]/td[1]')
        return BaseElement(self.driver, by = locator[0], value = locator[1])


class flightPurchase2(BasePage):

    url = 'http://newtours.demoaut.com/mercurypurchase2.php'
       
    
    @property
    def Ticket1_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Departing")]/../../../following-sibling::tr[1]/td/font')
        return BaseElement(self.driver, by = locator[0], value = locator[1])

    @property
    def Ticket2_info(self):
        locator = (By.XPATH, '//font[contains(text(), "Returning")]/../../../following-sibling::tr[1]/td/font')
        return BaseElement(self.driver, by = locator[0], value = locator[1])
    
    @property
    def passengerCount_info(self):
        locator = (By.XPATH, '//b[contains(text(), "Passengers")]/../../../following-sibling::tr[1]/td/font')
        return BaseElement(self.driver, by = locator[0], value = locator[1])



