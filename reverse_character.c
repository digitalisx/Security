#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char word[20];
	char temp;
	int length = 0;
	int i = 0;

	scanf("%s", word);

	while (word[i] != '\0')
	{
		length++;
		i++;
	}

	i = 0;

	for(int j = 0; j < length; j++)
	{
		temp = word[i];
		word[i] = word[length - 1];
		word[length - 1] = temp;
		i++;
		length -= 1;
	}

	printf("Reverse Paragraph : %s\n", word);
	
}
