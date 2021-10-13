import scrapy
import json
from datetime import date
from scrapy import Request

class MonsterSpiderSpider(scrapy.Spider):
    name = 'agmimports'

    link_long = '&InventoryGroupBy=IDTwo_&Intransit=null&SelectedLocation=&ShowLocationinGallery=on'

    start_urls = [
        'https://agmimports.stoneprofits.com/custom/agmimports/FetchDataWebV1.ashx?act=getItemInventory&id={}'
         .format(str(i + 1) + link_long) for i in range(2500,6000)
    ]


    def parse(self, response):
         jsonresponse = json.loads(response.body)


         for item in jsonresponse:

             img = ''
             if item['FileName'] != '':
                 img = 'https://production120files.stoneprofits.com/Files/agmimports/' + item['FileName']

             uf = item['LocationID']

             # Atlanta
             if uf == 3:
                 uf = 'GA'

             # Charleston / Hilton Head
             elif uf == 5 or uf == 2:
                 uf = 'SC'

             #Charlote
             elif uf == 4:
                 uf = 'NC'

             yield {

                 'conferencia': item['ItemID'],
                 'deposito': item['LocationID'],

                 'material': item['CategoryName'].upper(),
                 'nome' : item['ItemName'],
                 'qtd': item['AvailableSlabs'],
                 'unimed': 'SLABS',

                 'cliente': 'AGM IMPORTS',
                 'UF' : uf,
                 'site': 'https://www.agmimports.com/',
                 'inventario' : 'S',

                 'datadado': date.today(),
                 'img': img,
                 'link': None

             }

             # scrapy runspider agmimports.py -o data/agmimports.json