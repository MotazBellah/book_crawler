import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllBooksSpider(CrawlSpider):
    name = 'all_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ol"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
    )

    def parse_item(self, response):
        # print(response.url)
        yield {
            "name": response.xpath("//h1/text()").get(),
            "price": response.xpath("//p[@class='price_color']/text()").get(),
            "availability": response.xpath("(//td)[6]/text()").get(),
        }
