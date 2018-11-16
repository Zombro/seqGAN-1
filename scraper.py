# -*- coding: utf-8 -*-
"""
@author: kevzo

Scrape "Metamorphosis" (Franz Kafka) off project Gutenberg
https://www.gutenberg.org/files/5200/5200-h/5200-h.htm
"""

import requests
from bs4 import BeautifulSoup


def kafka():
    '''scrapes metamorphosis and returns a big string
         just something quick to get going with interesting sample text'''
    r = requests.get('https://www.gutenberg.org/files/5200/5200-h/5200-h.htm')
    assert(r.status_code == 200)
    html = BeautifulSoup(r.text, 'html.parser')
    return '\n'.join([p.text for p in html.find_all('p')])
