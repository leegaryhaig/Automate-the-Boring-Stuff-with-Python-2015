#! Python3
# You can save a web page to a file on your hard drive with the standard open() and write() method. There are some
# slight differences though. First, you must open the file in write binary mode by passing the string 'wb' as the second
# argument to open(). Even if the page is in plaintext, such as Romeo and Juliet. you need to write binary data instead
# of text data in order to maintain Unicode encoding.

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb') #wb stands for write in binary
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()


# The res objects raise_for_status() method will throw an exception and end the program is something goes wrong with the
# program. the iter_content() method returns 'chunks' of content on each iteration through the loop, and since we
# specified 'wb' it will return one hundred thousand bytes.