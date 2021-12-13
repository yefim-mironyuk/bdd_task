from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import *
from bdd_task.support.browser_helper import FindElement
from bdd_task.support.date_picker_helper import DatePickerLocators


class MainPage(BasePage):

    def accept_cookies(self):
        accept_cookies_button = FindElement.find_clickable_element(FindElement(self.browser),
                                                                   *MainPageLocators.ACCEPT_COOKIES_BUTTON)
        accept_cookies_button.click()

    def enter_departure_location(self, departure_location):
        departure_location_field = FindElement.find_clickable_element(FindElement(self.browser),
                                                                      *MainPageLocators.DEPARTURE_LOCATION_SEARCH_FIELD)
        departure_location_field.click()
        departure_location_field.clear()
        departure_location = departure_location[1:-1]
        departure_location_field.send_keys(departure_location)
        pick_departure_airport = FindElement.find_clickable_element(FindElement(self.browser),
                                                                    *MainPageLocators.PICK_DEPARTURE_AIRPORT_BUTTON)
        pick_departure_airport.click()

    def enter_destination_location(self, destination_location):
        destination_location_field = FindElement.find_clickable_element(FindElement(self.browser),
                                                                        *MainPageLocators.DESTINATION_LOCATION_SEARCH_FIELD)
        destination_location = destination_location[1:-1]
        destination_location_field.send_keys(destination_location + Keys.RETURN)
        pick_destination_airport = FindElement.find_clickable_element(FindElement(self.browser),
                                                                      *MainPageLocators.PICK_DESTINATION_AIRPORT)
        pick_destination_airport.click()

    def input_depart_date(self, departure_day):
        departure_day = departure_day[1:-1]
        depart_month = FindElement.find_clickable_element(FindElement(self.browser),
                                                          *DatePickerLocators.get_month_button(departure_day))
        depart_month.click()
        depart_day = FindElement.find_clickable_element(FindElement(self.browser),
                                                        *DatePickerLocators.get_day_button(departure_day))
        depart_day.click()

    def input_return_date(self, return_day):
        return_day = return_day[1:-1]
        return_form = FindElement.find_visible_element(FindElement(self.browser), *DatePickerLocators.RETURN_FORM)
        return_form.click()
        return_month = FindElement.find_visible_element(FindElement(self.browser),
                                                        *DatePickerLocators.get_month_button(return_day))
        return_month.click()
        return_day = FindElement.find_visible_element(FindElement(self.browser),
                                                      *DatePickerLocators.get_day_button(return_day))
        return_day.click()

    def press_search_button(self):
        search_and_book_button = FindElement.find_clickable_element(FindElement(self.browser),
                                                                    *MainPageLocators.SEARCH_BUTTON)
        search_and_book_button.click()
