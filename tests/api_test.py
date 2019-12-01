from api.api_helpers.booking_helper import BookingHelper


class TestBookingAPI:
    booking_helper = BookingHelper()

    # @pytest.mark.skip
    # def test_create_new_booking(self):
    #     logger.info(f'Start the get request for api booking')
    #     self.booking_helper.create_booking()

    def test_get_new_booking(self):
        resp = self.booking_helper.get_booking(1)
        assert (resp.json()["firstname"] == "Mark")
