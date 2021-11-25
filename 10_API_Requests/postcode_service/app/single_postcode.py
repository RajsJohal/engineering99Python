from .config_manager import base_url
import requests
from .models.single_postcode_model import SinglePostcodeModel


class SinglePostcode:
    def __init__(self, single_postcode):
        # Make a request
        # Method: return the response data, modelling as SinglePostcode Model
        self.url = base_url() + single_postcode
        self.request = requests.get(self.url)
        self.headers = self.request.headers
        self.response_json = self.request.json()

    def response_data(self):
        return SinglePostcodeModel(self.response_json)