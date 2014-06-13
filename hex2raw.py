import sys
import os
import re

ascii_string = ''

def hex2raw(s):

	global ascii_string
	hex_str_array = s.split(' ')
	#print hex_str_array

	for i in hex_str_array:
		t = int(i,base=16)

		ascii_string += chr(t)



def main():

	global ascii_string
	string = raw_input("input:\n")

	hex2raw(string)

	print ascii_string

	

if __name__ == '__main__':
	main()