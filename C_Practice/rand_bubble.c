#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubble_sort(int * ptr, int count)
{
	int temp;
	for (int i = 0; i < count; i++)
	{
		for (int j = 0; j < count - 1; j++)
		{
			if (ptr[j] < ptr[j + 1])
			{
				temp = ptr[j];
				ptr[j] = ptr[j + 1];
				ptr[j + 1] = temp;
			}
		}
	}
}

int main(void)
{
	int num;
	int * ptr;

	srand((unsigned)time(NULL));

	scanf("%d", &num);

	ptr = (int)malloc(sizeof(int) * num);

	for (int i = 0; i < num; i++)
	{
		ptr[i] = rand() % 10 + 1;
	}

	bubble_sort(ptr, num);

	for (int j = 0; j < num; j++)
	{
		printf("%d ", ptr[j]);
	}
	printf("\n");

	system("pause");
}
