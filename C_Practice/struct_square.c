#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

typedef struct rectangle
{
	Point rec_x; // 0,0
	Point rec_y; // 100,100
} Rectangle;

int rectangle_pos(Rectangle *ptr)
{
	printf("First Position : %d %d\n", (ptr->rec_x).xpos, (ptr->rec_x).ypos);
	printf("Second Position : %d %d\n", (ptr->rec_y).xpos, (ptr->rec_y).ypos);
	printf("Third Position : %d %d\n", (ptr->rec_y).xpos, (ptr->rec_x).ypos);
	printf("Fourth Position : %d %d\n", (ptr->rec_x).xpos, (ptr->rec_y).ypos);
}

Point rectangle_area(Rectangle *ptr)
{
	Point area = { (ptr->rec_y).xpos - (ptr->rec_x).xpos, (ptr->rec_y).ypos - (ptr->rec_x).ypos };
	return area;
}

int main(void)
{
	Rectangle pos;
	
	printf("Input First Position : ");
	scanf("%d %d", &(pos.rec_x).xpos, &(pos.rec_x).ypos);

	printf("Input Second Position : ");
	scanf("%d %d", &(pos.rec_y).xpos, &(pos.rec_y).ypos);

	rectangle_pos(&pos);
	
	Point area_result = rectangle_area(&pos);
	printf("Area : %d\n", area_result.xpos * area_result.ypos);
}
