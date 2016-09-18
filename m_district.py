# -*- coding: utf-8 -*-
from lxml import etree
import tmp_file
import demjson


def get_city_html(city):
    url = 'http://i.meituan.com/{}'.format(city)
    filename = 'm_{0}.html'.format(city)
    return tmp_file.get_content_by_url(url, filename)


def main():
    city = 'weifang'
    html = etree.HTML(get_city_html(city))
    xpath_data = html.xpath('//*[@id="filterData"]')
    js_content = xpath_data[0].text
    data = demjson.decode(js_content)
    for biz_area in data['BizAreaList']:
        print(biz_area)

if __name__ == '__main__':
    main()
