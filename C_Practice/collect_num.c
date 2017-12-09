#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[20];
	int sum = 0;

	printf("문자열을 입력하세요 : ");
	scanf("%s", str1);

	for (int i = 0; i < strlen(str1); i++)
	{
		if ((str1[i] > 47) && (str1[i] < 58))
		{
			sum += (str1[i] - 48);
		}
	}
	printf("Sum : %d\n", sum);
}
