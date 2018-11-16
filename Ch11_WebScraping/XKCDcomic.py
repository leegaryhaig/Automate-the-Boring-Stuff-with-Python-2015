# Python 3
# Download pages with the requests module.
# Find the URL of the comic image for a page using Beautiful Soup.
# Download and save the comic image to the hard drive with iter_content().
# Find the URL of the Previous Comic link, and repeat.

import requests, bs4, webbrowser, os

# Set URL and Create the directory where the Files are to be saved
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Requests the URL
    res = requests.get(url)
    res.raise_for_status()

    # parses HTML
    soup = bs4.BeautifulSoup(res.text)

    # look for the img element
    imgElement = soup.select('#comic img')

    if imgElement == []:
        print('Sorry image not found..%s' % url)
    else:
        try:
            imgUrl = 'http:' + imgElement[0].get('src')
            res = requests.get(imgUrl)
            res.raise_for_status()
            imgFile = open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()
        except requests.exceptions.MissingSchema:
            # Skip this page
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue

    # Go to the next page
    prevElem = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevElem.get('href')

    print('Finding Next page...%s' % url)




