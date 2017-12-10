#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE * fp = fopen("simple.txt", "rt");

	char str[50];

	if (fp == NULL)
	{
		puts("파일 오픈 실패!");
		return -1;
	}

	for (int i = 0; i < 4; i++)
	{
		fgets(str, sizeof(str), fp);
		printf("%s", str);
	}
	return 0;
}
