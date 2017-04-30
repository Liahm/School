#include "csapp.h"

void *thread(void *vargp)
{
	printf("Hello, world\n");
	return NULL;
}

int main(int argc, char *argv[])//added command line argument 
{
	pthread_t tid;
	long num = strtol(argv[1], NULL, 0); 
	int i= 0;
	while(i < num) // loop as many times as argument given.
	{
		pthread_create(&tid, NULL, thread, NULL);
		pthread_join(tid, NULL);
		i++;
	}
	exit(0);
}	
