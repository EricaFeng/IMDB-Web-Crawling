# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib
from bs4 import BeautifulSoup


urlLink='https://www.imdb.com/title/tt4912910/reviews?ref_=tt_urv'
urlPrefix='https://www.imdb.com/title/tt4912910/reviews/_ajax?paginationKey='

rFile = open("userreviews.txt","w")
while True:

    print urlLink
    html = urllib.urlopen(urlLink)

    # Initialize a BeautifulSoup object
    contentBs = BeautifulSoup(html)

    for reviews in contentBs.find_all('div', class_='text show-more__control'):
        rFile.write(reviews.text)
        rFile.write("\n")
    if contentBs.find('div', {'class': 'load-more-data'}):
        nextKey = contentBs.find('div', {'class': 'load-more-data'})['data-key']
        urlLink = urlPrefix + nextKey

    else:
        break

print "Done"
