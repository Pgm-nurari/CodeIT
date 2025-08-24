#include  <stdio.h> 
#include<stdlib.h> 

int main() 
{ 

   int *ptr=NULL,i,n; 

   //dynamic array creation using malloc 

   ptr=(int *)malloc(5*sizeof(int));  // 5 memory address allocated contiguously in a single block 
 
   printf("\n Allocated addresses:    "); 

   for (i=0;i<5;i++) 

        printf("%p  ",ptr+i); 

    printf("\n"); 

     // check if memory has been allocated successfully 

   if(ptr==NULL)  // memory not allocated 
   { 

      printf("Memory not allocated"); 

      exit(0); 

   } 

   else 
   { 

       printf("\n Enter Array elements : - "); 

        for (i=0;i<5;i++) 

            *(ptr+i)=(rand() % (100 - 2 + 1)) + 2; 

        printf("\n The array values are :    "); 

        for (i=0;i<5;i++) 

            printf("%d  ",ptr[i]); 

        printf("\n"); 
        
        free(ptr); // release the memory allocated to ptr 

        return 0; 

    } 

}