from selenium.webdriver.common import by
from web.common.base_page import BaseClass
import logging

class WebElement(BaseClass):

    def __init__(self, strategy=None, value=None):
        super(BaseClass,self).__init__()
        self.strategy = strategy
        self.value = value

    def get_locator(self):
        try:
            element = self.get_driver().find_element(self.strategy, self.value)
            logging.debug('=====>'+ str(element))
            return element
        except Exception as ex:
            raise ex

    def click(self):
        self.get_locator().click()

    def enter_text(self, text=None):
        self.get_locator().send_keys(text)
