import os.path
import sys
import pytsk3
import pyewf
import datetime
import argparse
import re

imagefile = ""

argparser = argparse.ArgumentParser(description='Extract the Files')

argparser.add_argument('-f','--file', dest='imagefile', action='store', type=str, default=None, required=True, help='Imagefile name & path')
argparser.add_argument('-e', '--extract', dest='extract', action="store_true", default=False, required=False, help='extract path')

class ewf_Img_Info(pytsk3.Img_Info):

	def __init__(self, ewf_handle):
		self._ewf_handle = ewf_handle
		super(ewf_Img_Info, self).__init__(
			url="", type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

	def close(self):
		self._ewf_handle.close()

	def read(self, offset, size):
		self._ewf_handle.seek(offset)
		return self._ewf_handle.read(size)

	def get_size(self):
		return self._ewf_handle.get_media_size()

def directoryRecurse(directoryObject, parentPath):
	for entryObject in directoryObject:
		if entryObject.info.name.name in [".", ".."]:
			continue

	try:

		f_type = entryObject.info.meta.type

	except:

		print "Cannot retrieve type of",entryObject.info.name.name
		continue

	try:

		filepath = '/%s/%s' % ('/'.join(parentPath),entryObject.info.name.name)
		outputPath ='./%s/%s/' % (str(partition.addr),'/'.join(parentPath))

		if f_type == pytsk3.TSK_FS_META_TYPE_DIR:

			sub_directory = entryObject.as_directory()
			parentPath.append(entryObject.info.name.name)
			directoryRecurse(sub_directory,parentPath)
			parentPath.pop(-1)

			print "Directory: %s" % filepath


		elif f_type == pytsk3.TSK_FS_META_TYPE_REG and entryObject.info.meta.size != 0:

            if args.extract == True:

				if not os.path.exists(outputPath):

					os.makedirs(outputPath)

				extractFile = open(outputPath+entryObject.info.name.name,'w')
				extractFile.write(filedata)
				extractFile.close

        elif f_type == pytsk3.TSK_FS_META_TYPE_REG and entryObject.info.meta.size == 0:

            wr.writerow([int(entryObject.info.meta.addr),'/'.join(parentPath)+entryObject.info.name.name,datetime.datetime.fromtimestamp(entryObject.info.meta.crtime).strftime('%Y-%m-%d %H:%M:%S'),int(entryObject.info.meta.size),"d41d8cd98f00b204e9800998ecf8427e","da39a3ee5e6b4b0d3255bfef95601890afd80709"])

	except IOError as e:

		print e
		continue

args = argparser.parse_args()
image_name = "".join(args.imagefile)
file_ext = os.path.splitext(image_name)
print str(image_name)
print file_ext[1]

if file_ext[1] == ".raw":

	imagehandle = pytsk3.Img_Info(str(image_name))
	partitionTable = pytsk3.Volume_Info(imagehandle)

	for partition in partitionTable:
		print partition.addr, partition.desc, "%ss(%s)" % (partition.start, partition.start * 512), partition.len

	filesystemObject = pytsk3.FS_Info(imagehandle, offset=65536)
	fileobject = filesystemObject.open("/$MFT")

	print "File Name:",fileobject.info.name.name
	print "File Creation Time:", fileobject.info.meta.crtime

	outFileName = str(partition.addr)+fileobject.info.name.name

	print outFileName

	outfile = open(outFileName, 'w')
	filedata = fileobject.read_random(0,fileobject.info.meta.size)
	outfile.write(filedata)
	outfile.close

if file_ext[1] == ".E01":

	filenames = pyewf.glob(str(image_name))
	ewf_handle = pyewf.handle()
	ewf_handle.open(filenames)
	imagehandle = ewf_Img_Info(ewf_handle)
	partitionTable = pytsk3.Volume_Info(imagehandle)

	for partition in partitionTable:

		if 'FAT32' in partition.desc:

			print "Partition Information(FAT32)"

			for partition in partitionTable:

				print partition.addr, partition.desc, "%ss(%s)" % (partition.start, partition.start * 512), partition.len

		if 'NTFS' in partition.desc:

			filesystemObject = pytsk3.FS_Info(imagehandle, offset=(partition.start*512))
			fileobject = filesystemObject.open("/$MFT")

			print "File Name:",fileobject.info.name.name
			print "File Creation Time:",datetime.datetime.fromtimestamp(fileobject.info.meta.crtime).strftime('%Y-%m-%d %H:%M:%S')

			outFileName = str(partition.addr)+fileobject.info.name.name

			print outFileName

			outfile = open(outFileName, 'w')
			filedata = fileobject.read_random(0,fileobject.info.meta.size)
			outfile.write(filedata)
			outfile.close
