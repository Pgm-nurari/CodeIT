//Sum of the elements in an array
#include<stdio.h>
void main(){
	int n,sum=0;
	printf("Enter the limit of the array: ");
	scanf("%d",&n);
	int arr[n];
	printf("\nEnter the elements: \n");
	for (int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	for (int i=0;i<n;i++){
		sum+=arr[i];
	}
	printf("\nSum of the elements in the array is: %d\n",sum);
}
