#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE * src = fopen("src.txt", "rt"); // src.txt를 읽기 모드로 염, 파일 존재해야 함
	FILE * dsc = fopen("dsc.txt", "wt"); // dsc.txt를 쓰기 모드로 염, 파일 자동 생성
	char str[50]; // str 배열 길이

	if (src == NULL) // src.txt 존재 유무 판별
	{
		printf("파일 오픈 실패 \n");
	}
		
	while ((fgets(str, sizeof(str), src) != NULL)) // src로부터 str size만큼 한줄씩 str에 복사 fgetc는 EOF를 반환함
	{
		fputs(str, dsc); // str의 값을 dsc에 한줄 적기
	}

	if (feof(src) != 0) // src가 끝에 도달하면 0말고 다른 수 반환
	{
		printf("파일 복사 완료\n");
	}
	else
	{
		printf("파일 복사 실패\n");
	}
	fclose(src); // 파일 닫기
	fclose(dsc); // 파일 닫기
}
