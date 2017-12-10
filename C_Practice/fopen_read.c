#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int ch, i;
	FILE * fp = fopen("data.txt", "rt");
	if (fp == NULL)
	{
		printf("파일 읽기 실패\n");
		return -1;
	}

	for (i = 0; i < 3; i++)
	{
		ch = fgetc(fp);
		printf("%c \n", ch);
	}

	fclose(fp);
	system("pause");
}
