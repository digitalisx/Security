#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

void remove_bsn(char str[])
{
	int len = strlen(str) - 1;
	str[len] = 0;
}

int main(void)
{
	char str1[20];
	char str2[20];
	char str3[20];

	fgets(str1, sizeof(str1), stdin);

	remove_bsn(str1);

	fgets(str2, sizeof(str2), stdin);

	remove_bsn(str2);

	strcpy(str3, str1);
	strcat(str3, str2);
	fputs(str3, stdout);

	printf("\n");
}
