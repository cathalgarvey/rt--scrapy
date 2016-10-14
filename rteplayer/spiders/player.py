# -*- coding: utf-8 -*-
import scrapy


class PlayerSpider(scrapy.Spider):
    name = "player"
    allowed_domains = ["rte.ie"]
    start_urls = (
        'http://www.rte.ie/',
    )

    def parse(self, response):
        pass
