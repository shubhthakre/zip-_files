
from zipfile import ZipFile 


file_name = "MASM64.zip"


with ZipFile(file_name, 'r') as zip: 
	
	zip.printdir() 

	# extracting all the files 
	print('Extracting all the files now...') 
	zip.extractall() 
	print('Done!') 
