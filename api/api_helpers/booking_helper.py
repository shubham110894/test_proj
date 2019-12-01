from api.common.api_base import ApiBase
from api.request_maker import RequestMaker
from utilities.custom_logger import logger


class BookingHelper(ApiBase):

    def __init__(self):
        logger.debug("========> INSIDE BOOKING_HELPER")
        super(ApiBase, self).__init__()
        self.end_point = "/bookings"
        self.base_url = self.API_BASE_URL + self.end_point
        self.request = RequestMaker()

    def get_booking(self, booking_id=None):
        try:
            logger.debug(f'=======> INSIDE get_booking method')
            base_url = f'{self.base_url}/{booking_id}'
            response = self.request.get(url=base_url, headers=self.headers)
            if response.json().status == 200:
                return response
            else:
                return {}
        except Exception as ex:
            logger.error(f'Failed to get a exiting booking')
            raise ex

    def create_booking(self, booking_id=None):
        try:
            logger.info(f'Failed to create a make request for the API')
            json_body = {"firstname" : "SB","lastname" : "N","totalprice" : 111,"depositpaid" : True,"bookingdates" : {"checkin" : "2018-01-01","checkout" : "2019-01-01"}}
            response = self.request.post(url=self.base_url, headers=self.headers,
                                         json_body=json_body)
            if response.json().status == 200:
                return response
            else:
                return {}
        except Exception as ex:
            logger.error(f'Failed to create a new booking')
            raise ex
