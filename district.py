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


def get_html(city):
    url = 'http://{}.meituan.com/category/'.format(city)
    filename = '{}.html'.format(city)
    return tmp_file.get_content_by_url(url, filename)


def print_district():
    city = 'wf'
    html = etree.HTML(get_html(city))
    xpath_data = html.xpath('//div[@data-component="filter-geo"]/div/ul/li')
    for li in xpath_data:
        a = li.findall('.//a')[0]
        url = a.attrib['href']
        city, district = get_pinyin_from_url(url)
        if not district:
            continue
        name = a.text
        print(city, district, name)


if __name__ == '__main__':
    print_district()
