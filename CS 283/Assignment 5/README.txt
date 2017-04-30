1)
Added command line arguments to hello.c from the book.

Looped the reading code by the number of times the user inputs.

To run hello.c
gcc hello.c -o hello csapp.c -pthread

./hello <value>



2.)

a)It's not printing anything because it's never "calling" the thread()
function. 
To call it it requires Pthread_join, which should be implemented
in line 10, before exit. Since it currently doesn't exit it will just run
main(), which only exits.


b) Added pthread_join to the code.
to run
gcc hellobug.c -o bug csapp.c -pthread
./bug  


3)hello-hw.txt contained no calls to the other function. Even if it did the other function never defined the variables.
Defined variables, created a struct for the variables since we weren't allowed to delete them. create a thread and joined them.

dotpr-hw.txt
Threads weren't created, wouldn't be joined, variables weren't defined correctly.
Defined variables and math.
Created threads and joined in separate loops so that it can wait