# -*- coding: utf-8 -*-
from lxml import etree
import demjson
import city


def print_province():
    html = etree.HTML(city.get_changecity_html())
    change_city_html = html.xpath('//*[@id="changeCity"]/span[2]')
    data_params = change_city_html[0].attrib['data-params']
    # print(data_params)
    data = demjson.decode(data_params)['data']
    name_map = data['def']
    link = data['link']
    for pid in sorted(link):
        print(pid, name_map[pid])



def print_city():
    html = etree.HTML(city.get_changecity_html())
    change_city_html = html.xpath('//*[@id="changeCity"]/span[2]')
    data_params = change_city_html[0].attrib['data-params']
    # print(data_params)
    data = demjson.decode(data_params)['data']
    name_map = data['def']
    link = data['link']
    for pid in sorted(link):
        print(pid, name_map[pid])
        for cid in link[pid]:
            print('\t', cid, name_map[cid])


if __name__ == '__main__':
    # print_province()
    print_city()
