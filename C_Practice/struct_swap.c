#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

Point SwapPoint(Point * pos1, Point * pos2)
{
	Point temp;
	temp = *pos1;
	*pos1 = *pos2;
	*pos2 = temp;
}

int main(void)
{
	Point pos1 = { 2,4 };
	Point pos2 = { 5,7 };
	
	SwapPoint(&pos1, &pos2);

	printf("POS1 : %d %d\n", pos1.xpos, pos1.ypos);
	printf("POS2 : %d %d\n", pos2.xpos, pos2.ypos);
}
