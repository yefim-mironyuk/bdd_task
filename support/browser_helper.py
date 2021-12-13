from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FindElement:
    def __init__(self, browser):
        self.browser = browser

    def find_visible_element(self, how, what):
        logger.debug(f'Trying to find visible element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            logger.error(f'Cannot find visible element "{how}", "{what}"!')
        logger.debug(f'Element "{how}", "{what}" was found...')
        return element

    def find_clickable_element(self, how, what):
        logger.debug(f'Trying to find clickable element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            logger.error(f'Cannot find element "{how}", "{what}" or element is not clickable!')
        logger.debug(f'Clickable element "{how}", "{what}" was found...')
        return element


class ElementStatements:
    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, how, what):
        logger.info(f'Trying to find element "{how}", "{what}"...')
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logger.error(f'Cannot find element "{how}", "{what}"!')
        logger.info(f'Element "{how}", "{what}" was found...')
        return True

    def is_correct(self, object1, object2):
        logger.info(f'Trying to figure out is "{object1}" matches "{object2}"...')
        try:
            assert object1 in object2
        except AssertionError:
            logger.error(f'"{object1}" is not in "{object2}"...')
            raise
        logger.info(f'"{object1}" is in "{object2}"...')
