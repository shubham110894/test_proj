import requests
from utilities.custom_logger import logger


class RequestMaker(object):

    def __init__(self):
        pass

    def get(self, param=None, url=None, headers={}, json_body={}):
        logger.info(f'GET request method for API')
        return self.__make_request('GET', param, url, headers, json_body)

    def post(self, url=None, headers={}, json_body={}):
        logger.info(f'POST request method for API')
        return self.__make_request('POST', url, headers, json_body)

    def __make_request(self, method='GET', params=None, url=None, headers={}, json_body={}):
        try:
            logger.info(f'Make request session for API')
            req = requests.Request(method=method, params=params, url=url, headers=headers, data=json_body)
            pre_request = req.prepare()
            self.session = requests.Session()
            response = self.session.send(pre_request)
            return respon
        except Exception as ex:
            logger.error(f'Failed to create a request for the API with METHOD:{method}, URL={url}')
            raise ex
