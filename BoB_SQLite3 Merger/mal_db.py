import os
import hashlib
import sqlite3

class sqlite:

	def __init__(self):
		
		self.conn = sqlite3.connect("malware.db")
		self.cur = self.conn.cursor()

	def generate_cell(self, name):

		md5_file = open(name, "rb")
		md5_read = md5_file.read()
		md5_value = hashlib.md5(md5_read).hexdigest()

		SQL_PARAGRAPH_HEADER = "INSERT INTO malware VALUES ('"
		SQL_PARAGRAPH_MIDDLE = name + "', '"
		SQL_PARAGRAPH_JUSTIFY = str(md5_value)
		SQL_PARAGRAPH_TAIL = "')"

		SQL_PARAGRAPH_FULL = ""
		SQL_PARAGRAPH_FULL += SQL_PARAGRAPH_HEADER
		SQL_PARAGRAPH_FULL += SQL_PARAGRAPH_MIDDLE
		SQL_PARAGRAPH_FULL += SQL_PARAGRAPH_JUSTIFY
		SQL_PARAGARPH_FULL += SQL_PARAGRAPH_TAIL

		return SQL_PARAGRAPH_FULL

	def generate_table(self):
		
		self.cur.execute("CREATE TABLE malware (Name text, MD5 text)")

		os.chdir("samples")

		for file_name in os.listdir():
			self.cur.execute(self.generate_cell(file_name))

		self.conn.commit()
		self.conn.close()
		
		return 0

if __name__ == "__main__":

	instance = sqlite()
	instance.generate_table()
