import scrapy


class MobileScraper(scrapy.Spider):
    name = 'Mobile'
    start_urls = ['https://www.whatmobile.com.pk/Samsung_Mobiles_Prices',
                  'https://www.whatmobile.com.pk/Huawei_Mobiles_Prices',
                  'https://www.whatmobile.com.pk/Vivo_Mobiles_Prices']

    def parse(self, response):
        for products in response.css('div.item'):
            yield {
                'name': products.css('a').attrib['href'].replace('/', ''),
                'price': products.css('span.PriceFont::text').get().replace('\n', '').replace('Rs. ', ''),
                'link': products.css('a').attrib['href']
            }
