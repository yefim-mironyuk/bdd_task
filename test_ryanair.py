import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from bdd_task.pages.main_page import MainPage
from bdd_task.pages.flights_page import FlightsPage
from .support.links import Links
from .support.converters import Converters



scenarios('features/ryanair.feature')


@pytest.fixture(scope="function")
def setup(browser):
    main_page = MainPage(browser, Links.home_page_link)
    main_page.open()
    main_page.accept_cookies()


@given("Ryanair home page is displayed", target_fixture="go_to_home_page")
def go_to_home_page(setup, browser):
    pass 


@when(parsers.cfparse(
    'Guest searches flight from {departure_location} to {destination_location} in next dates: departure - {departure_day}, return - {return_day}',
    ), converters=Converters.FLIGHTS_CONVERTERS)
def perform_flight_search(departure_location, destination_location, departure_day, return_day, browser):
    main_page = MainPage(browser, Links.home_page_link)
    main_page.enter_departure_location(departure_location)
    main_page.enter_destination_location(destination_location)
    main_page.input_depart_date(departure_day)
    main_page.input_return_date(return_day)
    main_page.press_search_button()


@then(parsers.cfparse(
    'Guest should see flights from {departure_location} to {destination_location} on {departure_day} and back on on {return_day}'), converters=Converters.FLIGHTS_CONVERTERS)
def is_page_correct(departure_location, destination_location, departure_day, return_day, browser):
    flight_page = FlightsPage(browser, Links.home_page_link)
    flight_page.should_be_correct_departure_location(departure_location)
    flight_page.should_be_correct_destination_location(destination_location)
    flight_page.should_be_correct_departure_day(departure_day)
    flight_page.should_be_correct_return_day(return_day)
