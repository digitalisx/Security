#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int ch;

	ch = getchar();

	if ((ch > 64) && (ch < 91))
	{
		putchar(ch + 32);
	}
	else if ((ch > 96) && (ch < 123))
	{
		putchar(ch - 32);
	}
	else
	{
		puts("Error");
	}
}
