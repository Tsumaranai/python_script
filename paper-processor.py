#conding=utf-8#
import os
import re
import sys
import codecs
import types
#reload(sys)
#sys.setfaultencodeing('utf-8')

text_file_path = 'E:\\info\\NY.txt'

en_paper_dir = 'E:\\info\\英文'
zh_paper_dir = 'E:\\info\\中文'

def main():

	file_array_en = os.listdir(en_paper_dir.decode('utf-8'))
	file_array_zh = os.listdir(zh_paper_dir.decode('utf-8'))
	text_file = open( text_file_path, 'a')

	for i in file_array_en:
		try:
			pa = re.compile('\d+')
			year = pa.search(i).group(0)
			pa = re.compile('(?<=_).+')
			topic = pa.search(i).group(0)

			src_file_path = en_paper_dir.decode('utf-8') + u'\\' + i
			dst_file_path = en_paper_dir.decode('utf-8') + u'\\' + topic

		#if os.path.isfile(src_file_path):
		#	print 'YES~!\n'
		#else:
		#	print 'NaaaaaaaaaaaaaaaaaaO~!\n'

			os.rename( src_file_path , dst_file_path)
			text_file.write(topic + ' , ' + year + '\n')
		except:
			p = 0

	text_file.close()



	text_file = codecs.open( text_file_path, 'a', 'utf-8')
	for i in file_array_zh:

		pa = re.compile('\d+')
		year = pa.search(i).group(0)
		pa = re.compile('(?<=_).+')
		topic = pa.search(i).group(0)
		
		#print type(zh_paper_dir.decode('utf-8'))
		src_file_path = zh_paper_dir.decode('utf-8') + u'\\' + i
		dst_file_path = zh_paper_dir.decode('utf-8') + u'\\' + topic

		if os.path.isfile(src_file_path):
			print 'YES~!\n'
		else:
			print 'NaaaaaaaaaaaaaaaaaaO~!\n'

		os.rename( src_file_path , dst_file_path)

		text_file.write(topic)
		text_file.write(' , ' + year + '\n')


		
	text_file.close();



if __name__ == '__main__':
	main()


