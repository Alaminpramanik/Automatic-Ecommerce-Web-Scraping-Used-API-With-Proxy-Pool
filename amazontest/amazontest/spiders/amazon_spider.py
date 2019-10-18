# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontestItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number=2
#    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/b?node=18332383011&pf_rd_p=6c9ccc0f-f483-458d-984d-5a71fbae856e&pf_rd_r=93XHW3CQSBKMBYQZ7MWQ'
    ]

    def parse(self, response):
        items=AmazontestItem()

        product_name=response.css('.s-access-title::text').extract()
        product_author=response.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
        product_price = response.css('.a-price-fraction , .a-price-whole , #result_3 .a-color-base').css('::text').extract()
        product_imglink = response.css('.cfMarker::attr(src)').extract()

        items['product_name']= product_name
        items['product_author']= product_author
        items['product_price']= product_price
        items['product_imglink']= product_imglink

        yield items

        next_page="https://www.amazon.com/s?i=specialty-aps&srs=18332383011&page=' + AmazonSpiderSpider.page_number + '&qid=1571361371&ref=lp_18332383011_pg_2"
        if AmazonSpiderSpider.page_number <=10:
            yield response.follow(next_page, callback=self.parse)
