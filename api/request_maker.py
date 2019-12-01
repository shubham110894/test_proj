import requests


class RequestMaker(object):

    def __get(self, url):
        res_obj = self.session.get(url=url)
        return res_obj.status_code, res_obj.reason

    def post(self, url, data):
        res_obj = self.session.post(url=url, data=data)
        return res_obj.status_code, res_obj.reason

    def __put(self):
        pass

    def __patch(self):
        pass

    def __delete(self, url):
        res_obj = self.session.delete(url=url)
        return res_obj.status_code, res_obj.reason

    def make_request(self, request_type=None, url=None, headers=None, json_body=None):
        self.session = requests.Session()
        self.session.send()
        status, response = request_type(url, headers, json_body)
        self.session.close()
        return status, response
