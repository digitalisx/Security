#define _CRT_SECURE_NO_WARNINGS
#define N_RND 10000
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void main(void)
{
	int num, i, seed = 100;
	FILE * fp;
	fp = fopen("rnd_num.txt", "wt");

	srand(seed);
	for(i = 0; i < N_RND; i++)
	{
		fprintf(fp, "%d\n", rand() % 100 + 1);
	}

	fclose(fp);
}
