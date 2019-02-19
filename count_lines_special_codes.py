import os
def getdir_linecount(pathname):
	if os.path.isfile(pathname):
		try :
			with open(pathname,mode="r",encoding="utf8") as f :
				return len(f.readlines())
		except UnicodeDecodeError :
			return 0
			pass
	else :
		files = os.listdir(pathname)

		count_line = 0
		for t in files :
			t = os.path.join(pathname,t)
			count_line += getdir_linecount(t)
		return count_line
		

print(getdir_linecount(r"C:\Users\Administrator\Desktop\fio"))