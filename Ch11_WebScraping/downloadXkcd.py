#! Python 3
import os, requests, bs4

# Create the directory where the file is going to be saved
os.makedirs('xkcd', exist_ok=True)
url = 'http://xkcd.com'

while not url.endswith('#'):
    print('Downloading from %s' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')[0]

    if comicElem == []:
        print('Could not locate the image...')
    else:
        try:
            comicUrl = 'http:' + comicElem.get('src')
            res = requests.get(comicUrl)
            res.raise_for_status()

        except requests.exceptions.MissingSchema:
            # Go to next page if any issues arise
            prevElem = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevElem
            continue
        


