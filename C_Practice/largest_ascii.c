#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	char word[20];
	int i = 0;
	char largest_char = '\0';

	scanf("%s", word);

	while (word[i] != '\0')
	{
		if (word[i] > largest_char)
		{
			largest_char = word[i];
		}

		i++;
	}
	
	printf("%c\n", largest_char);

}
