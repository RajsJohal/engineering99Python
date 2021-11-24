import json

class RatesParser:

    def __init__(self, filepath):
        self.filepath = filepath
        exchange_info = self._open_json_exchange()
        self.rates = exchange_info.get("rates")

    def _open_json_exchange(self) -> dict:
        with open(self.filepath) as exchange_file:
            return json.load(exchange_file)

    def convert(self, currency:str, amount):
        exchange = 0
        rates = self.rates.get(currency)
        exchange = rates * amount
        return exchange



#on initialisation, read in a provided filepath
#base, rate, and then each currency rate stored as attributes
# e.g. self.gbp = <0.89275>
# method called convert
# takes in a string corresponding to currency
# takes in a value (representing EUR)
# Returns the value in other currency

gbp = RatesParser("exchange_rates.json")
print(gbp.convert("GBP", 10))