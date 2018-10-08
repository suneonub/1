## /lib/usr/python

## Kirnath x ZeroByte.ID Recoded By Revandri


import random

import string

import requests

import time

import sys

import urllib2


base = "BLMOII"

berapa = int(raw_input("[+] Butuh Berapa Jink?: "))

if berapa > 20000000:

	print "[+] MARUK GOBLOK!"

	sys.exit()

def gene(size=4, chars=string.ascii_uppercase + string.digits):

	return ''.join(random.choice(chars) for _ in range(size))

for i in range(berapa):

	result = base+gene()

	print result

	file = open('Voc.txt', 'a')

	file.write(result+'\n')

cek = str(raw_input("[+] di cek g jink(y/n): "))

if cek == "y":

	print "[+] Muka Lo Jelek moga aja hoki!"

	time.sleep(2)

	files = open('Voc.txt', 'r')

	for line in files:

		pisah = line.split('\n')

		a = pisah[0]

		cek = requests.get("http://api-siptruk.c9users.io/vocbl.php?code={}".format(a))

		reason = cek.text

		if "[VALID]" not in reason:

			print "DIE | ",a

		else:

			print "LIVE | ",a
			print reason
			time.sleep(2)
			file = open('live.txt', 'a')
			file.write(reason+'\n')

else:

	print "[+] OK BABI! W KELUAR"

	sys.exit(4)


