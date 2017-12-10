#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

struct point
{
	int xpos;
	int ypos;
};

int main(void)
{
	struct point pos1 = { 1, 2 };
	struct point pos2 = { 100, 200 };
	struct point * pptr = &pos1; // pos1 구조체 변수를 가리키는 포인터

	(*pptr).xpos += 4; // pptr 포인터에 *씌워서 pos1 변수 지정 그 안에 xpos 값 접근 (1+4)
	(*pptr).ypos += 5; // pptr 포인터에 *씌워서 pos1 변수 지정, 그 안에 ypos 값 접근 (2+5)

	printf("[%d %d] \n",pptr->xpos, pptr->ypos); // pptr 포인터로 xpos ypos 값 불러오기 (5,7)

	pptr = &pos2; // pptr 포인터 pos2의 주소로 변경
	pptr->xpos += 1; // pos2의 xpos에 1 더하기 (101)
	pptr->ypos += 2; // pos2의 ypos에 2 더하기 (202)

	printf("[%d %d] \n", (*pptr).xpos, (*pptr).ypos); // pptr 포인터로 xpos ypos 값 불러오기 (101,202)
}
