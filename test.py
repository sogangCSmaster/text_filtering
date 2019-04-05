from config import key, api
import nltk
import requests
import sys
import distance
import csv

def fetch(keyword):
    response = requests.get(api, params={'keyword': keyword, 'token': key, 'limit': 100})
    response = response.json()

    return response


def main():
    keyword = sys.argv[1]
    f = open(keyword + 'title_similarity.csv', 'w', encoding='euc_kr', newline='')
    wr = csv.writer(f)
    wr.writerow(["제목1", "제목2", "유사도 측정(0~1)"])
    datas = fetch(keyword)['datas']
    contentList = []
    idList = []

    for data in datas:
        contentList.append({'id': data['id'], 'content': data['content'], 'title': data['title']})

    temp = contentList
    for data in datas:
        if data['id'] not in idList:
            idList.append(data['id'])
            for t in temp:
                if t['id'] != data['id']:
                    sim = distance.jaccard(data['title'], t['title'])
                    sim = 1 - sim
                    wr.writerow([data['title'], t['title'], sim])
        
main()
