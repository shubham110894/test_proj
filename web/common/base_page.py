from selenium import webdriver
import os
import logging
import time


class BaseClass(object):

    driver = None

    def __init__(self):
        pass

    def get_driver(self):
        try:
            if self.driver is not None:
                return self.driver
            else:
                self.driver = webdriver.Chrome("/Users/rohanpandhare/dev/Ridecell_qa_automation/resources/chromedriver")
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)
                return self.driver
        except Exception as ex:
            raise ex

    def open_browser(self):
        try:
            # logging.debug('BASE_URL ====> ' + str(os.getenv("BASE_URL")))
            self.get_driver().get('https://www.amazon.in')
            time.sleep(15)
        except Exception as ex:
            raise ex

    def close_driver(self):
        if self.get_driver() is not None:
            self.get_driver().close()
        else:
            pass

    def quit_driver(self):
        if self.get_driver() is not None:
            self.get_driver().quit()
        else:
            pass
