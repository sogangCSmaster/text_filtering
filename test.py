from config import key, api
import nltk
import requests
import sys

def fetch(keyword):
    response = requests.get(api, params={'keyword': keyword, 'token': key, 'limit': 100})
    response = response.json()

    return response


def main():
    keyword = sys.argv[0]

    datas = fetch(keyword)['datas']
    print(datas)

main()
