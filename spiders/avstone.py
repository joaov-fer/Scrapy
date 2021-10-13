import scrapy
import json
from datetime import date
from scrapy import Request

class AvStoneSpider(scrapy.Spider):
    name = 'avstone'

    def start_requests(self):


        url = "http://avstones.com/Shop/GetBundleList"

        payload = []

        payload.append("{\"param\":{\"materialId\":\"Exotic\"},\"pageno\":1,\"sortBy\":0,\"displaylength\":10000}")
        payload.append("{\"param\":{\"materialId\":\"Basic\"},\"pageno\":1,\"sortBy\":0,\"displaylength\":10000}")
        payload.append("{\"param\":{\"materialId\":\"Marble\"},\"pageno\":1,\"sortBy\":0,\"displaylength\":10000}")
        payload.append("{\"param\":{\"materialId\":\"Quartz\"},\"pageno\":1,\"sortBy\":0,\"displaylength\":10000}")
        payload.append("{\"param\":{\"materialId\":\"Quartzite\"},\"pageno\":1,\"sortBy\":0,\"displaylength\":10000}")

        headers = {
            'Content-Type': 'application/json'
        }

        for body in payload:
            yield Request(url, callback=self.parse, method="POST", headers=headers, body=body)

    def parse(self, response):
        jsonresponse = json.loads(response.body)

        for item in jsonresponse['result']:

            img = ''
            if item['Image_Name'] is not None and item['Image_Path'] is not None:
                img = 'http://avstones.com' + item['Image_Path'] + item['Image_Name']

            uf = 'IL'
            deposito = 1

            yield {

                'conferencia': item['ROWNUMBER'],
                'deposito': deposito,

                'material': item['Material_Type'].upper(),
                'nome': item['Material_Name'],
                'qtd': int(item['Qty_Slabs']),
                'unimed': 'SLABS',

                'cliente': 'AV STONE',
                'UF': uf,
                'site': 'http://avstones.com/Home/Index',
                'inventario': 'S',

                'datadado': date.today(),
                'img': img,
                'link': None

            }

        # scrapy runspider avstone.py -o data/avstone.json



