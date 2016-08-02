# -*- coding: utf-8 -*-

# Import Module
import gmail
import datetime
import base64
import re
import ssl
import urllib
import urllib2
import os
import os.path
import csv
import sqlite3
import hashlib
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import exifread

def main():

	# Parse Today's Date
	print "[!] E-Mail Parser"
	print "=================================================================================================="
	now_date = datetime.datetime.now()
	cov_date = str(now_date)[8:10]
	cov_date = int(cov_date)

	print "[+] Today is " + str(cov_date) + " day"

	print "[+] Prepare to parsing"
	
	# Make DB File
	file_db = open("..\\result.db","a+")
	print "[-] Make DB File!"
	con = sqlite3.connect("..\\result.db")
	con.text_factory = str
	cursor = con.cursor()
	# Create Table
	cursor.execute("CREATE TABLE IF NOT EXISTS result(File_Time text, Short_URL text, Long_URL text, File_Name text, GPS_X text, GPS_Y text, MD5 text, SHA1 text)")

	# Create CSV File
	file_csv = open("result.csv","w")
	result = csv.writer(file_csv, lineterminator = '\n')
	print "[-] Make CSV File!"
	result.writerow(["\xEF\xBB\xBF"])
	result.writerow(["File Number","Time","Short URL","Long URL", "File Name", "GPS (X)","GPS (Y)","MD5","SHA1"])

	# Login Gmail
	print "[-] Log-on Gmail Account..."
	g = gmail.login('digitalisx99@gmail.com', 'dnflsk135')

	target = 'fl0ckfl0ck@hotmail.com'

	# Check Mail in Box
	emails = g.inbox().mail(on = datetime.date(2016, 7, 29), sender = target)

	print "[-] Collect Link from Target's E-Mail : " + target 
	
	file_num = 0

	print "=================================================================================================="
	
	# Define GPS Info List
	gps_list = []
	
	for email in emails: # for every email sent in same day

		email.fetch() 
		txt = email.body
		
		file_num += 1 # File Number Count

		print "[!] Send Time : " + str(email.sent_at) + "\n"

		dec_txt = txt
		
		# Encoding Compare
		if email.headers.has_key('Content-Transfer-Encoding'):
			
			if email.headers['Content-Transfer-Encoding'] == 'base64':
			
				dec_txt = base64.b64decode(txt)
			
			else:
				
				pass
		
		# Use Regular Expression
		reg ='((https?://grep\.kr/[0-9a-zA-Z]{4})|https?://goo\.gl/[0-9a-zA-Z]{6})|(https?://me2\.do/[0-9a-zA-Z]{8})'
		
		file_short = re.search(reg, dec_txt).group()

		# Long URL
		try:
			long_url = urllib.urlopen(file_short, context=ssl._create_unverified_context()).geturl()
			file_long = urllib.unquote(urllib.unquote(long_url))

		# If Link is bomb, shutdown program
		except:
			print "[!] Warning : Sorry, This Link is Bomb!\n"
			result.writerow([file_num, email.sent_at, file_short, None, None, None, None, None, None])	
			exit()

		# Print URL Info
		print "[+] URL Info"
		print "[-] Short URL : " + file_short
		print "[-] Long URL : " + file_long + "\n"
		
		# Parse File Name
		file_name = file_long.split('/')[-1].decode('UTF-8')
		
		print "[+] File Name : " + file_name + "\n"

		try:
			
			# Download File from Long URL
			urllib.urlretrieve(long_url, file_name, context = ssl._create_unverified_context())
		
		except: 
			
			# HTTP/HTTPS Compare and Add
			long_url = long_url.replace("http", "https")
			urllib.urlretrieve(long_url, file_name, context = ssl._create_unverified_context())
		
		d_file = open(file_name, 'rb')

		# Export GPS Info from Image File
		tags = exifread.process_file(d_file)

		# This File included GPS info?
		if 'GPS GPSLongitude' in tags :
			
			# Calculate GPS_Y
			degx = int(tags['GPS GPSLatitude'].values[0].num)
			minx = int(tags['GPS GPSLatitude'].values[1].num)
			secx = float(tags['GPS GPSLatitude'].values[2].num)/tags['GPS GPSLatitude'].values[2].den
			
			# Calculate GPS_X
			degy = int(tags['GPS GPSLongitude'].values[0].num)
			miny = int(tags['GPS GPSLongitude'].values[1].num)
			secy = float(tags['GPS GPSLongitude'].values[2].num)/tags['GPS GPSLongitude'].values[2].den

			file_gpsy = (degy + (miny + secy / 60.0) / 60.0)
			file_gpsx = (degx + (minx + secx / 60.0) / 60.0)

			# If image file is include Ref Tag
			if tags['GPS GPSLatitudeRef'].values == "S":

				file_gpsx = -file_gpsx

			else:
				pass

			# Print EXIP GPS Info	
			print "[+] EXIF GPS Info"
			print "[-] GPS_X : " + str(file_gpsx)
			print "[-] GPS_Y : " + str(file_gpsy) + "\n"

			# Add info to GPS List
			gps_list.append(str(file_gpsx) + ',' + str(file_gpsy))

		else:
			print "[!] This File is not include GPS info\n"
			file_gpsx = None
			file_gpsy = None

		# File Read
		file_read = d_file.read()
		
		# Calculate File of Hash
		file_md5 = hashlib.md5(file_read).hexdigest()
		file_sha1 = hashlib.sha1(file_read).hexdigest()

		d_file.close()
		
		# Print Hash Info
		print "[+] File Hash Info"
		print "[-] MD5 : " + file_md5
		print "[-] SHA1 : " + file_sha1 + "\n"

		# Write on CSV File
		result.writerow([file_num, email.sent_at, file_short, file_long, file_name.encode('UTF-8'), file_gpsx, file_gpsy, file_md5, file_sha1])

		print "[!] Success write on CSV file"

		# Write on DB File
		cursor.execute("INSERT INTO result VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (email.sent_at, file_short, file_long, file_name, file_gpsx, file_gpsy, file_md5, file_sha1))
	
		print "[!] Success write on DB file"

		print "=================================================================================================="

		# Commit and Close DB File
	con.commit()
	con.close()

	# Define Google API Key
	google_api_key = '&key=AIzaSyAgkE8M1Zj_qAGrIuh62497eRHazjS_jB4'

	# Define Standard Map Link
	map_standard = 'https://maps.googleapis.com/maps/api/staticmap?&zoom=2&size=1500x1200&maptype=satellite&markers='
	map_path = '&path='

	# Export GPS Info from List
	for gps_xy in gps_list:
		map_standard = map_standard + gps_xy + '%7C' 
		map_path = map_path + gps_xy + '%7C'

	# Create Final Map URL
	real_map_url = map_standard + map_path[0:-3] + google_api_key

	# Open & Download Map Image File
	urllib.urlretrieve(real_map_url, "travel_path.jpg", context = ssl._create_unverified_context())
	print "\n[!] Success Download Travel Path Photo"
	print "[+] Make trave_path.jpg"
	print "\n=================================================================================================="

def make_folder():
	
	# Make Directory
	real_dir = './result'
	in_dir = './2016-07-29'

	#caldir = datetime.datetime.now()
	#cov_dir = str(caldir)[0:10]
	#real_dir = './report'
	#in_dir = './' + cov_dir
	
	# Check & Make Directory
	if not os.path.exists(real_dir):
		os.mkdir(real_dir)
	
	os.chdir(real_dir)

	if not os.path.exists(in_dir):
		os.mkdir(in_dir)

	os.chdir(in_dir)

make_folder()
main()

# GPS Info export from DB 
con = sqlite3.connect("..\\result.db")
con.text_factory = str
cursor = con.cursor()
cursor.execute("SELECT GPS_X,GPS_Y FROM RESULT WHERE GPS_X IS NOT NULL AND GPS_Y IS NOT NULL;")

# Define Standard Map Link
map_url = ''
map_standard = 'https://maps.googleapis.com/maps/api/staticmap?&key=AIzaSyAgkE8M1Zj_qAGrIuh62497eRHazjS_jB4&zoom=2&size=1500x1200&maptype=satellite'
map_markers = ''
map_path = '&path=color:0xff0000ff|weight:1'

for row in cursor:
	map_markers = map_markers + "&markers="  + row[0] + ", " + row[1]
	map_path = map_path + "|" + row[0] + ", " + row[1]

# Create Map Full URL
map_url = map_standard + map_markers + map_path

# Download Final Travel Path Image File
urllib.urlretrieve(map_url, "..\\final_travel_path.jpg", context = ssl._create_unverified_context())

print "\n[!] Save Final Travel Path Image File"
print "\n=================================================================================================="