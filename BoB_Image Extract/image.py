import os
import sys
import pytsk3
import pyewf
import csv
import datetime
import re

# Make CSV File
make_csv = open("report.csv", 'w')
make_csv.write('"Modified Time","Accessed Time","Created Time","Entry Edited Time","File Extension","File Size (Byte)","Full Path"\n')
report_csv = csv.writer(make_csv, quoting=csv.QUOTE_ALL)

# EWF File Type for option
class ewf_Img_Info(pytsk3.Img_Info):
	
	def __init__(self, ewf_handle):
		self._ewf_handle = ewf_handle
		super(ewf_Img_Info, self).__init__(url="", type=pytsk3.TSK_IMG_TYPE_EXTERNAL)
	
	def close(self):
		self._ewf_handle.close()

	def read(self, offset, size):
		self._ewf_handle.seek(offset)
		return self._ewf_handle.read(size)

	def get_size(self):
		return self._ewf_handle.get_media_size()

# Main Function

def image_main(directory_object, parent_path):
	
	for image_entry in directory_object:
		
		if image_entry.info.name.name in [".", ".."]:
			continue

		try:
			file_type = image_entry.info.meta.type

		except:
			print "[!] Error!"
			continue

		try:
			# Extract File Info : https://github.com/py4n6/pytsk/wiki/Development
			output_path = './%s/%s/' % ("extract_files",'/'.join(parent_path))

			if parent_path == []:
				file_path = '%s/%s' % ("extract_files",image_entry.info.name.name)
			else:
				file_path = '%s/%s/%s' % ("extract_files","/".join(parent_path),image_entry.info.name.name)

			if file_type == pytsk3.TSK_FS_META_TYPE_DIR:

				sub_directory = image_entry.as_directory()
				parent_path.append(image_entry.info.name.name)
				image_main(sub_directory, parent_path)
				parent_path.pop(-1)

			elif file_type == pytsk3.TSK_FS_META_TYPE_REG and image_entry.info.meta.size != 0:

				file_data = image_entry.read_random(0, image_entry.info.meta.size)

				modified_time = datetime.datetime.fromtimestamp(image_entry.info.meta.mtime)
				accessed_time = datetime.datetime.fromtimestamp(image_entry.info.meta.atime)
				created_time = datetime.datetime.fromtimestamp(image_entry.info.meta.crtime)
				edited_time = datetime.datetime.fromtimestamp(image_entry.info.meta.ctime)

				cv_modified_time = modified_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
				cv_accessed_time = accessed_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
				cv_created_time = created_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
				cv_edited_time = edited_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
				
				if os.path.splitext(file_path)[1] == "":
					file_extension = "None Extension"

				else:
					file_extension = os.path.splitext(file_path)[1]

				file_size = int(image_entry.info.meta.size)

				# Read option.ini file
				# http://stackoverflow.com/questions/16382311/python-using-string-as-condition-in-if-statement
				
				if eval(option):
					# Extract File					
					if not os.path.exists(output_path):
						os.makedirs(output_path)

					print "[-] Extract file name : %s" % str(image_entry.info.name.name)

					extract_files = open(output_path + image_entry.info.name.name, 'w')
					extract_files.write(file_data)
					extract_files.close

					# Write to CSV File
					report_csv.writerow([cv_modified_time,cv_accessed_time, cv_created_time, cv_edited_time, file_extension, file_size, file_path])

				else:
					continue

			elif file_type == pytsk3.TSK_FS_META_TYPE_REG and image_entry.info.meta.size == 0:
				continue

		except:
			print "Error!"
			continue

# Main Page
print "[*] KITRI BoB Image Extractor"
image_file = raw_input("[!] Input Image file path : ")
image_extension = os.path.splitext(image_file)[1]

# E01 Image Type
if (image_extension == ".E01"):
	file_names = pyewf.glob(image_file)
	ewf_handle = pyewf.handle()
	ewf_handle.open(file_names)
	image_handle = ewf_Img_Info(ewf_handle)

# RAW Image Type
elif (image_extension == ".raw"):
	image_handle = pytsk3.Img_Info(url=image_file)

partition_table = pytsk3.Volume_Info(image_handle)

option_file = open("option.ini", 'r')
option = option_file.read()

for partition in partition_table:

	try:
		filesystem_object = pytsk3.FS_Info(image_handle, offset=(partition.start*512))

	except:
		continue

	# File System Info Detection
	print "\n[+] File System Type Detected", filesystem_object.info.ftype
	directory_object = filesystem_object.open_dir(path="/")
	image_main(directory_object, [])

print "\n[!] Extract files and complete report generation based on option.ini"