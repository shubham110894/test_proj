from api.common.api_base import ApiBase
from api.request_maker import RequestMaker
from requests import Request

class BookingHelper(ApiBase):

    def __init__(self):
        super(ApiBase, self).__init__()
        self.end_point = "/bookings"
        self.base_url = self.API_BASE_URL + self.end_point
        self.reqeust = RequestMaker()

    def create_booking(self, booking_id=None):
        json_body = f'{"bookingid":{booking_id},"booking":{"firstname":"SB","lastname":"N","totalprice":111,"depositpaid":true,"bookingdates":{"checkin":"2018-01-01","checkout":"2019-01-01"}}}'
        status, response = self.reqeust.make_request(url=self.base_url, request_type=,
                                                     headers=self.headers, json_body=json_body)
        if status != 200:
            return response
        return True

    def get_booking(self, booking_id=1):
        base_url = self.base_url + "/" + booking_id
        status, response = self.reqeust.make_request(url=base_url, request_type="get", headers=self.headers)
        if status != 200:
            return response
        return True
