# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:04:49 2017

@author: Alp
"""

import requests
from bs4 import BeautifulSoup

#example_movie_list = ["antichrist", "festen"]
#movie_db_url_base = "http://theapache64.xyz:8080/movie_db/search?keyword="
#r = requests.get(movie_db_url_base+example_movie_list[1])

payload = {'producing_country_id': 'DK', 'search':'Search'}
url = "http://lumiere.obs.coe.int/web/search/index.php"

r = requests.post(url, data = payload)
html_doc = r.text
soup = BeautifulSoup(html_doc, "lxml")
print(soup.prettify())


