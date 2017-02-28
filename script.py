import os
from os import listdir
from os.path import isfile, join
import shutil
from shutil import copyfile

mydir = "/home/anuj/Ego/"
dest_dir = "/home/anuj/mydata/"
#onlyfiles has the list
alldir = [os.path.join(mydir,o) for o in os.listdir(mydir) if os.path.isdir(os.path.join(mydir,o))]

# for i in alldir:
	# print i
c = 0
mydict = {}
mydict ["DASDAS"] = 1
for i in alldir:
	path =  i + "/"

	onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
	# print onlyfiles
	# print i
	
	
	for file in onlyfiles:
		#remove _ from file names		
		filepath = path + file		
		
		file1 = file.replace(".mp4","")
		file1 = file1.replace("_","")
		# print file1

		key = file1
		# mydict{file} = 1
		if key in mydict: 
			itr = mydict[key]
			itr = itr + 1
			mydict[key] = itr
			dest_name = file1 + str(itr) + ".mp4"

		else:
			mydict[key] = 1
			dest_name = file1 + "1.mp4"
			# shutil.copy(filepath,dest_dir)

	
		# shutil.copy(filepath,buffer_dir)
		# os.rename(buffer_dir+file, buffer_dir+dest_name)
		# shutil.copy(buffer_dir+dest_name,dest_dir)
		# os.remove(buffer_dir+dest_name)

		shutil.copy(filepath,dest_dir)
		os.rename(dest_dir+file, dest_dir+dest_name)
		print filepath,
		print "-----",
		print dest_dir+dest_name
		# break

		# print buffer_dir+dest_name
		# print file
		c = c + 1


onlyfiles = [f for f in listdir(dest_dir) if isfile(join(dest_dir, f))]
for file in onlyfiles:
	file1 = file.replace("1","")
	os.rename(dest_dir+file,dest_dir+file1)