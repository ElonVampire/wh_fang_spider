import scrapy
import bs4
import re
import csv


class messageSpider(scrapy.Spider):
    name = 'message'
    allowed_domains = ['wh.lianjia.com']
    start_urls = []

    f = open(r'F:\Python爬虫武汉二手房\ershou\urls.txt', 'r')
    urls = f.readlines()
    for url in urls:
        start_urls.append(url[0:-1])
    f.close()


    fcsv = open('allmessage.csv', mode='w', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(fcsv)
    csv_writer.writerow(['房价', '每平方米的价格', '小区名称', '所在区域', '更小的所在区域',
                         '房屋户型', '所在楼层', '建筑面积', '户型结构', '套内面积', '建筑类型',
                         '房屋朝向', '建筑结构', '装修情况', '梯户比例', '配备电梯', '挂牌时间',
                         '交易权属', '上次交易', '房屋用途', '房屋年限', '产权所属', '房本备件', '房管局核验码'])
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

        communityName = bs.find_all('div', class_='communityName')
        items = re.findall(r'target="_blank">[^\x00-\xff]*', str(communityName[0]))
        if (items != []):
            communityName = re.sub(r'target="_blank">', '', items[0])  #小区名称
            # print(communityName)

        areaName = bs.find_all('div', class_='areaName')
        items = re.findall(r'target="_blank">[^\x00-\xff]*', str(areaName[0]))
        areaNameBig = re.sub(r'target="_blank">', '', items[0])     #所在区域
        areaNameSmall = re.sub(r'target="_blank">', '', items[1])   # 更小的所在区域
        # print(areaNameBig, areaNameSmall)

        base = bs.find_all('div', class_='base')
        items = re.findall(r'</span>\S*[^\x00-\xff]*\s*\S*[^\x00-\xff]*\S*</l', str(base))
        fwhx = re.sub(r'</span>', '', items[0][0:-3])  #房屋户型
        szlc = re.sub(r'</span>', '', items[1][0:-3])  #所在楼层
        jzmj = re.sub(r'</span>', '', items[2][0:-3])  #建筑面积
        hxjg = re.sub(r'</span>', '', items[3][0:-3])  #户型结构
        tnmj = re.sub(r'</span>', '', items[4][0:-3])  #套内面积
        jzlx = re.sub(r'</span>', '', items[5][0:-3])  #建筑类型
        fwcx = re.sub(r'</span>', '', items[6][0:-3])  #房屋朝向
        jzjg = re.sub(r'</span>', '', items[7][0:-3])  #建筑结构
        zxqk = re.sub(r'</span>', '', items[8][0:-3])  #装修情况
        thbl = re.sub(r'</span>', '', items[9][0:-3])  #梯户比例
        pbdt = re.sub(r'</span>', '', items[10][0:-3])  #配备电梯
        # print(fwhx, szlc, jzmj, hxjg, tnmj, jzlx, fwcx, jzjg, zxqk, thbl, pbdt)


        transaction = bs.find_all('div', class_='transaction')
        items = re.findall(r'\s*</span>\S*[^\x00-\xff]*\s*\S*[^\x00-\xff]*\S*</span>', str(transaction))
        gpsj = re.sub(r'</span>\n<span>', '', items[0][0:-7])  #挂牌时间
        jyqs = re.sub(r'</span>\n<span>', '', items[1][0:-7])  #交易权属
        scjy = re.sub(r'</span>\n<span>', '', items[2][0:-7])  #上次交易
        fwyt = re.sub(r'</span>\n<span>', '', items[3][0:-7])  #房屋用途
        fwnx = re.sub(r'</span>\n<span>', '', items[4][0:-7])  #房屋年限
        cqss = re.sub(r'</span>\n<span>', '', items[5][0:-7])  #产权所属
        fbbj = re.sub(r'</span>\n<span>', '', items[6][0:-7])  #房本备件
        fgjhym = ''  #房管局核验码
        if(len(items) < 8):
            fgjhym = fgjhym
        else:
            fgjhym = re.sub(r'</span>\n<span>', '', items[7][0:-7])  #房管局核验码
        # print(gpsj, jyqs, scjy, fwyt, fwnx, cqss, fbbj, fgjhym)

        fcsv = open('allmessage.csv', mode='a+', encoding='utf-8-sig', newline='')
        csv_writer = csv.writer(fcsv)
        csv_writer.writerow([price, sqmeter, communityName, areaNameBig, areaNameSmall,
                             fwhx, szlc, jzmj, hxjg, tnmj, jzlx, fwcx, jzjg, zxqk, thbl, pbdt,
                             gpsj, jyqs, scjy, fwyt, fwnx, cqss, fbbj, fgjhym])
        fcsv.close()

