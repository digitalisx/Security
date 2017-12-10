#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

struct employee
{
	char name[20];
	char phone[20];
	int age;
};

int main(void)
{
	struct employee arr[3];

	for (int i = 0; i < 3; i++)
	{
		scanf("%s %s %d", &arr[i].name, &arr[i].phone, &arr[i].age);
	}

	for (int i = 0; i < 3; i++)
	{
		printf("%s %s %d\n", arr[i].name, arr[i].phone, arr[i].age);
	}

	system("pause");
}
