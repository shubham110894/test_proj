import time
from flaky import flaky
from web.Pages.login_page import LoginPage
from web.Pages.home_page import HomePage


class TestLogin(object):
    login_page = LoginPage()
    home_page = HomePage()

    @flaky(max_runs=3, min_passes=1)
    def test_user_login_with_valid_credentials(self):
        self.home_page.navigate_to_input_box()
        self.login_page.login(self.login_page.config_d.get('USERNAME'), self.login_page.config_d.get('PASSWORD'))
        time.sleep(5)
        home_res = self.home_page.sign_out_account()
        self.login_page.close_driver()
        self.login_page.quit_driver()
        # assert (home_res == True)


# if __name__ == "__main__":
#     test_login = TestLogin()
#     test_login = test_login.test_user_login_with_valid_credentials()


