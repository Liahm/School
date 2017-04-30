//Eric Lee
//Assignment 1.a
//Read a file and print the last line first.

#include <stdio.h>
#define SIZE 128

int main (void)
{
    int ch; //int variable for ASCII values
    char line[SIZE];
    //char *buffer;

    FILE * fp = fopen("test.txt", "r");

    if (fp == NULL)
    {
        return;
    }
    //Read each line of the file, and print it to screen
    fseek(fp, 0, SEEK_END);
    while(ftell(fp) > 1) //return current file position as long as it is greater than 1
    {
        fseek(fp, -2, SEEK_CUR); //sets the file position of fp to -2 in the current pos of the pointer.
        if(ftell(fp) <= 1) //Less than 2 or 0 also works. But if there are blank lines it will get annoying.
            break;
        ch =fgetc(fp); //int read byte by byte
        int count =0;
        while(ch != '\n')//blank line
        {
            line[count++] = ch;
            if(ftell(fp) < 2) //if fp is less than 1, break it. because it's going to be blank
                break;
            fseek(fp, -2, SEEK_CUR); //Move it to -2 of current
            ch = fgetc(fp);
        }
        for(int i = count -1; i>= 0 && count > 0; i--) //loop as long as the "reverse" is not EOF
            printf("%c", line[i]); //print
        printf("\n");
    }
    fclose(fp);
}