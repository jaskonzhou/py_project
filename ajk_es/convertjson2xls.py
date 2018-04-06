import csv
import json


def read_json(filename):
    return json.loads(open(filename,encoding='utf-8').read())


def write_csv(data, filename):
    with open(filename, 'w') as outf:
        dw = csv.DictWriter(outf, data[0].keys())
        dw.writeheader()
        for row in data:
            dw.writerow(row)


write_csv(read_json('E:\scrapy\json\mydata1.json'), 'E:\scrapy\json\lest.csv')