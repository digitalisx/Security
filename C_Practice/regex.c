#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

regex_t regex;
int reti;
char msgbuf[4096];

int main(void)
{
	char pattern_crypt[1024] = "(mbedtls_)([a-z_0-9]*)(_crypt)([a-z_0-9]*)|";
	char pattern_update[1024] = "(mbedtls_)([a-z_0-9]*)(_update)|";
	char pattern_finish[1024] = "(mbedtls_)([a-z_0-9]*)(_finish)|";
	char pattern_evp_update[1024] = "(EVP_)([a-zA-Z_0-9]*)(Update)|";
	char pattern_evp_final[1024] = "(EVP_)([a-zA-Z_0-9]*)(_Final)|";
	char pattern_aes[1024] = "(AES_)([a-z0-9]*)(_encrypt)";
		
	strcat(pattern_crypt, pattern_update);
	strcat(pattern_crypt, pattern_finish);
	strcat(pattern_crypt, pattern_evp_update);
	strcat(pattern_crypt, pattern_evp_final);
	strcat(pattern_crypt, pattern_aes);

	printf("%s\n", pattern_crypt);

	reti = regcomp(&regex, pattern_crypt, REG_EXTENDED);

	if(reti)
	{
		printf("Could not compile regex\n");
		exit(1);
	}

	char dest[1024] = "mbedtls_aes_crypt_hello";

	reti = regexec(&regex, dest, 0, NULL, 0);

	if(!reti)
	{
		printf("Match");
	}
	else if(reti == REG_NOMATCH)
	{
		printf("No Match");
	}
	else
	{
		regerror(reti, &regex, msgbuf, sizeof(msgbuf));
		printf("Regex Match Failed");
		exit(1);
	}
}


