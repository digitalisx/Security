#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[20];
	char str2[20];

	fputs("첫번째 문자열 입력", stdout);
	scanf("%s", str1);

	fputs("두번째 문자열 입력", stdout);
	scanf("%s", str2);

	if (strcmp(str1, str2) == 0)
	{
		fputs("해당 문자열은 동일합니다.", stdout);
		printf("\n");
	}
	else
	{
		fputs("두 문자열은 동일하지 않습니다.", stdout);
		printf("\n");
		
		if (strncmp(str1, str2, 3) == 0)
		{
			fputs("그러나 앞의 3자리는 동일합니다", stdout);
			printf("\n");
		}
	}
}
