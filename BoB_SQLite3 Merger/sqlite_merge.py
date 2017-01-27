import os
import hashlib
import sqlite3

print "[*] KITRI BoB SQLite3 Merger v1.0"

result_db_path = os.getcwd() + "\\result.db" 

if os.path.isfile(result_db_path):
	
	os.remove(result_db_path)

else:
	
	pass

folder_name = os.getcwd() + "\\input_db"

count_num = 0
meta_info = []
file_dict = {}

print "[!] Making Result DB File in Current Folder\n"

result_db = sqlite3.connect("result.db")
result_db_cur = result_db.cursor()
result_db_cur.execute("CREATE TABLE BoB_DB_Metadata(OriginalDB_Path text, OriginalDB_Hash text, OriginalDB_Tablename text, RecordCount int)")

for root, dirs, files in os.walk(folder_name):
		
	for file in files:
		
		count_num += 1 

		print "[-] Destination DB File : " + file
		
		current_folder = os.getcwd()

		file_path = os.path.join(current_folder, folder_name, file)
		db_file = open(file_path, 'rb')
		db_data = db_file.read()
		db_hash_data = hashlib.sha1(db_data).hexdigest()
		db_file.close()

		con = sqlite3.connect(file_path)
		cursor = con.cursor()
		table_list = list(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"))
		table_dict = {}

		for insert_table in table_list:
				
			mysTuple=[str(x) for x in insert_table]

			for table_name in mysTuple:
					
				table_dict[table_name] = []
				record_count = cursor.execute("SELECT COUNT(*) FROM %s" % table_name).fetchone()[0]

				meta_info.append(table_name)
					
				result_db_cur.execute("INSERT INTO BoB_DB_Metadata VALUES (?, ?, ?, ?)", (file_path, db_hash_data, table_name, record_count))

				cursor.execute("PRAGMA table_info(%s);" % str(table_name))
				temp = cursor.fetchall()
				columns_list = []

				columns_data = cursor.execute("SELECT * FROM {}".format(table_name))
				data_list = list(columns_data)

				for i in range(0, len(temp)):
						
					if (("id" in temp[i][1]) | ("ID" in temp[i][1])):
							
						columns_list.append(temp[i][1])
						
					else:
						columns_list.append(temp[i][1])
					
				table_dict[table_name] = [columns_list] + data_list

			file_dict[file] = table_dict.copy()

con.close()

result_dict = {}

for file_name in file_dict.keys():

	for re_table_name in file_dict[file_name].keys():

		if re_table_name.find("sqlite_") != -1:
			
			continue
            
		if re_table_name not in result_dict.keys():
			
			result_dict[re_table_name] = []

		for data in file_dict[file_name][re_table_name]:
			
			if type(data) == list: # if data is column
				
				if result_dict[re_table_name] == []:
					
					result_dict[re_table_name].append(data)
					query = "CREATE TABLE {}(".format(re_table_name)
					
					for n in range(len(data)):
						
						query += data[n]
						query += " str,"
					
					query = query[:-1]
					query += ")"

					result_db_cur.execute(query)

			elif type(data) == tuple:
				
				if data not in result_dict[re_table_name]:
					
					result_dict[re_table_name].append(data)
					query = "INSERT INTO {} VALUES(".format(re_table_name) #Insert data
					
					for num in range(len(data) - 1):
						
						query += "?, "
					
					query += "?)"
					result_db_cur.execute(query, data)

result_db.commit()
result_db.close()

print "\n[!] Complete merge a total of %s DB files" % count_num
print "[!] Merge DB File Path : %s" %current_folder