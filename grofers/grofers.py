import requests
import json
import io
import csv

headers = {
    'authority': 'grofers.com',
    'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
    'device_id': 'd20a54a7-4d82-4be3-b54a-fde0171b6e02',
    'sec-ch-ua-mobile': '?0',
    'auth_key': 'c5349a0d0cc2cc8fbc0b1de1987c7f33b4ec3b23cbece9f2939ab62a6811957e',
    'content-type': 'application/json',
    'app_client': 'consumer_web',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
    'access_token': 'null',
    'dnt': '1',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://grofers.com/cn/grocery-staples/cid/16',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'gr_1_deviceId=d20a54a7-4d82-4be3-b54a-fde0171b6e02; city=; _gcl_au=1.1.303638561.1634757323; gr_1_locality=1849; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX187Mc9b0hdZo44no%2Bg1L5a6N95VLWpRcCQ%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19SknGAnhUo3%2FlC%2FkSs%2BpvqisdvlHaYh5g%3D; _sp_ses.bf41=*; ajs_anonymous_id=%22c6efeaa6-e054-4edd-832d-d673feb9e6a0%22; WZRK_G=c764421dcf994076b0baafafca0d4e79; gr_1_lat=28.477743; gr_1_lon=77.067818; gr_1_landmark=undefined; _sp_id.bf41=7f7d7c958243badb.1634757336.1.1634758761.1634757336.d3c5a77f-0e8e-4a3b-ae52-74de48826863; WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A2%2C%22s%22%3A1634757343%2C%22t%22%3A1634758763%7D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BpMnjsbrPk1WmA0A9H3HlpRbzXCN8OS92B1xSH0B3Yj0uQt63kkph3irIdBF812oDvTDLqfjR%2BYg%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18sX0y7X4yyLAz3jI%2FMjdjnyOC8EGrNSFk%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2BhHKFTOLYGAPvF0SDKXHuq6BJYqS0Kn0s%3D; __cfruid=b1cbeeb198c0b51f66781936328d04676a959d8f-1634758815; rl_user_id=RudderEncrypt%3AU2FsdGVkX18r%2B8bWMykbbUhNvX%2B4pH2jf4WEv%2FPxK9s%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BWbhDirwPzoO%2BVpNpPfsX5ys5OKi9TrIF2oPoB2VEe64QucZpnE7JZAYL%2FwXtW0MGiWoHfx0EyqdKtO60D%2FoR6z%2F8wfvPcyWsd%2FIcMz7jz5WpLOd0JoRd1zlFnHdkvIWEZRcui88lM8IaJo4tBTcqVlZ%2BvDmovWCH8LFS422qs74HsYVlIdfblkV0sEOiKO1HkTujVpdP0yNy0kj7%2Bj8mneEv%2FvO3V%2FDDNIRmCJodxcJTD%2FPxBeNP7b266qIA23E0eWfh6J28hEhzRS2jgX%2BRkFIh4t%2FaWQHcp2z0JHkfuIfD7ZKONkQ2N9Sn438AiSnDmXFg9JFZDGSizRkeFgLAiopKCvtzjkNg2%2FyJSUTIJ%2Fted%2FY2%2B4%2FV8jMz6uqmKAe5VPWg5H2vsbJ0T9wJYssxz2adPG4cUxO3wS8ueC0M1Np1BvtGqqOH78ki%2B8ZTgpxh4SfHag3%2FuGi3W326Sos%2BPzSVZ7YdqqgHIqSnZjHh%2B4xsA9YdNPNXXAQrv9Z%2FLgXq1yEGRpKOILL15L49XVwSNQZU4Pf4H028cdKesBVqEtXR3x6QPRRO6lNemClUP9%2F8V8VLZdMCtJcq%2BGopPzDYs%2FYerb%2FwT3In8I39z%2BSwbO8Ra%2BOAzg2g3J1t2YtdsKxQ1rng3uR1T%2BAFzCQgy28P9NQUsY%2FFtvNNuBpaIAeglu5OQsHTWia3xOLNZ%2F3%2FWcmbGueduRIlX75ZCWToAIDD%2FAtkBGOfU%2FHQaW25hn9SdxCTJIHBlUEuTSbddx8BhBOHpyoSXUwW9AoZMYg43IrUXdYcUyW9BjXdEyZy3usU3vxIuv56GXiUcRtltqlyc05cOW%2FXIVV3phQZxLBKn8spowER8CNNEMrrTjmFHdQ%2BNH5kDox61QuZ9g4%2FYLDq0lu9xFeEuMEUrRUC4PHqPZ2T89n%2FwASfwYXzGMI5%2FeBMerqHsh5ojERoLp2ypfDeP%2BV5gZHQ6qmwmTy4v77YykZbKQF%2B2iWNFHgrFYVEPh3grdm0cqDDjjdh2',
}

params = (
    ('l0_cat', '16'),
    ('start', '0'),
    ('next', '48'),
)

response = requests.get('https://grofers.com/v4/search/merchants/29867/products/', headers=headers, params=params)
# print(response.text)
data = json.loads(response.text)
# print(len(data['result']['products']))

itemcount = '307'

params1 = (
    ('l0_cat', '1487'),
    ('start', '0'),
    ('next', itemcount),
)

response1 = requests.get('https://grofers.com/v4/search/merchants/29867/products/', headers=headers, params=params1)
data1 = json.loads(response1.text)
# print(data1)

data2 = data1['result']['products']
# print(len(data2))
counter = len(data2)
with open("records.txt", "w", encoding="utf8") as f1:
    f1.write(str(data2))
    
product_list = []
    
for i in range(counter):
    data3 = data2[i]
    # print(data3)
    data4 = data3['variant_info']
    
    counter1 = len(data4)
    for j in range(counter1):
        data5 = data4[j]
        item_name = data5['line_1']
        rating = data5['rating']
        unit = data5['unit']
        mrp = data5['mrp']
        actual_price = data5['price']
        offer = data5['offer']
        sbc_offer = data5['sbc_offer']
        data_list = [item_name, rating, unit, mrp, actual_price, offer, sbc_offer]
        product_list.append(data_list)
        


with open("ouput.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(["ITEM NAME", "RATING", "QUANTITY", "MRP", "ACTUAL PRICE", "OFFER", 'SBC_OFFER'])
    
    for i in range(len(product_list)):
        # csvwriter.writerow() method takes a list of values
        csvwriter.writerow(product_list[i])

print(len(product_list))