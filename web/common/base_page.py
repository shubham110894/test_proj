from selenium import webdriver
from web.common import web_context as context
from utilities.custom_logger import logger
from utilities.config_parser import YamlParser


class BaseClass(object):

    def get_driver(self):
        logger.info(f'**************** DRIVER SETUP ****************')
        YamlParser_o = YamlParser()
        self.config_d = YamlParser_o.parser_module()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        context.driver = webdriver.Chrome(executable_path=self.config_d.get('CHROMEDRIVER'), options=options)
        context.driver.maximize_window()
        logger.info('**************** COMPLETED DRIVER SETUP ****************')
        return context.driver

    def open_browser(self):
        try:
            self.get_driver()
            logger.info('**************** OPEN BROWSER ****************')
            context.driver.get(self.config_d.get('BASE_URL'))
            logger.info(f'Navigating to {0} Website'.format(self.config_d.get('BASE_URL')))
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
