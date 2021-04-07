# encoding:utf-8
import requests
import time
import csv
import os
import json

path = os.path.dirname(os.getcwd())
# 此处需要ak，ak申请地址：https://lbs.amap.com/dev/key/app
ak = "" #使用自己的ak，注意认证开发者，这样一天有30万次的接口访问量

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://restapi.amap.com/'
}

# fcsv = open('allcjmessage.csv', mode='w', encoding='utf-8-sig', newline='')
# csv_writer = csv.writer(fcsv)
# csv_writer.writerow(['成交价', '每平方米的价格', '小区名称', '所在区域', '更小的所在区域',
#                      '挂牌价格', '成交周期', '调价', '关注', '浏览',
#                      '房屋户型', '所在楼层', '建筑面积', '户型结构', '套内面积', '建筑类型',
#                      '房屋朝向', '建成年代', '装修情况', '建筑结构', '梯户比例', '配备电梯',
#                      '链家编号', '交易权属', '挂牌时间', '房屋用途', '房屋年限', '产权所属',
#                      '经度', '纬度'])
# fcsv.close()

path = path + '\\chengjiaomessage\\allcjmessage.csv'
f = open(path, mode='r', encoding='utf-8', newline='')
reader = csv.reader(f)
reader = list(reader)
for row in reader[32614:]:
    # print(row[0], row[1], row[2], row[3], row[4], row[5],
    #       row[6], row[7], row[8], row[9], row[10], row[11],
    #       row[12], row[13], row[14], row[15], row[16], row[17],
    #       row[18], row[19], row[20], row[21], row[22], row[23],
    #       row[24], row[25], row[26], row[27])
    address = '武汉市' + row[3] + '区' + row[2]
    # print(address)
    url = 'http://api.map.baidu.com/geocoding/v3/?address=' + address + '&output=json&ak=' + ak + '&callback=showLocation'
    # print(url)
    response = requests.get(url, headers=headers)
    data = json.loads(response.text[48:-2])
    lng = data['location']['lng']
    lat = data['location']['lat']
    # print(lng, lat)
    fcsv = open('allcjmessage.csv', mode='a+', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(fcsv)
    csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5],
                         row[6], row[7], row[8], row[9], row[10], row[11],
                         row[12], row[13], row[14], row[15], row[16], row[17],
                         row[18], row[19], row[20], row[21], row[22], row[23],
                         row[24], row[25], row[26], row[27], lng, lat])
    fcsv.close()
f.close()

