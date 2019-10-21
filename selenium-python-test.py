import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import json
from urllib.parse import urlparse
from urllib.parse import urlsplit


from pages.registration_page import RegistrationPage
from pages.sign_in_page import SignInPage
from pages.flightFinder_page import flightFinder1
from pages.flightFinder_page import flightFinder2
from pages.flightFinder_page import flightPurchase
from pages.flightFinder_page import flightPurchase2



class MercuryToursTest(unittest.TestCase):

    def setUp(self):
        with open("pages/data.json", "r") as read_file:
            self.data = json.load(read_file)

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
   def test_Registration(self):
      
       browser=self.driver
       registration_page = RegistrationPage(driver=browser)
       
       registration_page.go()
       registration_page.firstName_input.input_text(self.data['firstName'])
       registration_page.lastName_input.input_text(self.data['lastName'])
       registration_page.phone_input.input_text(self.data['phone'])
       registration_page.email_input.input_text(self.data['email'])
       registration_page.address1_input.input_text(self.data['address1'])
       registration_page.address2_input.input_text(self.data['address2'])
       registration_page.city_input.input_text(self.data['city'])
       registration_page.state_input.input_text(self.data['state'])
       registration_page.postalCode_input.input_text(self.data['postalCode'])
       registration_page.country_selection.select(self.data['country'])
       registration_page.userName_input.input_text(self.data['email'])
       registration_page.password_input.input_text(self.data['password'])
       registration_page.confirmPassword_input.input_text(self.data['password'])
       registration_page.submit_button.click()
      
       current_url = urlparse(browser.current_url)
       result = '{uri.scheme}://{uri.netloc}{uri.path}'.format(uri=current_url)
       
       assert result == 'http://newtours.demoaut.com/create_account_success.php', "Unexpected URL"

       sign_in_page = SignInPage(driver=browser)
       sign_in_page.go()
       sign_in_page.userName_input.input_text(self.data['email'])
       sign_in_page.password_input.input_text(self.data['password'])
       sign_in_page.submit_button.click()

       current_url = urlparse(browser.current_url)
       result = '{uri.scheme}://{uri.netloc}{uri.path}'.format(uri=current_url)
       
       assert result == 'http://newtours.demoaut.com/mercuryreservation.php', "Unexpected URL"

    def test_FlightBooking(self):
       
        browser=self.driver

        sign_in_page = SignInPage(driver=browser)
        sign_in_page.go()
        sign_in_page.userName_input.input_text(self.data['email'])
        sign_in_page.password_input.input_text(self.data['password'])
        sign_in_page.submit_button.click()

        flightFinder1_page = flightFinder1(driver=browser)
        flightFinder1_page.flightType_select(self.data['flightType']).click()
        flightFinder1_page.passengers_select.select(self.data['passengerCount'])
        flightFinder1_page.departingFrom_select.select(self.data['departureFrom'])
        flightFinder1_page.MonthOfDeparting_select.select(self.data['departureMonth'])
        flightFinder1_page.DayOfDeparting_select.select(self.data['departureDay'])
        flightFinder1_page.ArrivingIn_select.select(self.data['arrivalTo'])
        flightFinder1_page.MonthOfReturning_select.select(self.data['returningMonth'])
        flightFinder1_page.DayOfReturning_select.select(self.data['returningDay'])
        flightFinder1_page.ServiceClass_select(self.data['flightClass']).click()
        flightFinder1_page.Airline_select.select(self.data['airlines'])
        flightFinder1_page.continue_button.click()

        flightFinder2_page = flightFinder2(driver=browser)
        flightFinder2_page.depart_select(self.data['chosenDepart']).click()
        flightFinder2_page.return_select(self.data['chosenReturn']).click()
        flightFinder2_page.continue_button.click()

        flightPurchase_page = flightPurchase(driver=browser)
        flightPurchase_page.passengerFirstName_input.input_text(self.data['firstName'])
        flightPurchase_page.passengerLastName_input.input_text(self.data['lastName'])
        flightPurchase_page.meal_select.select(self.data['meal'])
        flightPurchase_page.cardType_select.select(self.data['cardType'])
        flightPurchase_page.cardNumber_input.input_text(self.data['cardNumber'])
        flightPurchase_page.YearOfExpiration_select.select(self.data['yearOfExpiration'])
        flightPurchase_page.MonthOfExpiration_select.select(self.data['monthOfExpiration'])
        flightPurchase_page.CCFirstName_input.input_text(self.data['firstName'])
        flightPurchase_page.CCLastName_input.input_text(self.data['lastName'])
        flightPurchase_page.BillingAddress_input.input_text(self.data['address1'])
        flightPurchase_page.BillingCity_input.input_text(self.data['city'])
        flightPurchase_page.BillingState_input.input_text(self.data['state'])
        flightPurchase_page.BillingCode_input.input_text(self.data['postalCode'])
        flightPurchase_page.BillingCountry_select.select(self.data['country'])
        
        assert flightPurchase_page.Destination1_info.text == self.data['departureFrom'] + " to " + self.data['arrivalTo']
        assert flightPurchase_page.Destination2_info.text == self.data['arrivalTo'] + " to " + self.data['departureFrom']
        assert flightPurchase_page.flightClass_info.text == self.data['flightClass']

        flightPurchase_page.SecurePurchase_button.click()

        current_url = urlparse(browser.current_url)
        result = '{uri.scheme}://{uri.netloc}{uri.path}'.format(uri=current_url)
        
        assert result == 'http://newtours.demoaut.com/mercurypurchase2.php', 'Unexpected url'

        flightPurchase2_page = flightPurchase2(driver=browser)
        print(flightPurchase2_page.Ticket1_info.text)

        
        



        

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

