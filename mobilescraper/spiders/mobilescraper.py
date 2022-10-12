import scrapy
import csv
import pandas as pd


class MobileScraper(scrapy.Spider):
    name = 'Mobile'
    start_urls = ['https://www.whatmobile.com.pk/Samsung_Mobiles_Prices',
                  'https://www.whatmobile.com.pk/Huawei_Mobiles_Prices',
                  'https://www.whatmobile.com.pk/Vivo_Mobiles_Prices']

    mobile_dict = dict()

    def parse(self, response):
        for products in response.css('div.item'):

            link = 'https://www.whatmobile.com.pk/' + \
                   products.css('a').attrib['href']

            yield scrapy.Request(
                link, self.parse_products, dont_filter=False)

    def parse_products(self, response):
        for block in response.css('div#centerContainer'):
            self.mobile_dict['Name'] = block.css('h1.hdng3::text').get()
            self.mobile_dict['Price'] = block.css(
                'span.hdng::text').get().replace('\nRs. ', '')

        for table in response.css('table.specs'):
            features = table.css(
                'td.specs-value::text').getall()
            for i in range(0, len(features)):
                self.mobile_dict[f'Feature{i}'] = features[i].replace(
                    '\xa0\n', '')
            yield self.mobile_dict
