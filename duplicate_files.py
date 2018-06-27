'''
	Python code to find duplicate files in your file system using md5 checksum.

	Author : Shripad Tak
	Date : 22nd May 2018

	PROGRAM UNDER CONSTRUCTION !!! MINOR ERROR !!! COMMENTS WILL BE PUT AFTER SMOOTH EXECUTION !!!
'''
'''
import os
import hashlib
import csv

filename = 'test1.txt'
cksum_val = hashlib.md5(open(filename,'rb').read()).hexdigest()
filen, file_extension = os.path.splitext(filename)

csv_data_list = [['Name','Size','Location','Duplicate']]
row_data_list = []

dirs_list = ['Desktop','Documents','Downloads','Music','Pictures','Videos']

duplicate = 'No'

for direc in dirs_list:
	print(direc)
	for folders, subfolders, filenames in os.walk('/home/stak/'+direc):
		print(subfolders)
		for file in filenames:
			file_path = os.path.abspath(file)

			c_val = hashlib.md5(open(file_path,'rb').read()).hexdigest()
			if(c_val == cksum_val and os.path.abspath(filename) != os.path.abspath(file)):
				if(os.path.abspath(filename) != os.path.abspath(file)):
					duplicate = 'Yes'
				if(os.path.abspath(filename) == os.path.abspath(file)):
					duplicate = 'Original'


			row_data_list.append(file)
			row_data_list.append(os.path.abspath(file))
			row_data_list.append(os.path.getsize(os.path.abspath(file)))
			row_data_list.append(duplicate)

			csv_data_list.append(row_data_list)
			print(row_data_list)

print(csv_data_list)

csv_file = open('duplicate.csv', 'w', newline = '')
csv_writer = csv.writer(csv_file)

for l in csv_data_list:
	csv_writer.writerow(l)

csv_file.close()
'''

import os
import hashlib
import csv

def createFileList(path, file_list):
	content_list = os.listdir(path)
	for i in content_list:
		row_file_list = []
		if(i[0] != '.'):
			if(os.path.isdir(os.path.join(path, i))):
				createFileList(os.path.join(path, i), file_list)
			if(os.path.isfile(os.path.join(path, i))):
				checksum_val = hashlib.md5(open(os.path.join(path, i),'rb').read()).hexdigest()
				size = os.path.getsize(os.path.join(path, i))

				row_file_list.append(i)
				row_file_list.append(path)
				row_file_list.append(size)
				row_file_list.append(checksum_val)

				#print(row_file_list)
				file_list.append(row_file_list)

def checkDuplicate(file_list, file_duplicate_list):
	for i in file_list:
		row_list = []
		row_list.append(i[0])
		row_list.append(i[1])
		row_list.append(i[2])
		row_list.append(i[3])
		for j in file_list:
			duplicate_list = []
			duplicate_flag = False
			if(i != j):
				if(i[3] == j[3]):
					duplicate_flag = True
					duplicate_list.append(j[0])

		row_list.append(duplicate_flag)
		row_list.append(duplicate_list)

		file_duplicate_list.append(row_list)			

file_list = [['Name','Path','Size','CheckSum']]
file_duplicate_list = [['Name','Path','Size','CheckSum','Duplicate','Duplicate Files']]

os.chdir('/home/stak')
path = os.getcwd()

createFileList(path, file_list)

print(file_list)
