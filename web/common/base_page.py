from selenium import webdriver
from web.common import web_context as context


class BaseClass(object):

    def get_driver(self):
        print('**************** DRIVER SETUP ****************')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        context.driver = webdriver.Chrome(executable_path="/Users/rohanpandhare/dev/Ridecell_qa_automation/resources/chromedriver", options=options)
        print('**************** COMPLETED DRIVER SETUP ****************')
        return context.driver

    def open_browser(self):
        try:
            self.get_driver()
            print('**************** OPEN BROWSER ****************')
            context.driver.get('https://www.amazon.in')
        except Exception as ex:
            raise ex

    def close_driver(self):
        if context.driver is not None:
            print('**************** CLOSING DRIVER ****************')
            context.driver.close()

    def quit_driver(self):
        if context.driver is not None:
            print('**************** QUITING SESSION ****************')
            context.driver.quit()
