import urllib2
import json


def query_giphy(q):
    k = "dc6zaTOxFJmzC"
    q.strip().replace(' ', '+')
    endpoint = "http://api.giphy.com/v1/gifs/search?q=" + q \
               + "&api_key=" + k
    
    try:
        req = urllib2.Request(endpoint, headers={'User-Agent' : "Magic Browser"}) 
        response = urllib2.urlopen(req)
        data = json.load(response)
        gifs = []
        for i, v in enumerate(data['data']):
            gifs.append(v['images']['original'])
        return gifs
    except Exception as e:
        print e
        return []


def random_giphy():
    k = "dc6zaTOxFJmzC"
    endpoint = "http://api.giphy.com/v1/gifs/random?api_key=" + k
    try:
        req = urllib2.Request(endpoint, headers={'User-Agent' : "Magic Browser"}) 
        response = urllib2.urlopen(req)
        data = json.load(response)
        return data['data']
    except Exception as e:
        print e
        return {}


if __name__ == '__main__':
    query_giphy("yolo")
    random_giphy()