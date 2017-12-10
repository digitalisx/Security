#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct dbshort
{
	unsigned short upper;
	unsigned short lower;
} DBShort;

typedef union rdbuf
{
	int iBuf;
	char bBuf[4];
	DBShort sBuf;
} RDBuf;

int main(void)
{
	RDBuf buf;
	printf("정수 입력 : ");
	scanf("%d", &(buf.iBuf));

	printf("상위 2 Byte : %u \n", buf.sBuf.upper);
	printf("하위 2 Byte : %u \n", buf.sBuf.lower);
	printf("상위 1 Byte ASCII Code : %c \n", buf.bBuf[1]);
	printf("하위 1 Byte ASCII Code : %c \n", buf.bBuf[2]);
}
