from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r)
#print type(soup)
#print soup.prettify()[0:3000]
#print soup.prettify()[28700:30500]
letters = soup.find_all("div", class_="ec_statements")

lobbying = {}
for element in letters:
    lobbying[element.a.get_text()] = {}


letters[0].a["href"]
prefix = "www.aflcio.org"

for element in letters:
    lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]
for element in letters:
    date = element.find(id="legalert_date").get_text()
    lobbying[element.a.get_text()]["date"] = date


for item in lobbying.keys():
    print item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n" 
