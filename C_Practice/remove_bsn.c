#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void remove_bsn(char * str)
{
	int len = strlen(str);
	str[len - 1] = 0;
}

int main(void)
{
	char str[100];

	fputs("문자열 입력 : ", stdout);
	fgets(str, sizeof(str), stdin);
	remove_bsn(str);

	printf("길이 : %d 내용 : %s\n", strlen(str), str);
}
