import scrapy
import json
from datetime import date
from scrapy import Request

class CosmosSpider(scrapy.Spider):
    name = 'cosmos'

    link_long = '&InventoryGroupBy=IDTwo_&Intransit=null&SelectedLocation=&ShowLocationinGallery=on'

    start_urls = [
        'https://cosmos.stoneprofits.com/FetchDataWebV1.ashx?act=getItemInventory&id={}'
         .format(str(i + 1) + link_long) for i in range(1,4000)
    ]

    def parse(self, response):
         jsonresponse = json.loads(response.body)


         for item in jsonresponse:

             img = ''
             if item['FileName'] != '':
                 img = 'https://production120files.stoneprofits.com/Files/agmimports/' + item['FileName']

             uf = item['LocationID']

             # Atlanta - SAV
             if uf == 2 or uf == 14:
                 uf = 'GA'

             # Seattle
             elif uf == 10:
                 uf = 'WA'

             #Salt Lake City
             elif uf == 11:
                 uf = 'UT'

             # greensboro
             elif uf == 4 or uf == 5:
                 uf = 'NC'

             # Chicago - SPK / CGM-ORD
             elif uf == 12 or uf == 7:
                uf = 'IL'

             # Portland, OR - PDX
             elif uf == 9:
                 uf = 'OR'

             # CG&M-DC
             elif uf == 13:
                uf = 'DC'

             # CG&M-BNA
             elif uf == 3:
                uf = 'TN'

             # MO -  CG&M-STL
             elif uf == 8:
                uf = 'MO'


             yield {

                 'conferencia': item['ItemID'],
                 'deposito': item['LocationID'],

                 'material': item['CategoryName'].upper(),
                 'nome' : item['ItemName'],
                 'qtd': item['AvailableSlabs'],
                 'unimed': 'SLABS',

                 'cliente': 'COSMOS GRANITE & MABRLE',
                 'UF' : uf,
                 'site': 'https://www.cosmosgranite.com/',
                 'inventario' : 'S',

                 'datadado': date.today(),
                 'img': img,
                 'link': None

             }

             # scrapy runspider cosmos.py -o data/cosmos.json
