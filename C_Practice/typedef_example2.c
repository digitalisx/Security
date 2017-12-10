#include <stdio.h>

typedef struct position
{
	int xpos;
	int ypos;
}POINT;

int main(void)
{
	POINT pos;
	scanf("%d %d", &pos.xpos, &pos.ypos);

	printf("%d %d\n", pos.xpos, pos.ypos);
}
