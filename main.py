# -*- coding: utf-8 -*-

import requests

tag = {'q':'аренда+квартиры+в+москве'}
r = requests.get("https://www.avito.ru/moskva", params=tag)
# print(r.url)
# print(r.text)
# print(r.encodin)
print(r.content)