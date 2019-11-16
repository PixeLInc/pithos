import json
import requests

from .mappings.stations import *


class Pandora:
    def __init__(self):
        self.base_url = "https://www.pandora.com/api/v1"
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Pithos-Rewrite (https://github.com/PixeLInc/Pithos)",
            # The api validates the token & cookie match, can be any value.
            "X-CsrfToken": "yayeet",
        }
        self.cookies = {"csrftoken": "yayeet"}

    def request(self, method, path, body=None, clazz=None):
        response = self.session.request(
            method,
            f"{self.base_url}{path}",
            json=body,
            headers=self.headers,
            cookies=self.cookies,
        )
        data = response.json()

        if 300 > response.status_code >= 200:
            if clazz:
                return clazz(**data)

        return data

    def get_csrf(self):
        self.request("head", None, None)

    def login(self, username, password):
        data = {
            "existingAuthToken": "null",
            "keepLoggedIn": True,
            "password": password,
            "username": username,
        }

        response = self.request("POST", "/auth/login", data)

        if response["authToken"]:
            self.headers["X-AuthToken"] = response["authToken"]

        return response

    def get_stations(self, page_size=250, start_index=0):
        data = {"pageSize": page_size, "startIndex": start_index}

        return self.request("post", "/station/getStations", data, clazz=GetStations)

    def get_station(self, station_id, is_current_station):
        data = {"stationId": station_id, "isCurrentSTation": is_current_station}

        return self.request("post", "/station/getStationDetails", data, clazz=Station)

    def create_station(self, station_code, name=None, query=None):
        data = {
            "stationCode": station_code,
            "stationName": name,
            "searchQuery": query,
            "pandoraId": None,
            "creativeId": None,
            "lineId": None,
            "createionSource": None,
        }

        return self.request("post", "/station/createStation", data)

    def shuffle(self):
        return self.request("post", "/station/shuffle", clazz=Station)

    def add_feedback(self, track_token, is_positive):
        data = {"trackToken": track_token, "isPositive": is_positive}

        return self.request("post", "/station/addFeedback", data)

    def get_feedback(self, station_id, page_size=1, start_index=0, positive=True):
        data = {
            "pageSize": page_size,
            "startIndex": start_index,
            "stationId": station_id,
            "positive": positive,
        }

        return self.request("post", "/station/getStationFeedback", data)
