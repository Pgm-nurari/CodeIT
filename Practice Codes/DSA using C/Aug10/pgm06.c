//greatest element in an array
#include<stdio.h>
void main(){
	int n,greatest=0;
	printf("Enter the limit of the array: ");
	scanf("%d",&n);
	int arr[n];
	printf("\nEnter the elements: \n");
	for (int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	for (int i=0;i<n;i++){
		if (greatest<arr[i]){ greatest = arr[i];}
	}
	printf("Greatest is %d",greatest);
}
