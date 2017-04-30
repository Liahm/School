#include <stdio.h> 
#include <stdlib.h> 

int main () 
 {
  char * buf;
  int num;
  num = 1 << 29;
  buf = malloc(num) ;
  fgets (buf, 1024, stdin) ;
  printf ("%s\n", buf) ;
  return(1);
 }


/*
Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7a7cd27 in __GI__IO_getline_info (
    fp=fp@entry=0x7ffff7dd18e0 <_IO_2_1_stdin_>, buf=buf@entry=0x0, n=1023,
    delim=delim@entry=10, extract_delim=extract_delim@entry=1,
    eof=eof@entry=0x0) at iogetline.c:70
70      iogetline.c: No such file or directory.
In other words, 31 is too much
*/