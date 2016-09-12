# -*- coding: utf-8 -*-
"""通过网页版的美团获取城市列表
将结果保存到cities.json
"""
import os
import os.path
import re
import json
import string
import requests
from lxml import etree

_CITY_URL_PATTERN = re.compile('http://(\w+)\.')
_TMP_DIR = 'tmp-dir'


def check_tmp_dir():
    if not os.path.exists(_TMP_DIR):
        os.makedirs(tmp_dir)


def get_changecity_html(read_cache=True):
    # 网页版城市列表
    check_tmp_dir()
    path = '{}/changecity.html'.format(_TMP_DIR)
    if os.path.isfile(path):
        with open(path) as f:
            return f.read()
    url = 'http://www.meituan.com/index/changecity/initiative'
    html = requests.get(url).text
    with open(path, 'w') as f:
        f.write(html)
    return html


def get_pinyin_by_url(url):
    m = _CITY_URL_PATTERN.match(url)
    if m:
        return m.group(1)



def parse_city(html, letter):
    xpath = '//*[@id="city-{0}"]'.format(letter)
    result = html.xpath(xpath)
    if not result:
        return
    # print(result[0])
    cities = []
    for a in result[0].findall('.//a'):
        name = a.text
        url = a.attrib['href']
        pinyin = get_pinyin_by_url(url)
        city = dict(
            name=name,
            pinyin=pinyin
        )
        cities.append(city)
    return cities


def save(items):
    content = json.dumps(items)
    with open('cities.json', 'w') as f:
        f.write(content)


def main():
    html = etree.HTML(get_changecity_html())
    # xpath: //*[@id="city-B"]
    items = []
    for letter in string.ascii_uppercase:
        cities = parse_city(html, letter)
        item = dict(
            letter=letter,
            cities=cities
        )
        items.append(item)
    save(items)


def test():
    # print(get_changecity_html())
    html = etree.HTML(get_changecity_html())
    result = html.xpath('//*[@id="changeCity"]/span[2]')
    print(result)
    print(result[0].attrib['data-params'])



if __name__ == '__main__':
    main()
