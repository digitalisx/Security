#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[20] = "First~";
	char str2[20] = "Second";

	char str3[20] = "Simple num: ";
	char str4[20] = "1234567890";

	strcat(str1, str2);
	fputs(str1, stdout);

	printf("\n");

	strncat(str3, str4, 7);
	fputs(str3, stdout);

	printf("\n");
}
