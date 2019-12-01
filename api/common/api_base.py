from utilities.config_parser import YamlParser


class ApiBase(object):

    def __init__(self):
        self.API_BASE_URL = YamlParser.get_property("API_BASE_URL")
        self.headers = {
            "Content-Type":"application/json"
        }
