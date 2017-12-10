#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

struct point
{
	int xpos;
	int ypos;
};

struct person
{
	char name[20];
	char phoneNum[20];
	int age;
};

int main(void)
{
	struct point pos = { 10,20 };
	struct person man = { "이승기", "010-1234-2345", 21 };

	printf("%p %p \n", &pos, &pos.xpos);
	printf("%p %p \n", &man, man.name);
}
