import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://shop.tcgplayer.com/yugioh/product/show?ProductName=gimmick']

    def parse(self, response):
        x = []
        item_list = {
            'card_name': '',
            'price': '',
            'qty': '',
        }

        for each in response.css('div.sellerContainer'):

            item_list['card_name'] = each.css('a ::text').extract_first()

            item_list['price'] = each.css('span.pricegreen::text').extract()

#            item_list['qty'] = each.css('span.smalltext').extract()

            x.append(item_list['card_name'])
            x.append(item_list['price'])
#            x.append(item_list['qty'])

        print(x)