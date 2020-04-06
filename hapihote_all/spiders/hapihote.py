# -*- coding: utf-8 -*-
import scrapy
from hapihote_all.items import HapihoteAllItem


class HapihoteSpider(scrapy.Spider):
    name = 'hapihote'
    allowed_domains = ['happyhotel.jp']
    start_urls = ['https://happyhotel.jp/searchArea.act']

    def parse(self, response):
        for url in response.css("a::attr('href')").re(r'\?pref_id=\d*'):
        # for url in response.css("a"):
            yield response.follow(url,self.parse_topics)

    def parse_topics(self,response):
        for url in response.css("a::attr('href')").re(r'\?jis_code=\d*'):
            yield response.follow(url,self.parse_indivi)


    def parse_indivi(self,response):
        # この画面のロジックを考える
        # リンクあり https://happyhotel.jp/searchArea.act?jis_code=20201
        #  リンクなし https://happyhotel.jp/searchArea.act?jis_code=8203&page=1
        item =HapihoteAllItem()

        for idx in response.css(".hotel"):
            item["A_hotel_name"] = idx.css("h1 .name").xpath('string()').get()


            info = idx.css("h2").xpath('string()').get()
            info_list  = info.split("\n\t\t\t")
            item["B_adress"] = info_list[1]
            item["C_tel"] = info_list[2].replace("TEL: ","")


        last_num = (len(response.css(".guide.bottom > .pagerNav").css('a'))-1)
        if response.css(".guide.bottom > .pagerNav").css('a').get() is not None:
            if response.css(".guide.bottom > .pagerNav").css('a')[last_num].xpath('string()').get() ==  '>>':
                print("================================")
                next_page = response.css(".guide.bottom > .pagerNav").css('a')[last_num].css('::attr(href)').extract_first()
                next_page = "https://happyhotel.jp/" + next_page
                print(next_page)
                print("================================")
                print("================================")
                print("================================")
                print("================================")
                yield scrapy.Request(next_page, callback=self.parse_indivi)

        yield item


