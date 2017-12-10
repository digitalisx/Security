#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE * fp = fopen("mystory.txt", "rt");
	char str[50];
	int eo;

	if (fp == NULL)
	{
		printf("파일 없음\n");
		return -1;
	}

	while (fgets(str, sizeof(str), fp) != NULL)
	{
		printf("%s", str);
	}

	if (feof(fp) != 0)
	{
		printf("파일 읽기 완료\n");
	}
	else
	{
		printf("파일 읽기 실패\n");
	}

	fclose(fp);

	system("pause");
}
