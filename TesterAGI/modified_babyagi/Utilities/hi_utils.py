import requests
import json


class HiUtils:
    url = None
    data = None
    headers = None
    # path = "http://localhost:5000/"
    path = "http://72.189.196.202:2525/"

    def __init__(self):
        # self.set_url(self.path, "check")
        self.headers = {'Content-type': 'application/json'}

    def set_url(self, path, extension):
        self.url = path + extension

    def parse_data(self, data, extension):

        self.set_url(self.path, extension)

        response = requests.put(self.url, data=json.dumps(data), headers=self.headers)

        return response.text


