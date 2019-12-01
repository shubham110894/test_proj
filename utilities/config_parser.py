from utilities.custom_logger import logger
import yaml
import os


class YamlParser(object):
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), f'../config/test_config.yml')

    def parser_module(self):
        try:
            with open(self.config_path) as file:
                sort_file = yaml.load(file, Loader=yaml.FullLoader)
                logger.warning(f"Reading the config file -- " + yaml.dump(sort_file))
                return sort_file
        except Exception as ex:
            logger.error(f'Unable to load the config yaml {0}'.format(ex))
            raise Exception(ex)
