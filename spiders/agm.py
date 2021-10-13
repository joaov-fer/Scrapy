from scrapy.http.cookies import CookieJar
from datetime import date
import scrapy
from scrapy import Request
import requests
from selenium import webdriver

class agm(scrapy.Spider):
      name = "agm"
      domain_name = "agmgranite.com"


      def start_requests(self):

          headers = {
              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}




          ####  35 Spicewood TX
          urls =  ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=3&f=reset&invp=') for i in range(0,35)]

          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=3&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'TX'
          deposito = 1


          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          ####  25 Austin, TX
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=14&f=reset&invp=') for i in range(0, 25)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=14&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'TX'
          deposito = 2

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          # 25 San Antoinio TX
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=6&f=reset&invp=') for i in range(0, 25)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=6&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'TX'
          deposito = 3

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          # 80 raleigh NC
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=5&f=reset&invp=') for i in range(0, 80)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=5&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'NC'
          deposito = 4

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})



          # Oklahoma City, OK  45
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=4&f=reset&invp=') for i in range(0, 45)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=4&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'OK'
          deposito = 5

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          # Nashville, TN  45
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=2&f=reset&invp=') for i in range(0, 45)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=2&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'TN'
          deposito = 6

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          # Tusla, OK  40
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=24&f=reset&invp=') for i in range(0, 40)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=24&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'OK'
          deposito = 7

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          # Kansas City, MO  85
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=23&f=reset&invp=') for i in range(0, 85)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=23&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'MO'
          deposito = 8

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})



          # St Lois, MO  45
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=22&f=reset&invp=') for i in range(0, 45)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=22&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'MO'
          deposito = 9

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})




          # Des Moines, IA  35
          urls = ["https://www.agmgranite.com/paginate.php?page={}".format(str(i + 1) + '&lid=25&f=reset&invp=') for i in range(0, 35)]
          driver = webdriver.PhantomJS()
          driver.get('https://www.agmgranite.com/initial_load.php?&lid=25&f=reset&invp=')
          cookies = driver.get_cookies()
          uf = 'MO'
          deposito = 10

          for url in urls:
            yield Request(url, cookies=cookies, callback=self.gethref, headers=headers, meta={'uf':uf, 'deposito': deposito})



      def get_cookies(self, response):
          cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
          cookies = cookieJar.extract_cookies(response, response.request)
          return cookies



      def gethref(self, response):


          # Pegar detalhes
          for href in response.css('div.slab_right > div.view_detail > a::attr(href)').extract():
               yield response.follow(href, self.parse_author, meta={'uf': response.meta['uf'], 'deposito': response.meta['deposito']})



      def parse_author(self, response):
          def extract_with_css(query):
              return response.css(query).get(default='').strip()

          uf = response.meta['uf']
          deposito = response.meta['deposito']


          if extract_with_css('div.inv_left.clearfix > h3::text') != '':
              yield {

                      'conferencia': '',
                      'deposito': deposito,

                      'material': response.css('div.inv_left.clearfix > div::text').extract_first().replace('\r\n\t\t\t\t\r\n\t\t\t\t\t', '').upper(),
                      'nome' : response.css('div.inv_left.clearfix > h3::text').extract_first().upper(),
                      'qtd': str(response.css('#inventory_detail > div > div.inv_left.clearfix > div::text').extract()[3]).replace(' slabs', '').replace(' slab', '').replace('\r\n\t\t\t\t\t', ''),
                      'unimed': 'SLABS',

                      'cliente': 'AG&M GRANITE',
                      'UF': uf,
                      'site': 'https://www.agmgranite.com/',
                      'inventario': 'S',

                      'datadado': date.today(),
                      'img': response.xpath('//div[contains(@class,"inv_image")]/@style').extract_first().replace("background-image: url('", "").replace("');",  ""),
                      'link': response.request.url

                  }