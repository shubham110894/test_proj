import time

from web.Pages.login_page import LoginPage
from web.Pages.home_page import HomePage


class TestLogin():

    def __init__(self):
        self.login_page = LoginPage()
        self.home_page = HomePage()

    def test_user_login_with_valid_credentials(self):
        self.home_page.navigate_to_input_box()
        result = self.login_page.login("","")
        assert (result == True)


if __name__ == "__main__":
    test_login = TestLogin()
    test_login = test_login.test_user_login_with_valid_credentials()

