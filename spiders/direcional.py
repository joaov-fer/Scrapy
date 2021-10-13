

import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'direcional'

    start_urls = [
        'https://direcional.com.br/minas-gerais/encontre-seu-imovel/',
        'https://direcional.com.br/rio-de-janeiro/encontre-seu-imovel/',
        'https://direcional.com.br/sao-paulo/encontre-seu-imovel/',
        'https://direcional.com.br/ceara/encontre-seu-imovel/',
        'https://direcional.com.br/amazonas/encontre-seu-imovel/',
        'https://direcional.com.br/distrito-federal/encontre-seu-imovel/',
        'https://direcional.com.br/pernambuco/encontre-seu-imovel/'

    ]

    def parse(self, response):
        # follow links to author pages
        for href in response.css('a.btn-verde.btn-lg.btn::attr(href)'):
            yield response.follow(href, self.parse_author)


    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        if extract_with_css('div.resumo-empreendimento > h1::text') != '':
            yield {

                'link': response.request.url,
                'mome': extract_with_css('div.resumo-empreendimento > h1::text'),
                'local': extract_with_css('div.resumo-empreendimento > h2::text'),
                'caracteristicas': response.css('div.item-caracteristica > p::text').getall(),
                'status': extract_with_css('li.active.clearfix > p::text'),
                'endereco': extract_with_css('div.info-como-chegar > p::text')

                #'birthdate': extract_with_css('.author-born-date::text'),
                #'bio': extract_with_css('.author-description::text'),
            }