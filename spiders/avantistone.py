from datetime import date

import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'Avanti'

    start_urls = [
            'https://www.avantistones.com/gallery/index.php?materialType=GRANITE&page={}'.format(str(i + 1)) for i in range(0, 13) ] + [

            'https://www.avantistones.com/gallery/index.php?materialType=DOLOMITE',
            'https://www.avantistones.com/gallery/index.php?materialType=LIMESTONE',
            'https://www.avantistones.com/gallery/index.php?materialType=SCHIST',
            'https://www.avantistones.com/gallery/index.php?materialType=TRAVERTINE'
    ] + [

            'https://www.avantistones.com/gallery/index.php?materialType=MARBLE&page={}'.format(str(i + 1)) for i in range(0, 4)] + [

            'https://www.avantistones.com/gallery/index.php?materialType=QUARTZITE&page={}'.format(str(i + 1)) for i in range(0, 4)

    ]

    def parse(self, response):
        # follow links to author pages
        for href in response.css('tr > td > a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # next_page_url = response.css('table > tr > td >center >  a:nth-child(10)::attr(href)').extract_first()
        # if next_page_url:
        #     next_page_url = 'https://www.avantistones.com/gallery/index.php' + next_page_url
        #     print ('>>>', next_page_url)
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)


    def parse_author(self, response):

        img = response.css('tr > td> a > img::attr(src)').extract_first()
        if img is not None :
            img = 'https://www.avantistones.com' + response.css('tr > td> a > img::attr(src)').extract_first().replace('../..', '')
        else:
            img = ''


        if response.css('table:nth-child(4)> tr:nth-child(1)> td:nth-child(2)::text').get() is not None:
            yield {

                'conferencia': '',
                'deposito': 1,

                'material': response.css('table:nth-child(4)> tr:nth-child(5)> td:nth-child(2)::text').get(),
                'nome':  response.css('table:nth-child(4)> tr:nth-child(1)> td:nth-child(2)::text').get(),
                'qtd': response.css('table:nth-child(4)> tr:nth-child(10)> td:nth-child(2)::text').get(),
                'unimed': 'SLABS',

                'cliente': 'AVANTI STONE',
                'UF': 'TX',
                'site': 'https://www.avantistones.com/',
                'inventario': 'S',

                'datadado': date.today(),
                'img':  img,
                'link': response.request.url

            }

