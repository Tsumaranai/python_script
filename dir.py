import os

def mkdir(path):

	if os.path.exists(path):

		print 'It exists\n'
		return False
	else:
		os.makedirs(path)
		print 'create ' + path +'successfully\n'
		return True



mkpath = 'D:\\douban'

mkdir(mkpath)
