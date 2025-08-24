//dynamic structure creation 

#include<stdio.h> 
#include<stdlib.h> 
#include<string.h> 

struct student 

{ 

   int regno; 
   char sname[5]; 

}; 

int main() 

{ 

  struct student *ptr; 

  int i; 

  // Allocates the memory for 2 structures with pointer ptr pointing to the base address. 

  ptr=(struct student *)malloc(2*sizeof(struct student)); 
   
  if (ptr == NULL)
  {
    printf("Allocation failed !!!");
    exit(0);
  }
  else
  {
    for(i = 0; i < 2; ++i) 
    { 
       strcpy((ptr+i)->sname,"Ayan"); 
       (ptr+i)->regno = (100+i); 
    } 

   printf("Displaying Information:\n"); 
   for(i = 0; i < 2 ; ++i) 
       printf("%s\t%d\n", (ptr+i)->sname, (ptr+i)->regno); 
  }
  free(ptr);   

 return 0; 

}