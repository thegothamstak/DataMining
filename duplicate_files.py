'''
	Python code to find duplicate files in your file system using md5 checksum.

	Author : Shripad Tak
	Date : 22nd May 2018

	PROGRAM UNDER CONSTRUCTION !!! MINOR ERROR !!! COMMENTS WILL BE PUT AFTER SMOOTH EXECUTION !!!
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
