import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://shop.tcgplayer.com/yugioh/product/show?ProductName=gimmick']

    def parse(self, response):
        x = []
        itemHeader = {
            'card_name': '',
            'price': '',
            'qty': '',
        }

        for title in response.css('div.sellerContainer'):

            itemHeader['card_name'] = title.css('a ::text').extract_first()

            itemHeader['price'] = title.css('span.pricegreen::text').extract()

#            itemHeader['qty'] = title.css('span.smalltext').extract()

            x.append(itemHeader['card_name'])
            x.append(itemHeader['price'])
#            x.append(itemHeader['qty'])

        print(x)

# for price in response.css('span.pricegreen'):
#            yield {'price': price.css('::text').extract_first()}
