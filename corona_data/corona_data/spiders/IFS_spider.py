import scrapy
from datetime import datetime, timedelta


def write_to_file(file_name, data):
    with open(file_name, 'w+') as f:
        f.write('\n'.join(data))


def append_to_file(file_name, data):
    with open(file_name, 'a+') as f:
        f.write('\n'.join(data))


def read_last_line(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) > 0:
            return lines[-1]
        else:
            None


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

        db_last_update = read_last_line('latest_update.txt')
        website_latest_update = response.xpath('//*[@id="614137682"]/div/table/tbody/tr[3]/td[1]/text()').getall()[0]

        if db_last_update is not None and db_last_update == website_latest_update:
            return
        else:
            append_to_file('latest_update.txt', ['', website_latest_update])

            file_name = 'IFS.csv'

            col_index = [1, 2, 6, 7, 8, 5, 4, 9, 11]
            data = ['Patient_No, Confirmed_Date, Residence_City, Detected_City, Detected_Prefecture, Gender, Age, Status, Notes']

            length = int(response.xpath('//*[@id="0"]/div/table/tbody/tr/td[1]/text()').getall()[-1])

            for i in range(3, length+3):
                row = []
                for j in col_index:
                    list = response.xpath('//*[@id="0"]/div/table/tbody/tr[{}]/td[{}]/text()'.format(i, j)).getall()
                    print(list)
                    if len(list) > 0:
                        row.append("\"" + list[0]+ "\"")
                    else:
                        if j==4:
                            row.append('0')
                        else:
                            row.append('NULL')

                data.append(','.join(row))

            write_to_file(file_name, data)


