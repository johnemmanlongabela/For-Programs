import scrapy


class QuotesSpider(scrapy.Spider):
    name = "books"

    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        for book in response.css("div.books"):
            yield {
                "text": book.css("span.text::text").get(),
                "author": book.css("small.author::text").get(),
            }


        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)