import mailjet_rest


def send_mail(api_key, api_secret, from_mail, to_mail, message):
    mailjet = mailjet_rest.Client((api_key, api_secret))
    data = {
        'FromEmail': from_mail,
        'FromName': 'PolyMarket Guard',
        'Subject': 'New markets at PolyMarket!',
        'Text-part': message,
        'Recipients': [{'Email': to_mail}]
    }
    return mailjet.send.create(data)
