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

		SQL_PARAGRAPH = "INSERT INTO malware (Name, MD5) values (?, ?)"
		self.cur.execute(SQL_PARAGRAPH, (name, md5_value))

		return 0

	def generate_table(self):
		
		self.cur.execute("CREATE TABLE IF NOT EXISTS malware (Name text, MD5 text)")

		os.chdir("samples")

		for file_name in os.listdir():
			self.generate_cell(file_name)

		self.conn.commit()
		self.conn.close()
		
		return 0

if __name__ == "__main__":

	instance = sqlite()
	instance.generate_table()
