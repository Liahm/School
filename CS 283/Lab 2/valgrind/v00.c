#include <stdlib.h>

void f ()
 {
  int *x;
  x = malloc(10 * sizeof(int));

  free(x);
 }

int main ()
 {
  f();
  return 0;
 }
