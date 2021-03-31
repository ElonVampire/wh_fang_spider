import scrapy
import bs4
import re
import csv


class chengjiaomessageSpider(scrapy.Spider):
    name = 'chengjiaomessage'
    allowed_domains = ['wh.lianjia.com']
    start_urls = []

    f = open(r'F:\Python爬虫武汉二手房\chengjiao\urls.txt', 'r')
    urls = f.readlines()
    for url in urls:
        start_urls.append(url[0:-1])
    f.close()


    fcsv = open('allcjmessage.csv', mode='w', encoding='utf-8', newline='')
    csv_writer = csv.writer(fcsv)
    csv_writer.writerow(['成交价', '每平方米的价格', '小区名称', '所在区域', '更小的所在区域',
                         '挂牌价格', '成交周期', '调价', '关注', '浏览',
                         '房屋户型', '所在楼层', '建筑面积', '户型结构', '套内面积', '建筑类型',
                         '房屋朝向', '建成年代', '装修情况', '建筑结构', '梯户比例', '配备电梯',
                         '链家编号', '交易权属', '挂牌时间', '房屋用途', '房屋年限', '产权所属'])
    fcsv.close()


    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas_price = bs.find_all('div', class_='price')
        price = ''
        sqmeter = ''
        for data_price in datas_price:
            items = re.findall(r'>[0-9]+\.?[0-9]*', str(data_price))
            price = re.sub(r'>', '', items[0])      #房价 万
            sqmeter = re.sub(r'>', '', items[1])    #每平方米的价格 元/平米
            # print(price, sqmeter)

        msg = bs.find_all('div', class_='msg')
        items = re.findall(r'<label>[0-9]*', str(msg[0]))
        if (items != []):
            gpjg = re.sub(r'<label>', '', items[0])  #挂牌价格  万
            cjzq = re.sub(r'<label>', '', items[1])  #成交周期  天
            tj = re.sub(r'<label>', '', items[2])  #调价  次
            gz = re.sub(r'<label>', '', items[4])  #关注  人
            ll = re.sub(r'<label>', '', items[5])  #浏览  次
            # print(gpjg, cjzq, tj, gz, ll)


        communityName = bs.find_all('div', class_='house-title')
        items = re.findall(r'"wrapper">[^\x00-\xff]*\s?', str(communityName[0]))
        if (items != []):
            communityName = re.sub(r'"wrapper">', '', items[0][0:-1])  #小区名称
            # print(communityName)

        areaName = bs.find_all('div', class_='deal-bread')
        items = re.findall(r'">[^\x00-\xff]*二手房成交', str(areaName[0]))
        areaNameBig = re.sub(r'">', '', items[1][0:-5])     #所在区域
        areaNameSmall = re.sub(r'">', '', items[2][0:-5])   # 更小的所在区域
        # print(areaNameBig, areaNameSmall)

        base = bs.find_all('div', class_='base')
        items = re.findall(r'</span>\S*[^\x00-\xff]*\s*\S*[^\x00-\xff]*\S*\s*</l', str(base))
        fwhx = re.sub(r'\s*', '', items[0][7:-3])  #房屋户型
        szlc = re.sub(r'\s*', '', items[1][7:-3])  #所在楼层
        jzmj = re.sub(r'\s*', '', items[2][7:-3])  #建筑面积
        hxjg = re.sub(r'\s*', '', items[3][7:-3])  #户型结构
        tnmj = re.sub(r'\s*', '', items[4][7:-3])  #套内面积
        jzlx = re.sub(r'\s*', '', items[5][7:-3])  #建筑类型
        fwcx = re.sub(r'\s*', '', items[6][7:-3])  #房屋朝向
        jcnd = re.sub(r'\s*', '', items[7][7:-3])  #建成年代   新增
        zxqk = re.sub(r'\s*', '', items[8][7:-3])  #装修情况
        jzjg = re.sub(r'\s*', '', items[9][7:-3])  #建筑结构
        thbl = re.sub(r'\s*', '', items[11][7:-3])  #梯户比例
        pbdt = re.sub(r'\s*', '', items[12][7:-3])  #配备电梯
        # print(fwhx, szlc, jzmj, hxjg, tnmj, jzlx, fwcx, jcnd, zxqk, jzjg, thbl, pbdt)


        transaction = bs.find_all('div', class_='transaction')
        items = re.findall(r'</span>\S*[^\x00-\xff]*\s*\S*[^\x00-\xff]*\S*</l', str(transaction))
        ljbh = re.sub(r'\s*', '', items[0][7:-3])  #链家编号
        jyqs = re.sub(r'\s*', '', items[1][7:-3])  #交易权属
        gpsj = re.sub(r'\s*', '', items[2][7:-3])  #挂牌时间
        fwyt = re.sub(r'\s*', '', items[3][7:-3])  #房屋用途
        fwnx = re.sub(r'\s*', '', items[4][7:-3])  #房屋年限
        cqss = re.sub(r'\s*', '', items[5][7:-3])  #产权所属
        # print(ljbh, jyqs, gpsj, fwyt, fwnx, cqss)

        fcsv = open('allcjmessage.csv', mode='a+', encoding='utf-8', newline='')
        csv_writer = csv.writer(fcsv)
        csv_writer.writerow([price, sqmeter, communityName, areaNameBig, areaNameSmall,
                             gpjg, cjzq, tj, gz, ll,
                             fwhx, szlc, jzmj, hxjg, tnmj, jzlx, fwcx, jcnd, zxqk, jzjg, thbl, pbdt,
                             ljbh, jyqs, gpsj, fwyt, fwnx, cqss])
        fcsv.close()
