#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int squarebyvalue(int x)
{
	int square = x * x;
	return square;
}

int squarebyrefer(int *x)
{
	*x = *x * *x;
}

int main(void)
{
	int num1;

	scanf("%d", &num1);
	printf("Square By Value : %d\n", squarebyvalue(num1));
	
	squarebyrefer(&num1);

	printf("Square By Reference : %d\n", num1);

	return 0;
}
