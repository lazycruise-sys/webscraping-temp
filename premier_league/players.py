import requests, json

headers = {
    'authority': 'footballapi.pulselive.com',
    'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
    'sec-ch-ua-platform': '"Windows"',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.premierleague.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.premierleague.com/',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('pageSize', '100'),
    ('compSeasons', '418'),
    ('altIds', 'true'),
    ('page', '4'),
    ('type', 'player'),
    ('id', '-1'),
    ('compSeasonId', '418'),
)

response = requests.get('https://footballapi.pulselive.com/football/players', headers=headers, params=params)

data = json.loads(response.text)
# print(data['content'][0])

contents = data['content']

print(len(contents))

for content in contents:
    print(content['name']['first'], content['name']['last'])
    try:
        print(content['currentTeam']['name'])
        status = 'current'
    except:
        print(content['previousTeam']['name'])
        status = 'previous'
    print(content['playerId'])
    print()
    
    # conditionals for data elimination
    # collection of data [list is appropriate]
    # creation of header list
    # creation of data list
    # export header and data list to csv