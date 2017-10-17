# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:04:49 2017

@author: Alp
"""

import requests
from bs4 import BeautifulSoup

#movie_db_url_base = "http://theapache64.xyz:8080/movie_db/search?keyword="

producing_country_id = "DK"
payload = {'producing_country_id': producing_country_id, 'search':'Search'}
url = "http://lumiere.obs.coe.int/web/search/index.php"

r = requests.post(url, data = payload)
html_doc = r.text
soup = BeautifulSoup(html_doc, "lxml")

# Create dictionary of lists
movies = {"film_name": [], "producing_country":[],
              "production_year": [], "directors": [],
              "admissions_eu": []}

lang = "DA"

# Populate the dictionary lists matching with the search language
for name in soup.findAll('a'):
    if lang in str(name):
        movies["film_name"].append(str(name)[4:-10])
    if '(' not in str(name):
        movies["directors"].append(str(name))

# Trial for missing films
names = []        
for name in soup.findAll('a'):
    if "film_info" in str(name):
        names.append(name)
names
