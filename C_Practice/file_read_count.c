#define _CRT_SECURE_NO_WARNINGS
#define N_RND 10000
#define STEP 10
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int num, i, stat[STEP] = { 0, }; // stat 각 레이어에 맞는 수 카운팅을 위한 배열
	FILE * fp1, * fp2;

	fp1 = fopen("rnd_num.txt", "rt");

	if (fp1 == NULL)
	{
		printf("fopen() Failed\n");
		return 0;
	}

	fp2 = fopen("count.txt", "wt");

	for (i = 0; i < N_RND; i++) // 100000개 써칭
	{
		fscanf(fp1, "%d", &num); // 한줄씩 읽어서 num에 넣어줌
		stat[(num - 1) / STEP]++;  //  21, 31부터 시작이기때문에 넣어주려면 -1을 해야함
	}

	for (i = 0; i < STEP; i++)
	{
		fprintf(fp2, "[%3d ~ %3d] : %4d\n", i * STEP + 1, (i + 1)* STEP, stat[i]);
	}

	fclose(fp1);
	fclose(fp2);
}
