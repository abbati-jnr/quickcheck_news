import requests

BASEURL = 'https://hacker-news.firebaseio.com/v0/'


def get_item_by_id(item_id):
    url = '{}item/{}.json'.format(BASEURL, item_id)
    payload = "{}"
    response = requests.request("GET", url, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return ''


def get_largest_item_id():
    url = "{}maxitem.json".format(BASEURL)
    payload = "{}"
    response = requests.request("GET", url, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return ''


