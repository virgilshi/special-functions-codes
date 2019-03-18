import os
filepath=r"/Users/shiliu/Desktop/leveldb_fix/leveldb"
characters=r"/tmp"
def search_special_string(path):
	if os.path.isdir(path) :
		for t in os.listdir(path):
			search_special_string(os.path.join(path,t))
	else:
		import re
		if re.search("(\.cc|\.h)$",path) is not None :
			# print(path)
			with open(path,mode="r") as f :
				
				lines = f.readlines()
				for i in range(len(lines)) :
					# print(lines[i])
					if characters in lines[i] :
						print("lineno:%d,at %s"%(i,path))
				
			
			
search_special_string(filepath)
print("finished.")