from util import mail_sender
from util import market_checker

if __name__ == '__main__':
    markets = market_checker.market_checker()
    marketsFile = open('file/market.txt', 'r+')
    addresses = list(map(lambda a: a.replace("\n", ""), marketsFile.readlines()))
    marketsToMessage = []
    for market in markets:
        if market.address not in addresses:
            print(f'New market with question: {market.question} and with address:  {market.address}')
            marketsFile.write(market.address + "\n")
            marketsToMessage.append(market.question)

    if marketsToMessage:
        result = mail_sender.send_mail(
            api_key='36537fceb7533a9ab8e5926586f29087',
            api_secret='a66e6c2a56b68f9ca184b2bdf3afffc6',
            from_mail='udvarid@hotmail.com',
            to_mail='udvari.donat@gmail.com',
            message='\n----\n'.join(marketsToMessage)
        )
