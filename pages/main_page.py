import time
from selenium.webdriver import Keys
from .locators import *
from bdd_task.support.browser_helper import FindElement, ElementStatements
from bdd_task.support.date_picker_helper import DatePickerLocators


class MainPage(FindElement, ElementStatements):
    def accept_cookies(self):
        accept_cookies_button = self.find_clickable_element(*MainPageLocators.ACCEPT_COOKIES_BUTTON)
        accept_cookies_button.click()

    def enter_departure_location(self, departure_location):
        departure_location_field = self.find_clickable_element(*MainPageLocators.DEPARTURE_LOCATION_SEARCH_FIELD)
        departure_location_field.click()
        departure_location_field.clear()
        departure_location = departure_location[1:-1]
        departure_location_field.send_keys(departure_location)
        pick_departure_airport = self.find_clickable_element(*MainPageLocators.PICK_DEPARTURE_AIRPORT_BUTTON)
        pick_departure_airport.click()

    def enter_destination_location(self, destination_location):
        destination_location_field = self.find_clickable_element(*MainPageLocators.DESTINATION_LOCATION_SEARCH_FIELD)
        destination_location = destination_location[1:-1]
        destination_location_field.send_keys(destination_location + Keys.RETURN)
        pick_destination_airport = self.find_clickable_element(*MainPageLocators.PICK_DESTINATION_AIRPORT)
        pick_destination_airport.click()

    def input_depart_date(self, departure_day):
        departure_day = departure_day[1:-1]
        depart_month = self.find_clickable_element(*DatePickerLocators.get_month_button(departure_day))
        depart_month.click()
        depart_day = self.find_clickable_element(*DatePickerLocators.get_day_button(departure_day))
        depart_day.click()

    def input_return_date(self, return_day):
        return_day = return_day[1:-1]
        return_form = self.find_visible_element(*DatePickerLocators.RETURN_FORM)
        return_form.click()
        return_month = self.find_visible_element(*DatePickerLocators.get_month_button(return_day))
        return_month.click()
        return_day = self.find_visible_element(*DatePickerLocators.get_day_button(return_day))
        return_day.click()

    def press_search_button(self):
        search_and_book_button = self.find_clickable_element(*MainPageLocators.SEARCH_BUTTON)
        search_and_book_button.click()


    # def go_to_settings_page(self):
    #     settings_button = self.find_clickable_element(*MainPageLocators.SETTINGS_BUTTON)
    #     settings_button.click()
    #
    # def is_repository_created(self):
    #     self.find_visible_element(*MainPageLocators.QUICK_SETUP_MESSAGE)
    #     assert self.is_element_present(*MainPageLocators.QUICK_SETUP_MESSAGE), "Repository is not created!"
    #
    # def is_repository_renamed(self):
    #     name = self.find_visible_element(*MainPageLocators.REPOSITORY_NAME).text
    #     assert self.new_name == name, "Repository was not renamed!"
    #
    # def add_readme_file(self):
    #     add_readme_button = self.find_clickable_element(*MainPageLocators.ADD_README_BUTTON)
    #     add_readme_button.click()
    #     text_field = self.find_visible_element(*MainPageLocators.README_TEXT_FIELD)
    #     text_field.click()
    #     text_field.send_keys("\n THIS FILE WAS CREATED BY COMPUTER")
    #     time.sleep(3)
    #     submit_button = self.find_clickable_element(*MainPageLocators.SUBMIT_NEW_README_FILE)
    #     submit_button.click()
    #
    # def is_readme_file_added(self):
    #     assert self.is_element_present(*MainPageLocators.README_WINDOW), "ReadMe file was not created!"
    #
    # def is_repository_deleted(self):
    #     assert self.random_name not in self.find_visible_element(
    #         *MainPageLocators.REPOSITORIES).text, "Repository was not deleted!"
