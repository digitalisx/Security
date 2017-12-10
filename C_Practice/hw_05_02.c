#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
	char han[10][4] = { "", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구" }; // 값마다
	char smallunit[][4] = { "", "십", "백", "천" }; // 각 마다
	char largeunit[][4] = { "", "만", "억", "조", "경" }; // len / 4 만큼 들어가면 됨
	char str[64];

	scanf("%s", str);
	int len = strlen(str);
	int spe_num = len / 4;

	for(int i = 0; i < len; i++)
	{
		int val = str[i] - 48;	
		printf("%s", han[val]);
		
		if (((len - i - 1) % 4) == 0)
		{
			printf("%s", largeunit[spe_num]);
			spe_num--;
		}
		
		printf("%s", smallunit[(len - i - 1) % 4]);
	}
	printf("\n");
	system("pause");
}
