#include<stdio.h>
int main(){
	int a, b, temp, *ptr1,*ptr2,*ptr3;
	ptr1 = &a; ptr2=&b; ptr3 = &temp;
	printf("Enter 2 numbers: ");
	scanf("%d%d",ptr1,ptr2);
	printf("\nBefore swapping,\na=%d\nb=%d",*ptr1,*ptr2);	
	*ptr3 = *ptr1;
	*ptr1 = *ptr2;
	*ptr2 = *ptr3;
	printf("\nAfter swapping,\na=%d\nb=%d",*ptr1,*ptr2);
	printf("\n");
	return 0;
}
