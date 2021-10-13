import scrapy
from selenium import webdriver
#pip install selenium
from datetime import date


class BedrosiansSpider(scrapy.Spider):
    name = "bedrosians"

    start_urls = [
        'https://www.bedrosians.com/en/product/list/slabs/?pageSize=180&page=1'

    ]

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        super(BedrosiansSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        i = 0;
        allNames = response.xpath('//*[@class="product-card-title"]/a/text()').extract()
        allImgs = response.xpath('//*[@class="product-card-image-container"]/a/img/@data-src').extract()

        for site in allNames:

            conferencia = ''
            deposito = 0

            material = ''
            nome = allNames[i].replace('\n\t\t\t', '').replace('	', '')
            qtd = ''
            unimed = ''

            cliente = 'BEDROSIANS TILE & STONE'
            uf = 'CA'  #temp
            siteurl = 'bedrosians.com'
            inventario = 'N'

            img = 'https:' + allImgs[i]

            i +=1

            yield {
                'conferencia': conferencia,
                'deposito': deposito,

                'material': material,
                'nome': nome,
                'qtd': qtd,
                'unimed': unimed,

                'cliente': cliente,
                'UF': uf,
                'site': siteurl,
                'inventario': inventario,

                'datadado': date.today(),
                'img': img,
                'link': response.request.url

            }

        temNext = response.xpath('//*[@class= "plp-prev-next-btn next"]').extract()

        if len(temNext) > 1:
            generate_next_page = response.request.url

            number_page_atual = generate_next_page[-1:]
            next_page_number = int(number_page_atual) + 1

            url_atual = generate_next_page[:-1]
            next_page_url = url_atual + str(next_page_number)

            print('>>>>>>>>>' + next_page_url)
            yield response.follow(next_page_url, callback=self.parse)




