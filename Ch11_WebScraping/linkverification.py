#! Python 3
import requests, sys, bs4, os


# Download page and store links in linklist
while sys.argv[1]:
    url = sys.argv[1]
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, features="html.parser")
    i = 0
    linksList = soup.select('a')

    # Create a directory for err message to go
    os.makedirs('linkError', exist_ok=True)

    errfile = open(os.path.join('linkError', 'linkError.txt'), 'w')


    while i < len(linksList):
        link = linksList[i].get('href')

        if link.startswith('/'):
            try:
                link = url + link
                print('Checking Link....%s' % link)
                res = requests.get(link)
                res.raise_for_status()
                i += 1
                continue
            except requests.exceptions.RequestException as e:
                errfile.write("Error connecting to " + link + "\nReason:" + str(e) + "\n\n")
                print("Error logged in linkError.txt:" + str(e))
                i += 1
                continue

        else:
            try:
                print('Checking Link...%s' % link)
                res = requests.get(link)
                res.raise_for_status()
                i += 1
                continue
            except requests.exceptions.RequestException as e:
                errfile.write("Error connecting to " + link + "\nReason:" + str(e) + "\n\n")
                print("Error logged in linkError.txt:" + str(e))
                i += 1
                continue
    print('Done checking the links on this page')
    system.exit(1)
print('Please provide URL in command line')