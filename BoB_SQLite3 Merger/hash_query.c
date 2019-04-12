#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sqlite3.h>

#define _SIGFIND 1
#define _SIGNFIND 0

int sqlite_callback(void *pArg, int argc, char **argv, char **columnNames)
{
	return argv[1];
}

char* calculate_md5(const char * file_name)
{
	FILE *fp;
	char *result = malloc(sizeof(char) * 20);
	char base_command[128] = "md5sum ";
	char awk_command[128] = " | awk '{print $1}'";
	char line[128];
	
	strcat(base_command, file_name);
	strcat(base_command, awk_command);
	fp = popen(base_command, "r");

	if(NULL == fp)
	{
		perror("[!] Failed to popen\n");
		exit(1);
	}

	while(fgets(line, 128, fp) != NULL)
	{
		strcpy(result ,line);
		strtok(result, "\n");
		return result;
	}

	return 0;
}

int sqlite_diff(const char * md5_value)
{	
	char *zErrMsg = 0; 
	char sql_query_header[128] = "SELECT * FROM malware WHERE md5=\"";
	char sql_query_footer[16] = "\";";

	printf("[!] MD5 Hash : %s\n", md5_value);

	strcat(sql_query_header, md5_value);
	strcat(sql_query_header, sql_query_footer);
	sqlite3 *conn;
	sqlite3_open("malware.db", &conn);

	if(sqlite3_exec(conn, sql_query_header, sqlite_callback, 0, &zErrMsg))
	{
		printf("[!] Ransomware Signature Found!\n");
		return 1;
	}
	else
	{
		printf("[!] Ransomware Signature Not Found!\n");
		return 0;
	}
}

int main(void)
{
	sqlite_diff(calculate_md5("stack"));
	return 0;
}
