import urllib2
import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_list(site):
    source_code = requests.get(site)
    soup = BeautifulSoup(source_code.text,'html.parser')
    table = soup.find('span', id='S.26P_500_Component_Stocks').parent.find_next_sibling('table')
    names = list()
    urls = list()
    ids = list()
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            link = "https://en.wikipedia.org" + col[1].find('a').get('href')
            id1 = col[1].find('a').get('href')[6:]
            urls.append(link)
            name =  str(col[1].string.strip())
            ids.append(id1)
            names.append(name)
    df = pd.concat([pd.Series(names), pd.Series(urls), pd.Series(ids)], axis=1, keys=['names', 'urls','ids'])
    return df

def get_pageid(name):
    url = 'http://en.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=' + name
    resp = requests.get(url)
    data = resp.json()
    try:
        return data['query']['pages'].itervalues().next()['pageid']
    except:
        return None

if __name__ == '__main__':
    site = "https://en.wikipedia.org/w/index.php?title=List_of_S%26P_500_companies&oldid=697200065"
    df = scrape_list(site)
    print df