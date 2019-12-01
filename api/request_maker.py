import requests
from utilities.custom_logger import logger

class RequestMaker(object):

    def __get(self, url):
        logger.info(f'GET request method for API')
        res_obj = self.session.get(url=url)
        return res_obj.status_code, res_obj.reason

    def post(self, url, data):
        logger.info(f'POST request method for API')
        res_obj = self.session.post(url=url, data=data)
        return res_obj.status_code, res_obj.reason

    def __put(self):
        logger.info(f'PUT request method for API')
        pass

    def __patch(self):
        logger.info(f'PATCH request method for API')
        pass

    def __delete(self, url):
        logger.info(f'DELETE request method for API')
        res_obj = self.session.delete(url=url)
        return res_obj.status_code, res_obj.reason

    def make_request(self, request_type=None, url=None, headers=None, json_body=None):
        try:
            logger.info(f'Make request session for API')
            self.request = requests.Request()
            prepare = self.request.prepare()
            self.session = requests.Session()
            self.session.send(prepare)
            status, response = request_type(url, headers, json_body)
            self.session.close()
            return status, response
        except Exception as ex:
            logger.error(f'Failed to create a make request for the API')
            raise ex
