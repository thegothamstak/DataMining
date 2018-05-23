'''	
	Python code to open files with different extensions, rename them and save them.

	Author : Shripad Tak
	Date : 23rd May 2018
'''
#	Importing libraries
import os				#To traverse through the OS file system
from PIL import Image 	#To open Image files

#	Function for image files
def forImageFiles(file):

	imageFile = Image.open(file)	#Image object is created in imageFile
	imageFile.show()				#Will open the image file

	#	To rename the image file
	imageFile.save(input('Enter new name for imageFile : '))

#	Function for text files
def forTextFiles(file):

	textFile = open(file, 'r')		#File object is created in textFile
	textContent = textFile.read()	#File content is stored in textContent
	textFile.close()				#Close file object

	print('Content of the file '+file+' is :\n')	#Print fileContent
	print(textContent)

	#	Open another file (in append mode for now) to store the data with new name. (RENAME)
	tFile = open(input('Enter new name for textFile : '), 'a')	
	tFile.write(textContent)
	tFile.close()

#	Changing directory to where the files are
os.chdir('/home/stak/Pictures')

#	Name of the file to perform operations on
filename = 'IAmRoot.png'

#	Operations for image files based on extensions
if(filename.split(".")[-1] == 'png' or filename.split(".")[-1] == 'jpg' or filename.split(".")[-1] == 'jpeg'):
	forImageFiles(filename)

#	Operations for text files based on extensions
elif(filename.split(".")[-1] == 'txt'):
	forTextFiles(filename)

#	Program under construction
else:
	print('Program under construction. Sorry !')
