# -*- coding:UTF-8 -*-
import requests
import json

pageNumber = 1

url = 'http://restapi.amap.com/v3/place/polygon'
headers = {'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           }
pm = {'polygon': '107.124295,34.38007;107.15322,34.344148',
      'key': 'dc44a8ec8db3f9ac82344f9aa536e678',
      'extensions': 'base',       #返回结果控制 可选 为 "all"  或者 "base"
      'offset': 10,          #分页大小,高德地图分最大每页50个 强烈建议不超过25，若超过25可能造成访问报错
      'page': pageNumber            #第几页 	最大翻页数100
      }


'''
此段用于计算 maxPage  最大页数
'''
poiRequest = requests.get(url, params=pm)  # 发送get 请求
poiJsons = json.loads(poiRequest.text)  # 用json 格式化服务器返回的text字符串
maxPage = int(poiJsons['count']) // 10 - 1  # 重json的 'count" 字段取得 经纬度范围内的POI的数量 然后除以分页大小 减去1 就是循环的最大页数
'''
此段用于计算 maxPage  最大页数
'''



pois = []
for i in range(1,maxPage) :                     #循环 从第一页开始到最后一页
    poiRequest = requests.get(url, params=pm,)    # 发送get 请求
    poiJsons = json.loads(poiRequest.text)          #用json 格式化服务器返回的text字符串
    pageNumber = i + 1                              # 当前页数加1
    pois.extend(list(poiJsons['pois']))                   #把poi 列表 添加到 pois 列表中保存
    for poi in poiJsons['pois']:
        print(str(poi['name']), str(poi['id']))

