from web.common.base_page import BaseClass
from web.common import web_context as context

class WebElement(BaseClass):

    def __init__(self, strategy=None, value=None):
        super(BaseClass,self).__init__()
        self.strategy = strategy
        self.value = value

    def get_locator(self):
        try:
            web_element = context.driver.find_element(self.strategy, self.value)
            return web_element
        except Exception as ex:
            raise ex

    def click(self):
        self.get_locator().click()

    def enter_text(self, text=None):
        self.get_locator().send_keys(text)
