import os
filepath=r"C:\Users\Administrator\Desktop\linux\linux4.15\fs\f2fs\data.c"
characters=r"__is_cp_guaranteed"
def search_special_string(path):
	if os.path.isdir(path) :
		for t in os.listdir(path):
			search_special_string(os.path.join(path,t))
	else:
		with open(path,mode="r",encoding='UTF-8') as f :
			lines = f.readlines()
			for i in range(len(lines)) :
				# print(lines[i])
				if characters in lines[i] :
					print("lineno:%d,at %s"%(i,path))
			
search_special_string(filepath)
print("finished.")