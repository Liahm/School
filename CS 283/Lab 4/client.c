#include <stdio.h>
#include <stdlib.h>
#include "csapp.h"

int main(int argc, const char* argv[])
{
	char *buf, *p;
	char arg1[MAXLINE], arg2[MAXLINE], arg3[MAXLINE], content[MAXLINE];
	int n1=0, n2=0, n3=0;
	if ((buf = getenv("QUERY_STRING")) != NULL) {
		p = strchr(buf, '&');
		*p = '\0';
		strcpy(arg1, buf);
		strcpy(arg2, p+1);
		strcpy(arg3, p+2);
		n1 = atoi(arg1);
		n2 = atoi(arg2);
		n3 = atoi(arg3);
	} 
	if(argc < 2)
	{
		return EXIT_FAILURE;
	}
	else
	{
		const char* host = argv[1];
		const char* port = argv[2];
		const char* file = argv[3];
		
		printf("Input: %s, %s, %s \n", host, port, file);
		sprintf(content, "Website?");
		sprintf(content, "%s", host);

		printf("Content-length: %d\r\n", (int)strlen(content));
		printf("Content-type: text/html\r\n\r\n");
		printf("%s", content);
		fflush(stdout);
		exit(0);
	}
}

