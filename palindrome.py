#!/usr/bin/env python

import os
import sys


cat_carry = 'catac'

str_cat = ''

def rcs(case, num):
	
	global str_cat

	if num == 5:
		print str_cat
		return

	if case == 0:
		str_cat += cat_carry[num]
	#else:
	#	str_cat += cat_carry[num]
		if num == 4:
			cmd = 'curl http://fun.coolshell.cn/' + str_cat + '.html | grep 404'
			print cmd
			os.system(cmd)
			return
		rcs(0, num + 1)
		str_cat = str_cat[:num + 1]
		rcs(1, num + 1)
		str_cat = str_cat[:num + 1]
	else:
		str_cat +=  chr(ord(cat_carry[num]) - 32)
		if num == 4:
			cmd = 'curl http://fun.coolshell.cn/' + str_cat + '.html | grep 404'
			print cmd
			os.system(cmd)
			return
		rcs(0, num + 1)
		str_cat = str_cat[:num + 1]
		rcs(1, num + 1)
		str_cat = str_cat[:num+1]



def main():
	
	global str_cat
	rcs(0, 0)
	str_cat = ''
	rcs(1, 0)

if __name__ == "__main__":
	main() 
