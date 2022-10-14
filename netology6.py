import requests
from pprint import pprint


def get_json(url):
    param = {
        'fromdate': '1665446400', 'todate': '1665619200',
        'site': 'stackoverflow', 'tagged': 'python',
        'filter': 'default', 'sort': 'creation'
    }
    response = requests.get(url, params=param)
    return response.json()

def take_title_list(json):
    title_list = [item['title'] for item in json['items']]
    return title_list


if __name__ == '__main__':
    path = 'https://api.stackexchange.com/2.3/questions'
    json = get_json(path)
    pprint(take_title_list(json))
