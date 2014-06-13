import os

def hexdump(s):

	for b in xrange(0, len(s), 16):
		lin = [c for c in s[b : b + 16]]
		hdata = ' '.join('%02X' % ord(c) for c in lin)
		pdata = ''.join('%s' % (c if 32 <= ord(c) <= 126 else '.') for c in lin)

		print '%08x: %-48s %s' % (b, hdata, pdata)
		
		
		
def main():
    
    file_name = raw_input('Inuput the text path\n')
    fh = open(file_name,'rb')
    text = fh.read()
    hexdump(text)
	
	
	
if __name__ == '__main__':

	main()
# What Did I Learn? :
#s[x:y] element in s xth to yth
#join : join the element in list with ' '.join
#'xxxxxxx%xsd..' % (aaa) %num, num means length if 0num fullfil the blank with 0
# if num is positive, forth fullfil if negetive before the item
#xrange (from , to, gap)
#pay attention on lin, new ideas
#The three act operation, is so defferent with C, x if condition else y is equal to condition : x ? y in C
#Good Luck