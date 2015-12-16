import urllib2
from urlparse import urlparse
from os.path import splitext, basename
import hashlib
from bs4 import BeautifulSoup, SoupStrainer
from random import randint


source = "http://i.imgur.com"			# base site URL
savePath = "./randomImgur"			# path to save images to
randomChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


# Generate a random, five character filename.

fileName=""
for i in range(0,5):
	fileName += randomChars[randint(0,61)]

fullPath = source + "/" + fileName
page = urllib2.urlopen(fullPath)
page = BeautifulSoup(page)

for imageFound in page.findAll('img'):
	if fileName in imageFound['src']:
		print imageFound['src']
		image = urllib2.urlopen('http:'+imageFound['src'])	
		data = image.read()
		disassembled = urlparse(imageFound['src'])
	        filename, file_ext = splitext(basename(disassembled.path))
		saveTo = savePath + "/" + filename + file_ext 
       	 	print saveTo
        	fileToSave = open(saveTo, 'wb')
        	fileToSave.write(data)
        	fileToSave.close()	
