#  -*- coding: utf-8 -*-
import os
import os.path
import urllib
import requests

_TMP_DIR = 'tmp-dir'


def check_tmp_dir():
    if not os.path.exists(_TMP_DIR):
        os.makedirs(_TMP_DIR)


def get_path(filename):
    return '{0}/{1}'.format(_TMP_DIR, filename)


def get_content(filename):
    path = get_path(filename)
    if os.path.isfile(path):
        with open(path) as f:
            return f.read()


def save(filename, content):
    check_tmp_dir()
    path = get_path(filename)
    with open(path, 'w') as f:
        f.write(content)


def get_filename_by_url(url):
    name = urllib.parse.splitquery(url)[0].rsplit('/', 1)[-1]
    if not name.endswith('.html'):
        name = name + '.html'
    return name


def get_content_by_url(url, filename=None, read_cache=True):
    if not filename:
        filename = get_filename_by_url(url)

    if read_cache:
        content = get_content(filename)
        if content:
            return content
    html = requests.get(url).text
    save(filename, html)
    return html
