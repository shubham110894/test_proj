from selenium.webdriver import ActionChains
from web.common.base_page import BaseClass
from web.common import web_context as context
from loguru import logger
from web.common.web_context import take_screenshot, wait_for_element
from utilities.framework_constants import Constants as const


class WebElement(BaseClass):

    def __init__(self, strategy=None, value=None):
        super(BaseClass, self).__init__()
        self.strategy = strategy
        self.value = value

    def get_locator(self):
        try:
            logger.info(f'Get locator..')
            web_element = context.wait_for_element(self.strategy, self.value, const.XL)
            return web_element
        except Exception as ex:
            logger.error(f'Failed to find the locator ({self.strategy}, {self.value}), Exception : {ex}')
            take_screenshot()
            raise Exception(ex)

    def click(self):
        try:
            logger.info(f'Click web element')
            self.get_locator().click()
        except Exception as ex:
            logger.error(f'Failed to click on the web element {0}'.format(ex))
            take_screenshot()
            raise Exception(ex)

    def enter_text(self, text=None):
        try:
            logger.info(f'Enter text to web element')
            self.get_locator().send_keys(text)
        except Exception as ex:
            logger.error(f'Failed to enter text on the web element {0}'.format(ex))
            take_screenshot()
            raise Exception(ex)

    def hover_on_element(self):
        try:
            web_ac = ActionChains(context.driver)
            return web_ac.move_to_element(self.get_locator()).perform()
        except Exception as ex:
            logger.error(f'Failed to hover on the wev element{0}'.format(ex))
            take_screenshot()
            raise Exception(ex)

    def element_is_displayed(strategy=None, value=None):
        try:
            logger.info(f'Check if the element is displayed')
            return wait_for_element(strategy, value).is_displayed()
        except Exception as ex:
            logger.error(f'Failed to wait until the element is loaded {0}'.format(ex))
            take_screenshot()
            raise Exception(ex)