#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int swap(int *num1, int *num2, int *num3)
{
	int temp;
	temp = *num2;
	*num2 = *num1;
	*num1 = *num3;
	*num3 = temp;
}

int main(void)
{
	int num1, num2, num3;
	
	scanf("%d %d %d", &num1, &num2, &num3);
	
	swap(&num1, &num2, &num3);

	printf("%d %d %d\n", num1, num2, num3);
}
