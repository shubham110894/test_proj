from utilities.custom_logger import logger
import yaml
import os


class YamlParser(object):
    config_path = os.path.join(os.path.dirname(__file__), f'../config/test_config.yml')

    @classmethod
    def parser_module(cls):
        try:
            with open(cls.config_path) as file:
                sort_file = yaml.load(file, Loader=yaml.FullLoader)
                print(sort_file)
                return sort_file
        except Exception as ex:
            logger.error(f'Unable to load the config yaml {0}'.format(ex))
            raise Exception(ex)

    @classmethod
    def get_property(self, property_key=None):
        config_dict = self.parser_module().get('CONFIG')
        return config_dict.get(property_key)
