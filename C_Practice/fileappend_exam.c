#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE * fp = fopen("mystory.txt", "at");

	fputs("#즐겨먹는 음식 : 짬뽕, 탕수육\n", fp);
	fputs("#취미 : 축구\n", fp);

	fclose(fp);
}
