#include<stdio.h>
int main(){
	int arr[5],*arr_ptr;
	arr_ptr = &arr;
	printf("Enter 5 elements in the array: ");
	for (int i=0;i<5;i++){
		scanf("%d",arr_ptr);
	}	
	int *ptr1,sum = 0;
	ptr1 = &sum;
	for (int i=0;i<5;i++){
		*ptr1 = *ptr1 + *arr_ptr;
		arr_ptr++;
	}
	printf("\nSum is: %d",*ptr1);
	return 0;
}
