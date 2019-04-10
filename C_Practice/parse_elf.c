#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct _FINFO
{
	char* address;
	char* name;
} FINFO;

// strcasestr function implementation for unix env

char *strcasestr(const char *haystack, const char *needle)
{
	int size = strlen(needle);

	while(*haystack)
	{
		if(strncasecmp(haystack, needle, size) == 0)
		{
			return (char *)haystack;
		}
		haystack++;
	}
	return NULL;
}

// file exist check function

int file_exists(const char *fname)
{
	if(access(fname, F_OK) != -1)
	{
		printf("[!] Found File!\n");
		return 1;		
	}	
	else
	{
		printf("[!] File not exist!\n");
		exit(1);
	}
}

// mutex function check

int mutex_check(char *func_name)
{
	// pre-defined mutex function
	
	char* mutex_func = "pthread_mutex_init";

	if(strcasestr(func_name, mutex_func) != NULL)
	{
		printf("[!] Found Mutex function\n");
		return 1;
	}
	else
	{
		return 0;
	}
}

// file read and write function check

int fio_check(char *func_name)
{
	// pre-defined fio function and library
	
	char* open_func = "open@@";
	char* read_func = "read@@";
	char* write_func = "write@@";

	if(strcasestr(func_name, open_func) != NULL)
	{
		printf("[!] Found open function\n");
		return 1;
	}
	else if(strcasestr(func_name, read_func) != NULL)
	{
		printf("[!] Found read function\n");
		return 1;
	}
	else if(strcasestr(func_name, write_func) != NULL)
	{
		printf("[!] Found write function\n");
		return 1;
	}
	else
	{
		return 0;
	}
}


// crypto function use check

int crypt_check(char *func_name)
{
	// pre-defined encryption function and library

	char* mbedtls_lib = "mbedtls";
	char* custom_lib = "crypt";

       	if(strcasestr(func_name, mbedtls_lib) != NULL)
	{
		printf("[!] Found mbedtls function\n");
		return 1;
	}
	else if(strcasestr(func_name, custom_lib) != NULL)
	{
		printf("[!] Found suspicious encryption paragraph\n");
		return 1;
	}
	else
	{
		return 0;
	}
}

// extract function name, address from ELF Binary symbol table

char* elf_parse_symtab(const char *fname)
{
	if(file_exists(fname))
	{
		char *gen_command;
		gen_command = malloc(512);

		// merge command

		char base_command[512] = "readelf -s ";
		char grep_function[32] = " | grep \"FUNC\"";
		char awk_function[32] = " | awk {'print $2\" \"$8}'";

		strcat(base_command, fname);
		strcat(base_command, grep_function);
		strcat(base_command, awk_function);
				
		strcpy(gen_command, base_command);		
		
		return gen_command;
	}
}

char* elf_parse_got(const char *fname)
{
	if(file_exists(fname))
	{
		char *gen_command;
		gen_command = malloc(512);

		// merge command

		char base_command[512] = "readelf -r ";
		char awk_function[32] = " | awk {'print $1\" \"$5};";

		strcat(base_command, fname);
		strcat(base_command, awk_function);

		strcpy(gen_command, base_command);
		
		return gen_command;
	}

// extract Internal fucntion from script string

char* script_command(const char *fname)
{
	if(file_exists(fname))
	{
		char* gen_command;
		gen_command = malloc(512);
		char base_command[128] = "strings ";
		strcat(base_command, fname);
		strcpy(gen_command, base_command);
		
		return gen_command;
	}
}

// pipelining and insert info to structure from readelf result

int elf_pipe(const char* command)
{
	FILE *fp;
	char line[4096];
	
	FINFO fs[4098];
	int count;
	int fs_count = 0;

	fp = popen(command, "r");
	if(NULL == fp)
	{
		perror("[!] Failed to popen\n");
		exit(1);
	}

	while(fgets(line, 4096, fp) != NULL)
	{
		if(crypt_check(line))
		{
			// String Tokenlizing

			char *ptr_addr[2];
			char *ptr = strtok(line, " ");
			count = 0;
			while(ptr != NULL)
			{	
				ptr_addr[count] = ptr;
				count += 1;
				ptr = strtok(NULL, " ");
			}
		
			// insert information to struct array	

			fs[fs_count].address = ptr_addr[0];
			fs[fs_count].name = ptr_addr[1];

			printf("%s - %s", fs[fs_count].address, fs[fs_count].name);

			fs_count += 1;	
		}
	}
	pclose(fp);
	return 0;
}

// pipelining and alert function

int script_pipe(const char* command)
{
	FILE *fp;
	char line[4096];

	fp = popen(command, "r");
	if(NULL == fp)
	{
		perror("[!] Failed to popen\n");
		exit(1);
	}

	while(fgets(line, 4096, fp) != NULL)
	{
		if(crypt_check(line))
		{
			printf("%s", line);
		}
	}

	pclose(fp);
	return 0;
}

// main function

int main(void)
{
	// ELF Binary symbol table parse area
	
	char * elf_path = "/mnt/c/Users/DONGHYUN/Desktop/test";
	char * elf_token = elf_parse_symtab(elf_path);
	elf_pipe(elf_token);

	// Bash and Python script paragraph analysis area

	/*
	char * scr_path = "/mnt/c/Users/DONGHYUN/Desktop/sh";
	char * script_token = script_command(scr_path);
	script_pipe(script_token);
	*/

	return 0;
}
