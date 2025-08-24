#include<stdio.h>
int main(){
    int myAge = 43; // an int variable

    printf("%d", myAge);  // Outputs the value of myAge (43)
    printf("%p", &myAge); // Outputs the memory address of myAge (0x7ffe5367e044)

    int *p = &myAge;
    printf("\n\n%p", p);

    printf("\n\n%d", *p);// fetching value using pointer
    *p = 55;
    printf("\n\n%d", myAge);
    return 0;
}