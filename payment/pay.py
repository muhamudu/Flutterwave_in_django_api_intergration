import math
import random
import requests


def process_payment(amount, name, phone, email):
    hed = {'Authorization': 'Bearer ' + 'add your token'}
    data = {
        "tx_ref": '' + str(math.floor(1000000 + random.random() * 9000000)),
        "amount": amount,
        "currency": "RWF",
        "redirect_url": "http://127.0.0.1:8000/process/",
        "payment_options": "mobilemoneyrwanda",
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": email,
            "phonenumber": phone,
            "name": name
        },
        "customizations": {
            "title": "BIT Support Ltd",
            "description": "We offer dedicated service in promoting your business",
            "logo": "https://bits.rw/static/website/assets/img/logo.png"
        }
    }
    url = 'https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response = response.json()
    # print('==== meee ==============', myurl(request))
    print('=============== response==============', response)
    link = response['data']['link']
    return link