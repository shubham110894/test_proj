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
        self.navigate_to_sign_in.click()

    def insert_user_name(self, username = None):
        self.user_name_input_box.enter_text('8884668455')

    def insert_password(self, password = None):
        self.password_input_box.enter_text('Shubham110894')

    def click_next_button(self):
        self.next_button.click()

    def submit(self):
        self.submit_button.click()

    def login(self, username, password):
        self.navigate_to_input_box()
        self.insert_user_name(username)
        self.click_next_button()
        self.insert_password(password)
        self.submit()
        self.close_driver()
        self.quit_driver()
        return True
