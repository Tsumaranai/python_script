import os
import sys

string = ''

def st(s):

	global string

	for b in xrange(0,len(s)):

		x = s[b]

		if ord('a') <= ord(x) <= ord('z'):

			 if (ord(x) - 13) < ord('a'):
			 	x = chr(ord(x) + 26)

			 x = chr(ord(x) - 13)

		if ord('A') <= ord(x) <= ord('Z'):

			 if (ord(x) - 13) < ord('A'):
			 	x = chr(ord(x) + 26)

			 x = chr(ord(x) - 13)

		string += x



def main():

	text = raw_input ('filename: \n')

	#fh = open(filename,'rb')

	#text = fh.read()

	st(text)

	print string

if __name__ == '__main__':
	main()
