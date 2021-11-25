import requests
from pprint import pprint
import json

# postcode_req = requests.get(
#     "https://api.postcodes.io/postcodes/TW50HG"
# )
#
# print(postcode_req)
# if postcode_req.status_code == 200:
#     print(postcode_req.headers)
#     pprint(postcode_req.json(), sort_dicts=False)
#     print(type(postcode_req.json())) # dict, process the JSON content of the response
#     print(postcode_req.content)
#     postcode = postcode_req.json()
#
#
# Print the eastings and northings of the requsted postcode

# result = postcode.get("result")
#
# print(result.get("eastings"))
# print(result.get("northings"))

# OR

# print(postcode["result"]["eastings"])
# print(postcode["result"]["northings"])




# HTTP Request

# VERB - URL - VERSION
# Header - Key-Value Pairs (METADATA)
# Body - Text / JSON / XML (DATA)

# HTTP Response

# RESPONSE CODE (e.g. 200 / 404)
# HTTP VERSION
# HEADERS
# BODY

# postcode_headers = {"Content-Type": "application/json"}
# json_data = {"postcodes": ["PR3 0SG", "TW5 0HG", "M45 6GN"]}


# multi_req = requests.post(
#     "https://api.postcodes.io/postcodes",
#     headers = postcode_headers,
#     data = json.dumps(json_data)
# )

#pprint(multi_req.json(), sort_dicts=False)
# postcodes = multi_req.json()["result"]
# pprint(postcodes)

# print the following for each postcode in the response:
# <POSTCODE> - Latitude:00000000, Longitude:00000000
# e.g.
# PR3 0SG - Latitude: 53.856635, Longitude: -2.746251

# for n in postcodes:
#     postcode = n["result"]["postcode"]
#     latitude = n["result"]["latitude"]
#     longitude = n["result"]["longitude"]
#     print(f"{postcode} - Latitude:{latitude}, Longitude{longitude}")




# Create a postcode clas
# tat can hold lat/long and eastings and northings
# for a single postcode
# (maybe a method that is called init which takes in a postcode
# as a string and makes the API call)


class PostCode:

    def __init__(self, postcode: str):
        self.postcode = postcode
        self.search_results = None


    def postcode_search(self):
        postcode_headers = {"Content-Type": "application/json"}
        json_data = {"postcodes": [self.postcode]}
        multi_req = requests.post(
            "https://api.postcodes.io/postcodes",
            headers=postcode_headers,
            data=json.dumps(json_data)
        )
        self.search_results = multi_req.json()["result"]
        return self.search_results

    def coordinates(self):
        for n in self.search_results:
            pc = n["result"]["postcode"]
            latitude = n["result"]["latitude"]
            longitude = n["result"]["longitude"]
            print(f"{pc} - Latitude:{latitude}, Longitude{longitude}")

tw = PostCode("TW4 5EF")
tw.postcode_search()
tw.coordinates()