# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import  re
from ..items import TvshowItem


class TvSpider(CrawlSpider):
    name = 'tv'
    allowed_domains = ['ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/tv/hytv/list_71_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'list_71_\d+\.html'), follow=True),

        Rule(LinkExtractor(allow=r'hytv/\d+/\d+\.html'), callback='prase_detail', follow=False),
    )

    def parse_item(self, response):
        print(response.url)
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
    def prase_detail(self,response):
        item=TvshowItem()
        title=response.xpath('//font[@color="#07519a"]/text()').get()
        item["title"]=title
        infos=response.xpath('//div[@id="Zoom"]//p//text()').getall()[:10]

        for info in infos:
            if "◎译　　名　" in info:
                yiming=re.sub(r"◎译　　名　","",info)
                item["yiming"]=yiming
            elif "◎年　　代　" in info:
                year=re.sub(r"◎年　　代　","",info)
                item["year"]=year
            elif "◎产　　地　"in info:
                country=re.sub(r"◎产　　地　","",info)
                item["country"]=country
            elif "◎类　　别　" in info:
                tag=re.sub(r"◎类　　别　","",info)
                item["tag"]=tag
            elif "◎语　　言　" in info:
                language = re.sub(r"◎语　　言　", "", info)
                item["tag"] = language
            elif "◎上映日期　" in info:
                date=re.sub(r"◎上映日期　","",info)
                item['date']=date
            elif "◎集　　数　" in info:
                chapter=re.sub("◎集　　数　","",info)
                item["chapter"]=chapter
            elif "◎片　　长　"in info:
                duration=re.sub(r"◎片　　长　","",info)
                item['duration']=duration
            elif "◎导　　演　" in info:
                director=re.sub(r"◎导　　演　","",info)
                item['director']=director

        yield item








