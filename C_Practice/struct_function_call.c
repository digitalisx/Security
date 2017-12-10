#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

void OrgSymTrans(Point * ptr)
{
	ptr->xpos = (ptr->xpos) * -1;
	ptr->ypos = (ptr->ypos) * -1;
}

void ShowPosition(Point pos)
{
	printf("[%d %d] \n", pos.xpos, pos.ypos);
}

int main(void)
{
	Point pos = { 7, -5 }; // pos xpos : 7, ypos : -5
	
	OrgSymTrans(&pos); // -7, 5
	ShowPosition(pos); // -7, 5
	OrgSymTrans(&pos); // 7, -5
	ShowPosition(pos); // 7, -5
}
