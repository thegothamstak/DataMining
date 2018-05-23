'''	
	Python code to find duplicate contacts in our phone contact list.
	The contatcs were imported from the contacts application from my android phone in vcf format.
	1. To obtain that, open Contacts application.
	2. Tap on the 3 dots on the top right corner of the screen.
	3. Go to Import/Export contacts.
	4. Tap on Export to storage and click OKAY.
	5. You will find the file on your internal storage in Contacts directory.

	Author : Shripad Tak
	Date : 23rd May 2018
'''
#	Importing libraries
import os		#	To traverse through the OS file system
import pprint	#	To pretty print the dictionary output

#	Changed directory to where the contact file is saved in the file system
os.chdir('/home/stak/Documents/DMA')

#	Returns the file object
file = open('contacts.vcf','r')

#	Converts each line in the file as separate list and stores in raw_contact_list
raw_contacts_list = file.readlines()

#	Closing the file object
file.close()

#	Declaring empty dictionary in which all contacts will be saved after data cleansing
contacts_dict = {}

#	Loop to iterate through each list (line) of the file that was stored in raw_contacts_list
for record in raw_contacts_list:
	
	#	BEGIN and END hold one complete block of contact record
	if('BEGIN' in record):
		name_key = ''		#	Initialized as '' to store new name at each iteration	
		num_value = []		#	Initialized as '' to store new contact list at each iteration

	#	Contact name string (inside the list) includes FN: | So used to locate the contact name.
	if('FN' in record):
		name = record
		name = name.replace('FN:','')	#	To clean the string of anything other than contacgt name (i.e FN:)

		name_key = name[:-1]			#	Stored in name_key to clean \n from the name

	#	Contact number string (inside the list) includes TEL;VOICE;PREF: or TEL;CELL:| So used to locate the contact number.
	if('TEL;VOICE;PREF' in record or 'TEL;CELL' in record):
		
		#	To cleanse the number of anything other than numeric data
		number = record
		number = number.replace('TEL;VOICE;PREF:','')
		number = number.replace('TEL;CELL:','')
		number = number.replace('-','')
		number = number.replace('+91','')

		num_value.append(number[:-1])	#	Stored in num_key to clean \n from the number

	#	Marks the end of the contact block
	if('END' in record):
		if(num_value == []):			#	Validation to not store blank contact as it creates ambiguity
			continue
		else:
			contacts_dict.setdefault(name_key, num_value)	#	Contacts stored in contact dictionary

#	Printing the Contact dictionary
print('\nContact dictionary :\n')
pprint.pprint(contacts_dict)

#	Initializing the dictionary that will contain contact names and its duplicates
duplicate_dict = {}

#	Will iterate through contact dictionary to find duplicates 
for key in contacts_dict.keys():
	contact_name = key  				#	Taking key of contacts_dict as contact name

	dupli_list = []						#	Initializing the dupli_list which will store all the contact names that are duplicates
	
	#	Iterate through contact dictionary to check with each contact
	for check_key in contacts_dict.keys():

		if(key == check_key):			#	To validate for refrain from checking with same contact
			continue
		else:
			#	If contact number is same it will be stored in dupli_list as duplicate
			if(contacts_dict[key] == contacts_dict[check_key]):
				dupli_list.append(check_key)
	
	#	Adding each record to duplicate_dict 
	duplicate_dict.setdefault(key, dupli_list)

#	Printing duplicate dictionary
print('\nDuplicate Dictionary :\n')
pprint.pprint(duplicate_dict)