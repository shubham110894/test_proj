import time
from loguru import logger
from selenium.webdriver.common.by import By
from web.common.base_page import BaseClass
from web.common.web_element import WebElement


class LoginPage(BaseClass):

    def __init__(self):
        super(BaseClass, self).__init__()
        self.open_browser()
        self.navigate_to_sign_in = WebElement(By.ID, 'nav-link-accountList')
        self.user_name_input_box = WebElement(By.ID , "ap_email")
        self.password_input_box = WebElement(By.ID, "ap_password")
        self.next_button = WebElement(By.ID, "continue")
        self.submit_button = WebElement(By.ID, "signInSubmit")

    def navigate_to_input_box(self):
        try:
            logger.info(f'Navigating to the sign-in page')
            self.navigate_to_sign_in.click()
        except Exception as ex:
            logger.error(f'Failed to navigate to the sign-up page {0}'.format(ex))
            raise Exception(ex)

    def insert_user_name(self, username=None):
        try:
            logger.info(f'Insert the username')
            self.user_name_input_box.enter_text(self.config_d.get('USERNAME'))
        except Exception as ex:
            logger.error(f'Failed to enter the user name -{0}, {1}'.format(self.config_d.get('USERNAME'), ex))
            raise Exception(ex)

    def insert_password(self, password=None):
        try:
            logger.info(f'Insert the password')
            self.password_input_box.enter_text(self.config_d.get('PASSWORD'))
        except Exception as ex:
            logger.error(f'Failed to enter the password -{0}, {1}'.format(self.config_d.get('PASSWORD'), ex))
            raise Exception(ex)

    def click_next_button(self):
        try:
            logger.info(f'Click on the continue button')
            self.next_button.click()
        except Exception as ex:
            logger.error(f'Failed to click on continue button -{0}'.format(ex))
            raise Exception(ex)

    def submit(self):
        try:
            logger.info(f'Click on Login Button')
            self.submit_button.click()
        except Exception as ex:
            logger.error(f'Failed to click on login button -{0}'.format(ex))
            raise Exception(ex)

    def login(self, username, password):
        try:
            self.navigate_to_input_box()
            self.insert_user_name(username)
            self.click_next_button()
            self.insert_password(password)
            self.submit()
            self.close_driver()
            self.quit_driver()
            return True
        except Exception as ex:
            logger.error(f'Failed to login with the given credentials -{0}'.format(ex))
            raise Exception(ex)
