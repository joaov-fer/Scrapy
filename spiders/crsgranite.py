import scrapy
import json
from datetime import date

class CrsGranite(scrapy.Spider):
    name = 'crsgranite'

    start_urls = [
        'https://crsgranite.com/stones/granite/',
        'https://crsgranite.com/stones/marble/',
        'https://crsgranite.com/stones/quartz/',
        'https://crsgranite.com/stones/quartzite/',
        'https://crsgranite.com/stones/soapstones/'

    ]


    def parse(self, response):

         material = response.css('div > h2::text').get().split(' ')[0]

         for site in response.css('div.page-content.mt-5 > div > div > div > div.row> div.col-md-4'):

             yield {

                 'conferencia': '',
                 'deposito': 1,

                 'material': material,
                 'nome' : site.css('div.product-item > h3 > a::text').get(),
                 'qtd': '',
                 'unimed': '',

                 'cliente': 'CRS MARBLE & GRANITE',
                 'UF' : 'SC',
                 'site': 'https://crsgranite.com/',
                 'inventario' : 'N',

                 'datadado': date.today(),
                 'img': site.css('div.pi-img-wrapper > img::attr(src)').get(),
                 'link': response.request.url

             }


         for next_page_url in response.css('body > div.page-content.mt-5 > div > div > div > div.post-nav > ul > li'):
             if next_page_url.css('li > a[title="next"]'):
                 next_page_url = next_page_url.css('a::attr(href)').extract_first()
                 print('>>>>>>>' + str(next_page_url))
                 yield response.follow(next_page_url, callback=self.parse)