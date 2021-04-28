import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # opsi 1
            #yield response.follow(next_page, callback=self.parse)  # opsi 2
            
#        for href in response.css('ul.pager a::attr(href)'):  # opsi 3, indent note
#            yield response.follow(href, callback=self.parse)
            
#        anchors = response.css('ul.pager a') # opsi 4, tag indent note
#        yield from response.follow_all(anchors, callback=self.parse)