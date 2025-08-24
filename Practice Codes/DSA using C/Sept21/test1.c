#include<stdio.h>
int main(){
	int *ptr1,*ptr2;
	printf("Enter 2 numbers: ");
	scanf("%d%d",ptr1,ptr2);
	if (*ptr1>*ptr2){ printf("\nGreatest is %d",*ptr1); }
	else { printf("\nGreatest is %d\n",*ptr2); }
	return 0;
}
