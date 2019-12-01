import pytest
from utilities.custom_logger import logger
from api.api_helpers.booking_helper import BookingHelper


class TestBookingAPI(object):
    booking_helper = BookingHelper()

    def test_booking(self):
        logger.info(f'Start the get request for api booking')
        self.booking_helper.create_booking()
