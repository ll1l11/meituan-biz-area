# -*- coding: utf-8 -*-
import tmp_file

def get_html(city, district):
    url = 'http://{0}.meituan.com/category/all/{1}'.format(city, districty)
    filename = 'biz_area_{0}_{1}.html'.format(city, district)
    return tmp_file.get_content_by_url(url, filename)
