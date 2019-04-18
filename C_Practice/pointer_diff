#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

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

unsigned long int* GetMapInfo(pid_t pid)
{
	// memory allocation for save path, addr
	
	unsigned long int* addr = (unsigned long int*)calloc(1, 4*sizeof(unsigned long int));
	char* map = (char*)calloc(1, 150);
	char* path = (char*)calloc(1, 100);
	char* real_path = (char *)calloc(1, 100);
	void* padding = NULL;

	// open mpas file according to pid (addr of process)

	sprintf(path, "/proc/%d/maps", pid);
	FILE* f = fopen(path, "r");

	// open exe file according to pid (run program list)

	memset(path, 0, 100);
	sprintf(path, "/proc/%d/exe", pid);
	readlink(path, real_path, 100);
	int idx = 0;
 
	while(!feof(f))
	{
		fgets(map, 150, f);
		map[strlen(map - 1)] = '\x00';

		if(strcasestr(map, real_path))
		{
			addr[idx++] = strtoul(map, (char **)&padding, 16);
			
			if(idx > 2)
				break;
		}
		else
			continue;
	}

	fclose(f);

	if(idx > 2)
	{
		padding += 1;
		map = padding;
		addr[idx] = (strtoul(map, NULL, 16) - 0x100);
	}

	free(map);
	free(path);
	free(real_path);

	return addr;
}

int AddrMod(unsigned long int * addr, char * dest)
{	
	unsigned long first_address;
	unsigned long second_address;

	sscanf(dest, "%lx-%lx", &first_address, &second_address);

	if(((uintptr_t)first_address <= (uintptr_t)addr) && ((uintptr_t)second_address >= (uintptr_t)addr))
	{
		printf("[!] Find Result : True\n");
		return 1;
	}
	else
	{
		printf("[!] Find Result : False\n");
		return 0;
	}

	return 0;
	
}

int AddrCheck(unsigned long int * addr, pid_t pid)
{
	FILE * fp = NULL;
	char line[1024];
	char mmap_command[128];
	sprintf(mmap_command,"cat /proc/%d/maps | grep \"%s\\|%s\\|%s\"", pid, "stack", "heap", "maped");

	if((fp = popen(mmap_command, "r")) == NULL)
	{
		return -1;
	}

	while(fgets(line, 1024, fp) != NULL)
	{	
		strtok(line, " ");
		printf("[!] Find Memory Area : %s\n", line);
		AddrMod(addr, line);
	}

	pclose(fp);
	return 0;
}

int main(void)
{
	printf("[!] Input Memory Address : %p\n", GetMapInfo(80));
	AddrCheck(GetMapInfo(80), 80);
	return 0;
}

