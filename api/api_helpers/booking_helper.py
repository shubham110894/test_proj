from api.common.api_base import ApiBase
from api.request_maker import RequestMaker
from utilities.custom_logger import logger


class BookingHelper(ApiBase):

    def __init__(self):
        super(ApiBase, self).__init__()
        self.end_point = "/bookings"
        self.base_url = self.API_BASE_URL + self.end_point
        self.reqeust = RequestMaker()

    def create_booking(self, booking_id=None):
        try:
            logger.info(f'Failed to create a make request for the API')
            json_body = f'{"bookingid":{booking_id},"booking":{"firstname":"SB","lastname":"N","totalprice":111,"depositpaid":true}}'
            status, response = self.reqeust.make_request(url=self.base_url, request_type="get",
                                                         headers=self.headers, json_body=json_body)
            if status != 200:
                return response
            return True
        except Exception as ex:
            logger.error(f'Failed to create a new booking')
            raise ex

    def get_booking(self, booking_id=1):
        try:
            base_url = self.base_url + "/" + booking_id
            status, response = self.reqeust.make_request(url=base_url, request_type="get", headers=self.headers)
            if status != 200:
                return response
            return True
        except Exception as ex:
            logger.error(f'Failed to get a exiting booking')
            raise ex
