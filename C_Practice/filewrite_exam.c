#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE * fp = fopen("mystory.txt", "wt");

	fputs("#이름 : 김동현\n", fp);
	fputs("#주민번호 : 111111-1111111\n", fp);
	fputs("#전화번호 : 010-1111-1111\n", fp);

	fclose(fp);
}
