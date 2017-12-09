#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void cleanbuff(void)
{
	while (getchar() != '\n');
}

int main(void)
{
	char str[5];

	fputs("문자열 입력 : ", stdout);
	fgets(str, sizeof(str), stdin);
	cleanbuff();

	printf("길이 : %d 내용 : %s\n", strlen(str), str);

	fputs("문자열 입력 : ", stdout);
	fgets(str, sizeof(str), stdin);

	printf("길이 : %d 내용 : %s\n", strlen(str), str);

}
