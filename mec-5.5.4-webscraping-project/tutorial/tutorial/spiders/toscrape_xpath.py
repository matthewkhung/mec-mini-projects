import scrapy


class XpathScrapeSpider(scrapy.Spider):
    name = "toscrape_xpath"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div [@class="quote"]'):
            yield {
                'text': quote.xpath('span [@class="text"]/text()').get(),
                'author': quote.xpath('span/small [@class="author"]/text()').get(),
                'tags': quote.xpath('div [@class="tags"]/a [@class="tag"]/text()').getall()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
