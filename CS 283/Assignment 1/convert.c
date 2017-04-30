//Eric Lee
//Assignmnet 1.b
//Receive a decimal and transform it into a binary

#include <stdio.h>

int main(void)
{
	long decimal,decimalTwo ,binary =0, i=1;//variables in long
	//because of the use of mod
	int remainder;	
	scanf("%ld", &decimal);	//get decimal
	decimalTwo = decimal; //decimalTwo to print for user.
	while(decimal != 0) 
	{
		remainder = decimal%2; //remainder
		decimal = decimal/2; //more math
		binary = binary + (remainder*i); //binary equation
		i = i*10;
	}
	printf("Your number %ld is %ld", decimalTwo, binary);
	printf("\n");
	return 0;
	
}
