import urllib2
import json


def query_giphy(q):
    k = "dc6zaTOxFJmzC"
    q = q.strip().replace(' ', '+')
    endpoint = "http://api.giphy.com/v1/gifs/search?q=" + q \
               + "&api_key=" + k
    try:
        req = urllib2.Request(endpoint, headers={'User-Agent' : "Magic Browser"}) 
        response = urllib2.urlopen(req)
        data = json.load(response)
        gifs = []
        for i, v in enumerate(data['data']):
            gifs.append(v['images']['original'])
        return gifs[:15]
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
        return data['data']['image_url']
    except Exception as e:
        print e
        return {}


if __name__ == '__main__':
    print query_giphy("yolo")
    pass