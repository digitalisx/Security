#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct person
{
	char name[50];
	char phone[20];
	int pay_hour;
	int work_hour;
	int total_pay;
} Person;

void sort(Person *info, int num)
{
	Person temp;

	for (int i = 0; i < num - 1; i++)
	{
		for (int j = 0; j < num - 1 - i; j++)
		{
			if (info[j].total_pay < info[j + 1].total_pay)
			{
				temp = info[j];
				info[j] = info[j + 1];
				info[j + 1] = temp;
			}
		}
	}
}

int main(void)
{
	FILE * inp = fopen("input.txt", "rt");
	FILE * out = fopen("output.txt", "wt");
	Person *info;
	int num;

	if (inp == NULL)
	{
		printf("Input Text File Not Found!\n");
		return -1;
	}

	fscanf(inp, "%d", &num);
	info = (Person *)calloc(num, sizeof(Person));

	for (int i = 0; i < num; i++)
	{
		fscanf(inp, "%s", info[i].name);
		fscanf(inp, "%s", info[i].phone);
		fscanf(inp, "%d", &info[i].pay_hour);
		fscanf(inp, "%d", &info[i].work_hour);
		info[i].total_pay = info[i].pay_hour * info[i].work_hour;
	}

	sort(info, num);

	fputs("Name   Phone          Working Hour  pay/hour  total pay\n", out);

	for (int j = 0; j < num; j++)
	{
		fprintf(out, "%s %s  %d            %d     %d\n", info[j].name, info[j].phone, info[j].pay_hour, info[j].work_hour, info[j].total_pay);
	}

	free(info);
	fclose(inp);
	fclose(out);

	return 0;
}
