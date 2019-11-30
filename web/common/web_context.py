from utilities.custom_logger import logger
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

now = datetime.now()
current_time = now.strftime("%H_%M_%S")

driver = None

def take_screenshot():
    try:
        logger.info(f'Taking screen shot of failure case')
        driver.save_screenshot(os.path.join(os.path.dirname(__file__), f'../reports/screenshots/failed-{current_time}.png'))
    except Exception as ex:
        logger.error(f'Failed to enter text on the web element {0}'.format(ex))
        raise Exception(ex)


def wait_for_element(strategy=None, value=None):
    try:
        logger.info(f'Wait for element until timeout')
        return WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((strategy, value)))
    except Exception as ex:
        logger.error(f'Failed to wait until the element is loaded {0}'.format(ex))
        raise Exception(ex)


def element_is_displayed(strategy=None, value=None):
    try:
        logger.info(f'Check if the element is displayed')
        return wait_for_element(strategy, value).is_displayed()
    except Exception as ex:
        logger.error(f'Failed to wait until the element is loaded {0}'.format(ex))
        raise Exception(ex)