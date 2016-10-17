# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RteplayerItem(scrapy.Item):
    """
    This is the URL of a Show Episode, with the Show Name.
    You can pass the URL to youtube-dl to get the episode.
    """
    show_name = scrapy.Field()
    episode_num = scrapy.Field()
    episode_date = scrapy.Field()
    episode_image = scrapy.Field()
    episode_description = scrapy.Field()
    episode_url = scrapy.Field()
