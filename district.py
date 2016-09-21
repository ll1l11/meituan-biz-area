# -*- coding: utf-8 -*-
import re
from lxml import etree
import tmp_file

_DISTRICT_PATERN = \
    re.compile('http://(\\w+)\.meituan\.com/category/all/(\\w+)$')


def get_pinyin_from_url(url):
    m = _DISTRICT_PATERN.match(url)
    if m:
        return m.group(1), m.group(2)
    return None, None


def get_city_html(city):
    url = 'http://{}.meituan.com/category/'.format(city)
    filename = '{}.html'.format(city)
    return tmp_file.get_content_by_url(url, filename)


def get_biz_area(city, district):
    url = 'http://{0}.meituan.com/category/all/{1}'.format(city, district)
    filename = 'biz_area_{0}_{1}.html'.format(city, district)
    return tmp_file.get_content_by_url(url, filename)


def print_district():
    city = 'wf'
    print_result(get_city_html(city))


def print_biz_area():
    city = 'bj'
    district = 'chaoyangqu'
    print_result(get_biz_area(city, district))


def print_result(content):
    html = etree.HTML(content)
    # xpath_data = html.xpath('//div[@data-component="filter-geo"]/div[last()]')
    # xpath_data = html.xpath('//div[@data-component="filter-geo"]/div')
    xpath_data = html.xpath('//div[contains(@data-component, "filter-geo")]/div')
    print('*' * 20)
    print(xpath_data)
    print('\n')
    for a in xpath_data[-1].xpath('.//ul[contains(@class, "J-")]/li/a'):
    # for a in xpath_data[-1].findall('.//ul/li/a'):
        url = a.attrib['href']
        city, district = get_pinyin_from_url(url)
        if not district:
            continue
        name = a.text
        print(city, district, name)


if __name__ == '__main__':
    # print_district()
    print_biz_area()
