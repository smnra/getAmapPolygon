# -*- coding:UTF-8 -*-
import requests
import json

if __name__ == '__main__':
    url = 'http://restapi.amap.com/v3/place/polygon'
    headers = {'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    }
    s = requests.Session()
    pm = {'polygon': '108.640287,26.043184;110.579374,27.275355',
          'key' : 'dc44a8ec8db3f9ac82344f9aa536e678',
          'extensions' : 'all',
          'offset' : 7,
          'page' : 1
          }
    r = s.request('GET',url = url, params = pm, headers = headers)
    pois = json.loads(r.text)

    for poi in pois['pois']:
        print(poi['name'],poi['id'],poi['location'],poi['type'])
        region = s.request('GET', url='http://ditu.amap.com/detail/get/detail', params={'id':poi['id']}, headers=headers)
        region_poss = json.loads(region.text)
        print(region_poss['data']['spec']['mining_shape']['shape'])

