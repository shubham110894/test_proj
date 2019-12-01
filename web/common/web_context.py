from utilities.custom_logger import logger
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.framework_constants import Constants as const

now = datetime.now()
current_time = now.strftime("%H_%M_%S")
driver = None


def take_screenshot(filename="Failed"):
    try:
        logger.info(f'Taking screen shot of failure case')
        driver.save_screenshot(os.path.join(os.path.dirname(__file__), f'../../reports/screenshots/{filename}-{current_time}.png'))
    except Exception as ex:
        logger.error(f'Failed to enter text on the web element {0}'.format(ex))
        raise Exception(ex)


def wait_for_element(strategy=None, value=None, timeout=const.XL):
    try:
        logger.info(f'Wait for element until timeout')
        return WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((strategy, value)))
    except Exception as ex:
        logger.error(f'Failed to wait until the element is loaded {0}'.format(ex))
        take_screenshot()
        raise Exception(ex)


def element_is_displayed(strategy=None, value=None):
    try:
        logger.info(f'Check if the element is displayed')
        return wait_for_element(strategy, value).is_displayed()
    except Exception as ex:
        logger.error(f'Failed to wait until the element is loaded {0}'.format(ex))
        take_screenshot()
        raise Exception(ex)
