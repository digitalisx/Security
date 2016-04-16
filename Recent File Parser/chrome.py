import os
import sys
import sqlite3

print("\n[!] Chrome History Viewer\n")

print("[!] Process kill for open History DB file\n")

os.system("taskkill.exe /f /im chrome.exe")

con = sqlite3.connect('C:\Documents and Settings\DongHyun\AppData\Local\Google\Chrome\User Data\Default\History')
cursor = con.cursor()
cursor.execute("SELECT * FROM keyword_search_terms ORDER BY url_id DESC")

count = 0
		
while count < 15:
	
	count = count + 1

	data = cursor.fetchone()
	covdata = "".join(str(data))
	
	print "\n",covdata.decode('unicode_escape')

	if count == 15:
		
		print("\n[!] Complete History DB load! - 15 Search Keyword")