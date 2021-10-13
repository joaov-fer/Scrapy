# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest, Request
from datetime import date
from scrapy.utils.response import open_in_browser
from selenium import webdriver
import json
import time
from random import randint


class axle(scrapy.Spider):
    name = 'axle'

    start_urls = ['https://iii.slcl.org/iii/cas/login']

    links = []
    paginas = 0

    def parse(self, response):

        lt = response.css('#fm1 > input[type=hidden]:nth-child(6)::attr(value)').get()

        frmdata = {
            "name": "Stein",
            "code": "2856746",
            "pin": "1234",
            "rememberme": "on",
            "lt": lt,
            "_eventId": "submit"
        }


        yield FormRequest.from_response(
            response,
            formdata=frmdata,
            dont_filter=True,
            callback=self.after_login
        )

    # Get Request Key
    def after_login(self, response):
        print('Logado')
        # open_in_browser(response)

        headers = response.request.headers
        yield Request(
            url="http://0-www.referenceusa.com.iii.slcl.org/UsBusiness/Search/Custom",
            headers=headers,
            dont_filter=True,
            method="GET",
            callback=self.find
        )

    def find(self, response):
        print('Find')

        frmdata = {
            'VerifiedRecord' : 'V',
            'NaicsLookup': '32799104,23814005,32799106,32799110,32799111',
            'postbackType': 'viewresults'
        }

        request_key =response.request.url.split('/')[-1]
        headers = response.request.headers
        yield FormRequest(
            url='http://0-www.referenceusa.com.iii.slcl.org/UsBusiness/Search/NewCustomSearchRequest/' + request_key,
            formdata=frmdata,
            headers=headers,
            dont_filter=True,
            callback=self.pre_result
        )


    def pre_result(self, response):
        # open_in_browser(response)
        jsonresponse = json.loads(response.body)
        obj = jsonresponse['data']
        rows = int(obj['totalCount'])
        print('>>>> ' + str(rows))

        paginas = rows/ 25
        if rows % 25 != 0:
            paginas += 1

        request_key =response.request.url.split('/')[-1]

        print('>> Paginas: ' + str(paginas))

        paginas = 1
        for i in range(paginas):
            frmdata = {
                "requestKey": request_key,
                "direction" : "Ascending",
                "pageIndex" : str(i)
            }

            headers = response.request.headers
            last_page = False
            if i == (paginas-1):
                last_page = True

            yield FormRequest(
                url='http://0-www.referenceusa.com.iii.slcl.org/UsBusiness/Result/Page/'+ request_key,
                formdata=frmdata,
                headers=headers,
                dont_filter=True,
                callback=self.result,
                meta={'last_page' : last_page}
            )
            time.sleep(randint(15, 21))

    def result(self, response):
        print('OK')
        # open_in_browser(response)

        for link in response.xpath('//*[@class="action-view-record"]'):

            url = link.css('a::attr(data-tagged-url)').get()
            a_link = 'http://0-www.referenceusa.com.iii.slcl.org' + str(url)
            print(a_link)
            self.links.append(a_link)

        print(response.meta['last_page'])
        if response.meta['last_page']:

            print('>> links')
            headers = response.request.headers
            for link in self.links:
                yield Request(
                    url=link,
                    headers=headers,
                    callback=self.get_infos
                )
                time.sleep(randint(25, 36))

    def get_infos(self, response):
        open_in_browser(response)





# scrapy runspider axle.py -o data/axle.json



