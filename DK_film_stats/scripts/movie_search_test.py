# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:04:49 2017

@author: Alp
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

example_movie_list = ["antichrist", "festen"]

url_1 = "http://lumiere.obs.coe.int"
movie_db_url_base = "http://theapache64.xyz:8080/movie_db/search?keyword="

r = requests.get(movie_db_url_base+example_movie_list[1])
html_doc = r.text

soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())

for link in soup.findall('a'):
    print(link.get("href"))
