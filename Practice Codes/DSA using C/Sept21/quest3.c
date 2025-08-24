#include<stdio.h>
int main(){
	int a, b, *ptr1,*ptr2;
	ptr1 = &a; ptr2=&b; 
	printf("Enter 2 numbers: ");
	scanf("%d%d",ptr1,ptr2);
	if (*ptr1>*ptr2){ printf("\nGreatest is %d",*ptr1); }
	else { printf("\nGreatest is %d\n",*ptr2); }
	return 0;
}
