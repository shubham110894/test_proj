from api.common.api_base import ApiBase
from api.request_maker import RequestMaker


class BookingHelper(ApiBase):

    def __init__(self):
        super(ApiBase, self).__init__()
        self.end_point = "/bookings"
        self.base_url = self.API_BASE_URL + self.end_point
        self.reqeust = RequestMaker()

    def create_booking(self, booking_id=None):
        json_body = '{"bookingid":14,"booking":{"firstname":"SB","lastname":"N","totalprice":111,"depositpaid":true,"bookingdates":{"checkin":"2018-01-01","checkout":"2019-01-01"}}}'
        self.reqeust.make_request()