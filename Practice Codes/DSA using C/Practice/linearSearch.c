//Linear Searching...
#include<stdio.h>
#include<stdbool.h>
void main(){
	int n,value,index;
	bool flag = false;
	printf("Enter the limit of the array: ");
	scanf("%d",&n);
	int arr[n];
	printf("\nEnter the elements: \n");
	for (int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	printf("Enter the value: ");
	scanf("%d",&value);
	for (int i=0;i<n;i++){
		if (value==arr[i]){ index = i;flag = true;break;}
	}
	if (flag == true){
		printf("Index of %d is %d",value,index);
	}else{
		printf("%d not in the list",value);
	}
}
