import scrapy
#run in main folder, scrapy crawl quotes


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
			


# Jalankan di Anaconda Prompt, atau prompt.exe 			
			
# scrapy shell "http://quotes.toscrape.com/page/1/"			  # selecting

# response.css('title')
# response.css('title::text').getall()
# response.css('title').getall()
# response.css('title::text').get()
# response.css('title::text')[0].get()
# regex
# response.css('title::text').re(r'Quotes.*')
# response.css('title::text').re(r'Q\w+')
# response.css('title::text').re(r'(\w+) to (\w+)')

# response.xpath('//title')
# response.xpath('//title/text()').get()




# extracting :


# scrapy shell "http://quotes.toscrape.com"

# response.css("div.quote")
# quote = response.css("div.quote")[0]
# text = quote.css("span.text::text").get()
# text

# author = quote.css("small.author::text").get()
# author

# tags = quote.css("div.tags a.tag::text").getall()
# tags

# for quote in response.css("div.quote"):
# text = quote.css("span.text::text").get()
# author = quote.css("small.author::text").get()
# tags = quote.css("div.tags a.tag::text").getall()
# print(dict(text=text, author=author, tags=tags))