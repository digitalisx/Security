#include <stdio.h>

typedef int INT;
typedef int * PTR_INT;

typedef unsigned int UINT;
typedef unsigned int * PTR_UINT;

typedef unsigned char UCHAR;
typedef unsigned char * PTR_UCHAR;

int main(void)
{
	INT num1 = 120;
	PTR_INT pnum1 = &num1;

	UINT num2 = 190;
	PTR_UINT pnum = &num2;

	UCHAR ch = 'z';
	PTR_UCHAR pch = &ch;

	printf("%d %d %c", *pnum1, *pnum, *pch);
}
