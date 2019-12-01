import time
from loguru import logger
from selenium.webdriver.common.by import By
from web.common.base_page import BaseClass
from web.common.web_element import WebElement


class HomePage(BaseClass):

    def __init__(self):
        super(BaseClass, self).__init__()
        self.navigate_to_sign_in = WebElement(By.ID, 'nav-link-accountList')
        self.hover_elem = WebElement(By.ID, 'nav-al-your-account')

    def navigate_to_input_box(self):
        try:
            logger.info(f'Navigating to the sign-in page')
            self.navigate_to_sign_in.click()
        except Exception as ex:
            logger.error(f'Failed to navigate to the sign-up account {0}'.format(ex))
            raise Exception(ex)

    def sign_out_account(self):
        try:
            self.navigate_to_sign_in.hover_on_element()
            sign_out = WebElement(By.ID, 'nav-item-signout')
            sign_out.click()
        except Exception as ex:
            logger.error(f'Failed to navigate to the sign-out account {0}'.format(ex))
            raise Exception(ex)
