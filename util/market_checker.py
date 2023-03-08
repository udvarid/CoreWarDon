import requests


class Market:
    def __init__(self, question, address):
        self.question = question
        self.address = address


def market_checker():
    api_url = "https://clob.polymarket.com/markets"
    markets = []
    response = requests.get(api_url, timeout=10, verify=False).json()
    for element in [x for x in response if x['active'] is True and x['closed'] is False]:
        markets.append(Market(element["question"], element["fpmm"]))
    return markets
