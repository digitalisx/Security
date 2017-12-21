#define _CRT_SECURE_NO_WARNINGS
#define TRIAL 1000
#define SIZE 10

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int freq[SIZE] = { 0, }; // SIZE 10의 0으로 채워진 배열 선언
	int rnum, min, max;
		
	srand(time(NULL)); // SEED 값을 랜덤하게 분배

	for(int i = 0; i < TRIAL; i++) // 시도횟수 : 1000번 동안 돌림
	{
		rnum = rand() % 10; // 1 ~ 9까지의 수를 랜덤하게 뽑아줌
		printf("%d\n", rnum);
		freq[rnum]++; // rnum에 해당하는 수를 freq 배열에 각각 넣어줌
	}

	max = 0;
	min = 0;

	for (int k = 1; k < SIZE; k++)
	{
		if (freq[k] > freq[max]) // freq[1]의 값이 freq[0]보다 크면
		{
			max = k; // max는 k가 된다
		}
		if (freq[k] < freq[min]) // freq[1]의 값이 freq[min]보다 작으면
		{
			min = k; // min이 k가 된다.
		}
	}

	printf("가장 많이 생성된 수 : %d  / 빈도 : %d\n", max, freq[max]);
	printf("가장 적게 생성된 수 : %d  / 빈도 : %d\n", min, freq[min]);

	system("pause");
}
