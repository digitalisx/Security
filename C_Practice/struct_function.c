#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
}Point;

void Showposition(Point curl)
{
	printf("[%d %d]\n", curl.xpos, curl.ypos);
}

Point GetPosition(void)
{
	Point Cen;
	scanf("%d %d", &Cen.xpos, &Cen.ypos);
	return Cen;
}

int main(void)
{
	Point Cen = GetPosition();
	Showposition(Cen);
}
