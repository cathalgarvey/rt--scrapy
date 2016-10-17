# -*- coding: utf-8 -*-
import scrapy
from rteplayer import items


class PlayerSpider(scrapy.Spider):
    name = "player"
    allowed_domains = ["rte.ie"]
#    start_urls = ['https://www.rte.ie/player/ie/a-z/a/']
    start_urls = [
        'https://www.rte.ie/player/ie/a-z/{}/'.format(l) for l in "abcdefghijklmnopqrstuvwxyz"
        ] + ['https://www.rte.ie/player/ie/a-z/0-9/']

    def parse(self, response):
        'Deal with a start URL from the alphabetised show list'
        show_urls = response.css("a.thumbnail-programme-link").xpath("@href").extract()
        show_names = response.css("a.thumbnail-programme-link span.thumbnail-title").xpath("text()").extract()
        for name, url in zip(show_names, show_urls):
            R = scrapy.Request(
              response.urljoin(url),
              callback=self.parse_show
            )
            R.meta['show name'] = name.strip()
            yield R

    def parse_show(self, response):
        "Deal with a show URL."
        show_name = response.meta['show name']
        yield from self.parse_episode(response)
        # The URL representing the Show's top-level URL is actually also an episode
        # URL so will get skipped. That's why we pitched off the show URL, above.
        more = response.css("section.indexpage-content-box.more a.thumbnail-programme-link").xpath("@href").extract()
        for url in more:
            R = scrapy.Request(
              response.urljoin(url),
              callback=self.parse_episode
            )
            R.meta['show name'] = show_name
            yield R

    def parse_episode(self, response):
        "Deal with an episode URL."
        I = items.RteplayerItem()
        I['show_name'] = response.meta['show name']
        I['episode_num'] = response.css("h1.season").xpath("text()").extract_first().strip()
        I['episode_date'] = response.css("li.broadcast-date > span").xpath("text()").extract_first().strip()
        I['episode_image'] = response.css("img.fluid-image").xpath("@src").extract_first().strip()
        I['episode_description'] = response.css("h2[itemprop=description]").xpath("text()").extract_first().strip()
        I['episode_url'] = response.urljoin(response.url)
        yield I
