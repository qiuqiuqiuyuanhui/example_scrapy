from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, ExampleWebScrapingWebsiteItem


class ExampleWebscraping(BasePortiaSpider):
    name = "example.webscraping.com"
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(ExampleWebScrapingWebsiteItem,
                   None,
                   'table',
                   [Field('population',
                          'tr:nth-child(3) > .w2p_fw *::text, tbody > tr:nth-child(3) > .w2p_fw *::text',
                          []),
                       Field('country',
                             'tr:nth-child(5) > .w2p_fw *::text, tbody > tr:nth-child(5) > .w2p_fw *::text',
                             [])])]]
