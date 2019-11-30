from web.Pages.login_page import LoginPage
import os


class TestLogin(object):

    def __init__(self):
        self.user_name = os.getenv("USER_NAME")
        self.password = os.getenv("PASSWORD")
        self.login_page = LoginPage()

    def test_user_login_with_valid_credentials(self):
        result = self.login_page.login(self.user_name, self.password)
        assert (result == True)


if __name__ == "__main__":
    test_login = TestLogin()
    test_login = test_login.test_user_login_with_valid_credentials()
