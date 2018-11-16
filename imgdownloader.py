#! Python 3
import requests, bs4, os

# Check to make sure path exists
url = "https://unsplash.com/wallpaper/1339119/mac-wallpapers"
os.makedirs('MacWallpapers', exist_ok=True)

res = requests.get(url)
res.raise_for_status()
i = 0

soup = bs4.BeautifulSoup(res.text, features="html.parser")
imgClass = soup.select('a[class="_2Mc8_"]')
imgLink = 'https://unsplash.com' + imgClass[0].get('href')
print(imgLink)

while i < len(imgClass):
    # Request the image
    print(i)
    imgLink = 'https://unsplash.com' + imgClass[i].get('href') + '/download?force=true'
    print('Requesting img from...%s' % imgLink)

    # Get Author Name
    authorString = imgClass[i].get('title')
    authorList = authorString.split()
    author = ' '.join(authorList[-2:])

    try:
        # Download the image
        print('Downloading img...%s' % author)
        res = requests.get(imgLink)
        res.raise_for_status()

    except requests.exceptions.MissingSchema:
        # Skip this image
        print('Cant Download img...%s' % author)
        i += 1
        continue

    # Save the image the MacWallpapers
    print('Saving Image to MacWallpapers')
    imgFile = open(os.path.join('MacWallpapers', str(i) + author + '.jpg'), 'wb')
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)
    imgFile.write(chunk)
    imgFile.close()

    # Increment i
    i += 1

print('Done')







