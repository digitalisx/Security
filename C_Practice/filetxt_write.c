#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE * fp = fopen("simple.txt", "wt");

	if (fp == NULL)
	{
		puts("파일 오픈 실패!");
		return -1;
	}

	fputs("A\n", fp);
	fputs("B\n", fp);
	fputs("My name is Hong \n", fp);
	fputs("Your name is Yoon \n", fp);
	fclose(fp);
	
	return 0;
}
