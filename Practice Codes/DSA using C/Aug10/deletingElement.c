//Linear Deletion...
#include<stdio.h>
#include<stdbool.h>
void main(){
	int n,value,index;
	bool flag = false;
	printf("Enter the limit of the array: ");
	scanf("%d",&n);
	int arr[n];int arr2[n-1];
	printf("\nEnter the elements: \n");
	for (int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	printf("Enter the value: ");
	scanf("%d",&value);
	for (int i=0;i<n;i++){
		if (value==arr[i]){
			 flag = true;
		}
		if (flag==true && i!=n-1){
			arr[i]=arr[i+1];
		}
	}
	if (flag == true){
		printf("After deleting the new array is: ");
		for (int j=0;j<n-1;j++){
			printf("%d, ",arr[j]);
		}
		printf("\n");
	}else{
		printf("%d not in the list",value);
	}
}
