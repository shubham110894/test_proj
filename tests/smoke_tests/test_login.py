import time

from web.Pages.login_page import LoginPage


class TestLogin():

    def __init__(self):
        self.login_page = LoginPage()

    def test_user_login_with_valid_credentials(self):
        result = self.login_page.login("","")
        assert (result==True)


if __name__ == "__main__":
    test_login = TestLogin()
    test_login = test_login.test_user_login_with_valid_credentials()
