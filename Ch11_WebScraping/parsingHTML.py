#! Python 3
import bs4
import requests

# Creating a Beautiful Soup object from HTML

res = requests.get('http://nostarch.com/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
elems = noStarchSoup.select('div')  # Uses bs4 to search noStarchSoup Object for the select div tags
print(type(elems[1]))
print(len(elems))
print(type(elems[1].getText()))
print(elems[0].attrs)
print('\n\n')

pElems = noStarchSoup.select('p')  # Search
print('Paragrah Element' + str(pElems))
print('\n')
print('Paragrah Element' + str(pElems[0]))  # returns the first span element found
print(pElems[0].getText())
print('\n')
print('Paragrah Element' + str(pElems[1]))
print(pElems[1].getText())
print('\n\n')
# Getting Data from an elements attributes
spanElem = noStarchSoup.select('span')[0]  # Another way of returning the first span element found
print('Span Element: ' + str(spanElem))
print(spanElem.get('class'))
print(spanElem.get('notarealclass'))
print(spanElem.attrs)