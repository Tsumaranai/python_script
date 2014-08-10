#!/usr/bin/env python


import os
import sys



deepest = 1

in_order_raw = 'T, b, H, V, h, 3, o, g, P, W, F, L, u, A, f, G, r, m, 1, x, J, 7, w, e, 0, i, Q, Y, n, Z, 8, K, v, q, k, 9, y, 5, C, N, B, D, 2, 4, U, l, c, p, I, E, M, a, j, 6, S, R, O, X, s, d, z, t'

post_order_raw = 'T, V, H, o, 3, h, P, g, b, F, f, A, u, m, r, 7, J, x, e, w, 1, Y, Q, i, 0, Z, n, G, L, K, y, 9, k, q, v, N, D, B, C, 5, 4, c, l, U, 2, 8, E, I, R, S, 6, j, d, s, X, O, a, M, p, W, t, z'


in_tree_deep = [1] * 62


in_order = in_order_raw.split(', ')
post_order = post_order_raw.split(', ')
post_order.reverse()
#print in_order


#print post_order



for ele in post_order:


	index = in_order.index(ele)
#	print index	
	pos = index
	while pos < 61 and in_tree_deep[index]  == in_tree_deep[pos + 1]:
		
		pos += 1
#		print pos
		in_tree_deep[pos] += 1
	
		'''
		if pos == 61 and (in_tree_deep[pos - 1] - 1) ==  in_tree_deep[pos]:

			in_tree_deep[pos] += 1
		'''


	pos = index

	while pos > 0 and in_tree_deep[index] == in_tree_deep[pos - 1]:

		pos -= 1
#		print pos
		in_tree_deep[pos] += 1

	'''		
	if pos == 0 and (in_tree_deep[pos + 1] -1) == in_tree_deep[pos]:
			in_tree_deep[pos] += 1
	'''

		


last = [None]*62
k = 0
for v in in_tree_deep:
	
	last[k] = [v, in_order[k]]
	k += 1

print max(in_tree_deep)

print min(in_tree_deep)


print last
	
