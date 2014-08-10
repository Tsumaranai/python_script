#!/usr/bin/env python


import os
import sys
import hashlib
import math

pos = [None] * 10
en_code = 'e48d316ed573d3273931e19f9ac9f9e6039a4242'
N = 9
passwd = 'zWp8LGn01wxJ7'


def jud(x,  lvl):

	for i in xrange(1, lvl):

		if x == pos[i] or abs(lvl - i) == abs(x - pos[i]):

			return False


	return True



def queen(lvl):

	if lvl > N :
		
		queen_pos = ''
		for i in xrange(1, lvl):
			queen_pos += '%d'%pos[i]

		print pos
		if hashlib.sha1(passwd + queen_pos + '\n').hexdigest() == en_code:

			print queen_pos

		return 
			

	for i in xrange(1, N + 1):
		
		if lvl == 1 or jud(i, lvl):

			pos[lvl] = i

			queen(lvl + 1)
			
			pos[lvl] = None

	return 	







def main():

	queen(1)


if __name__ == '__main__':

	main()










	
