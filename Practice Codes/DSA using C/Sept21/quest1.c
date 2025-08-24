#include<stdio.h>
int main(){
	int a,*ptr1,b, *ptr2,sum =0;
	printf("Enter a number: ");
	scanf("%d",&a);
	ptr1 = &a;
	printf("Enter a number: ");	
	scanf("%d",&b);	
	ptr2 = &b;
	sum = *ptr1+*ptr2;
	printf("\nSum of the 2 numbers is: %d",sum);
	return 0;
}	
