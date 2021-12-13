from .base_page import BasePage
from .locators import *
from bdd_task.support.browser_helper import FindElement, ElementStatements


class FlightsPage(BasePage):
    def should_be_correct_departure_location(self, departure_location):
        departure_location_on_page = FindElement.find_visible_element(FindElement(self.browser),
                                                                      *FlightsPageLocators.DEPARTURE_AIRPORT).text
        ElementStatements.is_correct(ElementStatements(self.browser), departure_location_on_page, departure_location)

    def should_be_correct_destination_location(self, destination_location):
        destination_location_on_page = FindElement.find_visible_element(FindElement(self.browser),
                                                                        *FlightsPageLocators.DESTINATION_AIRPORT).text
        ElementStatements.is_correct(ElementStatements(self.browser), destination_location_on_page,
                                     destination_location)

    def should_be_correct_departure_day(self, departure_day):
        departure_day_on_page = FindElement.find_visible_element(FindElement(self.browser),
                                                                 *FlightsPageLocators.DEPARTURE_DAY).text
        ElementStatements.is_correct(ElementStatements(self.browser), departure_day_on_page, departure_day)

    def should_be_correct_return_day(self, return_day):
        return_day_on_page = FindElement.find_visible_element(FindElement(self.browser),
                                                              *FlightsPageLocators.RETURN_DAY).text
        ElementStatements.is_correct(ElementStatements(self.browser), return_day_on_page[3:-1], return_day)
