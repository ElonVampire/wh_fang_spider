import scrapy
import bs4
import re


class chengjiaoSpider(scrapy.Spider):
    name = 'chengjiao'
    allowed_domains = ['wh.lianjia.com']
    start_urls = []

    areas = ["jiangan", "jianghan", "qiaokou", "dongxihu", "wuchang", "qingshan", "hongshan", "hanyang", "donghugaoxin",
             "jiangxia", "caidian", "huangbei", "xinzhou", "zhuankoukaifaqu", "hannan"]
    for area in areas:
        for num in range(100):
            url = 'https://wh.lianjia.com/chengjiao/' + area + '/pg' + str(num + 1) + '/'
            start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('a')
        f = open('urls.txt', 'a+')
        for data in datas:
            items = re.findall(r'https://wh.lianjia.com/chengjiao/[0-9]*.html"\s*target="_blank"><img', str(data))
            if(items != []):
                item = re.sub(r'"\s*target="_blank"><img', '', items[0])
                f.write(item + '\n')
        f.close()

