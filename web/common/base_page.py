from selenium import webdriver
from web.common import web_context as context
from utilities.custom_logger import logger
from utilities.config_parser import YamlParser


class BaseClass(object):

    def get_driver(self):
        logger.info(f'**************** DRIVER SETUP ****************')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        context.driver = webdriver.Chrome(executable_path=YamlParser.get_property('CHROMEDRIVER'), options=options)
        context.driver.maximize_window()
        context.driver.implicitly_wait(15)
        logger.info('**************** COMPLETED DRIVER SETUP ****************')
        return context.driver

    def open_browser(self):
        try:
            logger.info('**************** OPEN BROWSER ****************')
            context.driver.get(YamlParser.get_property('BASE_URL'))
            logger.info(f'Navigating to {0} Website'.format(YamlParser.get_property('BASE_URL')))
        except Exception as ex:
            logger.error(f'Failed to open browser & navigate to the URL {0}'.format(ex))
            raise Exception(ex)

    def close_driver(self):
        try:
            if context.driver is not None:
                logger.info('**************** CLOSING DRIVER ****************')
                context.driver.close()
        except Exception as ex:
            logger.error(f'Failed to close the browser {0}'.format(ex))
            raise Exception(ex)

    def quit_driver(self):
        try:
            if context.driver is not None:
                logger.info('**************** QUITING SESSION ****************')
                context.driver.quit()
        except Exception as ex:
            logger.error(f'Failed to quit the browesr {0}'.format(ex))
            raise Exception(ex)
