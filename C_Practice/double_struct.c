#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

typedef struct circle
{
	Point cen;
	double rad;
} Circle;

void ShowCircleInfo(Circle * cptr)
{
	printf("[%d %d] \n", (cptr->cen).xpos, (cptr->cen).ypos);
	printf("Radius : %g \n\n", cptr->rad);
}

int main(void)
{
	Circle c1 = { {1,2}, 3.5 }; // Point 구조체 변수 cen (xpos:1, ypos:2)에, rad에는3.5 들어감
	Circle c2 = { 2,4, 3.9 }; // Point 구조체 변수 cen (xpos: 2, ypos:4) 에 포인터 잡혀있음, rad에는 3.9들어감
	ShowCircleInfo(&c1); // c1의 cen에 접근한뒤 안에 있는 xpos ypos를 가져온다.
	ShowCircleInfo(&c2); // c2의 cen에 접근한뒤 안에 있는 xpos ypos를 가져온다.

	system("pause");
}
