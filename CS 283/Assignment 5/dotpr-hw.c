#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "csapp.h"
#define NUMTHRDS 4
#define VECLEN 100000
pthread_t callThd[NUMTHRDS];
double *array_a;
double *array_b;
double big_sum;
int veclen;
void *dotprod(void *arg)
{
	double mysum, *x, *y;
	long offset;
	int i, start, end;
   x = array_a;
   y = array_b;
   offset = (long)arg;

	start = offset*veclen;
	end = start + veclen;

   mysum = 0;
   for (i=start; i<end ; i++)
   {
   	mysum += (x[i] * y[i]);
   }
   big_sum += mysum;
	printf("Thread %ld did %d to %d: mysum= %f global sum= %f\n", offset,start, end, mysum, big_sum);
}
int main (int argc, char *argv[])
{
	long i;
   double *a, *b;
   void *status;
   a = (double*) malloc (NUMTHRDS*VECLEN*sizeof(double));
   b = (double*) malloc (NUMTHRDS*VECLEN*sizeof(double));
   for (i=0; i<VECLEN*NUMTHRDS; i++)
   {
  		a[i]=1;
      b[i]=a[i];
   }
	veclen = VECLEN;
   array_a = a;
   array_b = b;
   big_sum = 0;
   /* ... */
   /* create threads */
   /* ... */
   for(i=0;i<NUMTHRDS;i++)
   {
		pthread_create(&callThd[i], NULL, dotprod, (void *)i);
   	/* Each thread works on a different set of data.
      The offset is specified by 'i'. The size of
      the data for each thread is indicated by VECLEN.
      */
   }
   /* Wait on the other threads */
   for(i=0; i<NUMTHRDS; i++)
	{
		pthread_join(callThd[i], &status);
	}
   printf ("Sum = %f \n", big_sum);
   free (a);
   free (b);
}
