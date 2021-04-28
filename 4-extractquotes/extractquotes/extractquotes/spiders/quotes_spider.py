import scrapy
# main folder, scrapy crawl quotes


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
			
# save as json file :
# scrapy crawl quotes -O quotes.json

# scrapy crawl quotes -o quotes.jl
# o = overwrite


# get from pagination

# scrapy shell "http://quotes.toscrape.com"

# response.css('li.next a').get()
# response.css('li.next a::attr(href)').get()
# response.css('li.next a').attrib['href']

# complete in next function