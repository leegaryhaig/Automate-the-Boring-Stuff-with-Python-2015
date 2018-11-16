#! Python 3 - Create a script that will take a search string and open up several tabs of the highest search results.

import webbrowser, sys, bs4, requests

#TODO: Get the CMD line arg and request search page 'https://www.google.com/search?q=SEARCH_TERM_HERE'

res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
print(res)
print('\n\n\n')
#TODO: Find all the results using bs4 to extra top search results (select method) link exists in h3 class="r"
soup = bs4.BeautifulSoup(res.text)
print(res.text)

#TODO: Open Web Browsers for each results.
linkElem = soup.select('.r a' ) # stores the value a element in r class in a list
numOpen = min(5, len(linkElem))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElem[i].get('href'))
