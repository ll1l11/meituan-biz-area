# -*- coding: utf-8 -*-
"""通过网页版的美团获取城市列表
将结果保存到cities.json
"""
import re
import json
import string
from lxml import etree
import tmp_file

_CITY_URL_PATTERN = re.compile('http://(\w+)\.')


def get_changecity_html(read_cache=True):
    url = 'http://www.meituan.com/index/changecity/initiative'
    filename = 'changecity_initiative.html'
    return tmp_file.get_content_by_url(url, filename, read_cache)


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
    print(items)
    save(items)


def test():
    # print(get_changecity_html())
    html = etree.HTML(get_changecity_html())
    result = html.xpath('//*[@id="changeCity"]/span[2]')
    print(result)
    print(result[0].attrib['data-params'])


if __name__ == '__main__':
    main()
