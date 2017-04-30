#include <stdio.h>
#include <pthread.h>
#include "csapp.h"
#define NUM_THREADS 8
char *messages[NUM_THREADS];
struct thread_info{
	int taskid, sum;
	char *hello_msg;
};

void *PrintHello(void *threadarg)
{
	int taskid, sum;
	char *hello_msg;
	struct thread_info *data;    

	data = (struct thread_info* ) threadarg;
	taskid = data->taskid;
	sum = data->sum;
	hello_msg = data->hello_msg;
   //define what each variable is
   printf("Thread %d %s Sum=%d\n", taskid, hello_msg, sum);
   pthread_exit(NULL);
}
int main(int argc, char *argv[])
{
	struct thread_info threads_list[NUM_THREADS];
	pthread_t threads[NUM_THREADS];
	void * return_value;
   int rc, t, sum;
   sum=0;
   messages[0] = "Hello-0";
   messages[1] = "Hello-1";
   messages[2] = "Hello-2";
   messages[3] = "Hello-3";
   messages[4] = "Hello-4";
   messages[5] = "Hello-5";
   messages[6] = "Hello-6";
   messages[7] = "Hello-7";
   for(t = 0; t < NUM_THREADS; t++)
   {
   	sum = sum + t;
		threads_list[t].taskid = t;
		threads_list[t].sum = sum;
		threads_list[t].hello_msg = messages[t];

      pthread_create(&threads[t], NULL, PrintHello, &threads_list[t]);//
		printf("Creating thread %d\n", t);
      pthread_join(threads[t],NULL);//
   }
   pthread_exit(NULL);
}
