#include <stdio.h>



// This is the hello world program written in c.
// To compile and run this we cas use this command
// `gcc c_ptr.c && ./a.out`

void main(void)
{
    int x = 50;
    int *p = &x;
    printf("Pointer to address of x: %p\n", p);
}
