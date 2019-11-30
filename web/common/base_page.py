from selenium import webdriver
import os
import logging
import time


class BaseClass(object):

    def __init__(self):
        self.logger = logging.getLogger()
        pass

    def get_driver(self):
        try:
            driver = webdriver.Chrome("/opt/dexter/chromedriver")
            driver.maximize_window()
            driver.implicitly_wait(30)
            return driver
        except Exception as ex:
            raise ex

    def open_browser(self):
        try:
            # logging.debug('BASE_URL ====> ' + str(os.getenv("BASE_URL")))
            self.get_driver().get('https://www.amazon.in')
            time.sleep(30)
        except Exception as ex:
            raise ex

    def close_driver(self):
        if self.get_driver() is not None:
            self.get_driver().close()
        else:
            pass

    def quit_drier(self):
        if self.get_driver() is not None:
            self.get_driver().quit()
        else:
            pass
