#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
	int sign = 0;
	int sig = 0;
	int digit = 0;
	int period = 0;
	int period_count = 0;
	int period_pos = 0;
	int num_count = 0;

	char str[50];

	printf("Input Number : ");
	scanf("%s", str);

	int len = strlen(str);
	
	if ((str[0] == 43))
	{
		sign = 1;
		sig = 1;
	}
	else if ((str[0] == 45))
	{
		sign = 1;
		sig = -1;
	}
	else
	{
		sign = 0;
	}

	for (int i = 0; i < len; i++)
	{	
		if ((str[i] > 47) && (str[i] < 58))
		{
			num_count += 1;
		}

		if ((str[0] == 42) || (str[0] == 47))
		{
			printf("부호는 + 혹은 - 만이 가능함\n");
			return -1;
		}

		if ((str[i + 1] == 43) || (str[i + 1] == 45))
		{
			printf("숫자 중간에 부호는 나타날 수 없음\n");
			return -1;
		}

		if (((str[i] > 64) && (str[i] < 91))||((str[i] > 96) && (str[i] <123)))
		{
			printf("영문자는 숫자의 표기에 사용할 수 없음\n");
			return -1;
		}

		if ((str[i+1] > 34) && (str[i+1] < 43))
		{
			printf("특수 문자는 숫자 표현에 사용 될 수 없음\n");
			return -1;
		}

		if (str[i] == 46)
		{
			period_count += 1;
			if (period_count >= 2)
			{
				printf("소수점은 한 번만 사용될 수 있음\n");
				return -1;
			}
			period = 1;
			period_pos = i + 1;
		}
	}

	if (num_count == 0)
	{
		printf("어떠한 숫자도 입력하지 않음\n");
		return -1;
	}

	if (sign == 0)
	{
		if (period_count == 0)
		{
			printf("significand = ");
			for (int j = 0; j < len + 1; j++)
			{
				if (j == 1)
				{
					printf(".");
				}
				printf("%c", str[j]);
			}
			printf("exponent = %d\n", len - 1);
			return 0;
		}

		if (period_count >= 1)
		{
			printf("significand = ");
			for (int k = 0; k < len + 1; k++)
			{
				if (k == 1)
				{
					printf(".");
				}
				if (k != (period_pos - 1))
				{
					printf("%c", str[k]);
				}
			}
			printf("exponent = %d\n", period_pos - 2);
			return 0;
		}
	}

	if (sign == 1)
	{
		printf("significand = ");

		if (sig == -1)
		{
			printf("-");
		}

		for (int k = period_pos; k < len + 1; k++)
		{
			if (k == (period_pos + 1))
			{
				printf(".");
			}
			if (k != (period_pos - 1))
			{
				printf("%c", str[k]);
			}
		}
		printf("exponent = %d\n", period_pos - 3);
		return 0;
	}
	return 0;
}
