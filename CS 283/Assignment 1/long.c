//Eric Lee
//Assignment 1.c
//Find how many bits a variable of type long int is.

#include <stdio.h>

int main(void)
{
	long *longType;
	int x = (int)longType; //0
	longType++;
	int y = (int)longType; //8
	
	printf("Long is: %d \n", (y-x));
	//sizeof(long) prints 8
}
