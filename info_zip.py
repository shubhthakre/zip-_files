# importing required modules 
from zipfile import ZipFile 
import datetime 

# specifying the zip file name 
file_name = "MASM64.zip"


with ZipFile(file_name, 'r') as zip: 
	for info in zip.infolist(): 
			print(info.MASM64) 
			print('\tModified:\t' + str(datetime.datetime(*info.date_time))) 
			print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)') 
			print('\tZIP version:\t' + str(info.create_version)) 
			print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
			print('\tUncompressed:\t' + str(info.file_size) + ' bytes') 
