import scrapy
from datetime import datetime, timedelta


def write_to_file(file_name, data):
    with open(file_name, 'w+') as f:
        f.write('\n'.join(data))


def append_to_file(file_name, data):
    with open(file_name, 'a+') as f:
        f.write('\n'.join(data))


class IFSSpider(scrapy.Spider):
    name = "ifs"

    def start_requests(self):
        urls = [
            'https://docs.google.com/spreadsheets/d/1zIgPU0ZlYkiKaavYAUcHKgEP95jdaMaf9ljJgRqtog4/htmlview#'
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = ("IFS_{}".format(response.xpath('//*[@id="614137682"]/div/table/tbody/tr[3]/td[1]/text()').getall()[0]))\
            .replace(":", "-").replace(", ", "_").replace(" ", "_")

        col_index = [1, 2, 6, 7, 8,5, 4, 9, 11]

        write_to_file(file_name, ['Patient_No, Confirmed_Date, Age, Gender, Residence_City, Detected_City, '
                                  'Detected_Prefecture, Status, Notes', ''])

        data = ['Patient_No, Confirmed_Date, Age, Gender, Residence_City, Detected_City, Detected_Prefecture, Status, Notes']

        length = int(response.xpath('//*[@id="0"]/div/table/tbody/tr/td[1]/text()').getall()[-1])

        for i in range(3, length+3):
            row = []
            for j in col_index:
                list = response.xpath('//*[@id="0"]/div/table/tbody/tr[{}]/td[{}]/text()'.format(i, j)).getall()
                print(list)
                if len(list) > 0:
                    row.append(list[0])
                else:
                    row.append('')

            data.append(','.join(row))

        write_to_file(file_name, data)


