#include "csapp.h"

void *thread(void *vargp); //wrote rpg isntead of rgp many times

int main()
{
	pthread_t tid;
	pthread_create(&tid, NULL, thread, NULL);
	pthread_join(tid, NULL);
	exit(0);
}

void *thread(void *vargp)
{
	Sleep(1);
	printf("Hello, world!\n");
	return NULL;
}
