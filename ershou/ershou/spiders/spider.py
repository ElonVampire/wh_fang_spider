import scrapy
import bs4
import re


class ershouSpider(scrapy.Spider):
    name = 'ershou'
    allowed_domains = ['wh.lianjia.com']
    start_urls = []

    areas = ["jiangan", "jianghan", "qiaokou", "dongxihu", "wuchang", "qingshan", "hongshan", "hanyang", "donghugaoxin",
             "jiangxia", "caidian", "huangbei", "xinzhou", "zhuankoukaifaqu", "hannan"]
    for area in areas:
        for num in range(100):
            url = 'https://wh.lianjia.com/ershoufang/' + area + '/pg' + str(num + 1) + '/'
            start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('a')
        f = open('urls.txt', 'a+')
        for data in datas:
            items = re.findall(r'https://wh.lianjia.com/ershoufang/\S*.html"\starget="_blank"><img class=', str(data))
            if(items != []):
                item = re.sub(r'"\starget="_blank"><img class=', '', items[0])
                f.write(item + '\n')
        f.close()

