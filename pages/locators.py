from selenium.webdriver.common.by import By


class MainPageLocators():
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "button.cookie-popup-with-overlay__button")
    DEPARTURE_LOCATION_SEARCH_FIELD = (By.CSS_SELECTOR, "#input-button__departure")
    PICK_DEPARTURE_AIRPORT_BUTTON = (By.CSS_SELECTOR, "fsw-airport-item > span")
    DESTINATION_LOCATION_SEARCH_FIELD = (By.CSS_SELECTOR, "#input-button__destination")
    PICK_DESTINATION_AIRPORT = (By.CSS_SELECTOR, "fsw-airport-item:nth-child(2) > span > span")
    DEPARTURE_DAY_SEARCH_FIELD = (By.CSS_SELECTOR,
                                  ".ng-star-inserted > nas-datepicker-combo > div > div:nth-child(1) > nas-datepicker > label > div > div > div.nas-datepicker__controls > input")
    RETURN_DAY_SEARCH_FIELD = (
        By.CSS_SELECTOR,
        ".ng-star-inserted > nas-datepicker > label > div > div > div.nas-datepicker__controls > input")
    TRAVELLERS_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "button.nas-dropdown__toggle.nas-dropdown__toggle--active")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div > div > button")


class FlightsPageLocators():
    DEPARTURE_DAY = (By.CSS_SELECTOR, ".ng-trigger-fadeInOut.ng-star-inserted > span:nth-child(1)")
    RETURN_DAY = (
        By.CSS_SELECTOR, ".ng-star-inserted > span.ng-tns-c55-3.ng-star-inserted")
    DEPARTURE_AIRPORT = (By.CSS_SELECTOR, ".ng-tns-c55-3 > h4:nth-child(1)")
    DESTINATION_AIRPORT = (By.CSS_SELECTOR, ".ng-tns-c55-3 > h4:nth-child(3)")