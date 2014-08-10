#!/usr/bin/env python


import os


def printn(x , th):

	i = x % th

	if x <= th:

		print i
		return

	printn(x / th, th)

	print i





printn(85165 , 26)
