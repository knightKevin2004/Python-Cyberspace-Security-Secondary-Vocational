#include <stdio.h>
#include <stdlib.h>
#include "md5.h"
 
int main(int argc, char *argv[])
{
	int i;
	char encrypt[100];
	scanf("%s",encrypt);
	if (strlen(encrypt) != 29)
	{
	    return 1;
	}
        else
	{
            for(int i = 0;i < strlen(encrypt);i++){
	        if(encrypt[i]=='#')
		    encrypt[i]='\0';
	    };
	}
	unsigned char decrypt[16];
	MD5_CTX md5;
	MD5Init(&md5);
	MD5Update(&md5,encrypt,strlen((char *)encrypt));
	MD5Final(&md5,decrypt);
	printf("加密前:%s\n加密后:",encrypt);
	for(i=0;i<16;i++)
	{
		printf("%02x",decrypt[i]);
	}
	
	getchar();
	
	return 0;
}
