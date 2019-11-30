from web.common.base_page import BaseClass
from web.common import web_context as context
from loguru import logger


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
            logger.error(f'Failed to find the locator {0}'.format(ex))
            raise Exception(ex)

    def click(self):
        try:
            self.get_locator().click()
        except Exception as ex:
            logger.error(f'Failed to click on the web element {0}'.format(ex))
            raise Exception(ex)

    def enter_text(self, text=None):
        try:
            self.get_locator().send_keys(text)
        except Exception as ex:
            logger.error(f'Failed to enter text on the web element {0}'.format(ex))
            raise Exception(ex)
