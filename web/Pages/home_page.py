import time
from loguru import logger
from selenium.webdriver.common.by import By
from web.common.base_page import BaseClass
from web.common.web_element import WebElement


class HomePage(BaseClass):

    def __init__(self):
        super(BaseClass, self).__init__()
        self.open_browser()
        self.navigate_to_sign_in = WebElement(By.ID, 'nav-link-accountList')

    def navigate_to_input_box(self):
        try:
            logger.info(f'Navigating to the sign-in page')
            self.navigate_to_sign_in.click()
        except Exception as ex:
            logger.error(f'Failed to navigate to the sign-up page {0}'.format(ex))
            raise Exception(ex)
