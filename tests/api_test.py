import requests
import pytest


def request_get():
    a = requests.get("https://restful-booker.herokuapp.com/booking/2/")
    print(a.text)
    print(a.status_code)


def request_post():
    headers = {'Content-Type': 'application/json'}
    auth = requests.post(url="https://restful-booker.herokuapp.com/auth", data={"username": "admin","password": "password123"}, json=headers)
    print(auth.text)
    print(auth.status_code)
    payload = {"firstname" : "SB","lastname" : "N","totalprice" : 111,"depositpaid" : True,"bookingdates" : {"checkin" : "2018-01-01","checkout" : "2019-01-01"}}
    a = requests.post(url="https://restful-booker.herokuapp.com/booking", data=payload, json=headers)
    print(a.text)
    print(a.status_code)
    print(a.raise_for_status())


if __name__ == "__main__":
    request_post()