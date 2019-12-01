import time
from flaky import flaky
from web.Pages.login_page import LoginPage
from web.Pages.home_page import HomePage
from web.common.base_page import BaseClass
import pytest
from utilities.custom_logger import logger
from utilities.config_parser import YamlParser


class TestLogin:
    login_page = LoginPage()
    home_page = HomePage()

    @pytest.fixture(autouse=True)
    def setup_and_teardow(self):
        logger.info(f'*************SETUP TEST DATA**************')
        base_class = BaseClass()
        base_class.get_driver()
        base_class.open_browser()
        yield
        logger.info(f'*************TEARDOWN TEST DATA*************')
        base_class.close_driver()
        base_class.quit_driver()

    # @flaky(max_runs=3, min_passes=1)
    def test_user_login_with_valid_credentials(self):
        self.home_page.navigate_to_input_box()
        self.login_page.login(YamlParser.get_property('USERNAME'), YamlParser.get_property('PASSWORD'))
        time.sleep(5)
        home_res = self.home_page.sign_out_account()
        #self.login_page.close_driver()
        #self.login_page.quit_driver()
        # assert (home_res == True)


# if __name__ == "__main__":
#     test_login = TestLogin()
#     test_login = test_login.test_user_login_with_valid_credentials()


