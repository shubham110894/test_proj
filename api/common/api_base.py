from utilities.config_parser import YamlParser
from utilities.custom_logger import logger


class ApiBase(object):

    def __init__(self):
        logger.debug(f'======> Inside API_BASE')
        self.API_BASE_URL = YamlParser.get_property("API_BASE_URL")
        self.headers = {"Content-Type": "application/json"}
