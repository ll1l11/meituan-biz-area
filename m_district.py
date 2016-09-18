# -*- coding: utf-8 -*-
import tmp_file


def get_html(city):
    url = 'http://i.meituan.com/{}'.format(city)
    filename = 'm_{0}.html'.format(city)
    return tmp_file.get_content_by_url(url, filename)


if __name__ == '__main__':
    print(get_html('weifang'))
