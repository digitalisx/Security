#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int first(int num)
{
	int j = 0;
	
	for (int i = 1; i <= num; i++)
	{
		j += i;
	}

	j = j*j;
	
	return j;
}

int second(int num)
{
	int j = 0;

	for (int i = 1; i <= num; i++)
	{
		j += (i*i);
	}

	return j;
}

int main(void)
{
	printf("Result : %d\n", first(100) - second(100));
}
