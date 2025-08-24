//Linear Deletion...
#include<stdio.h>
#include<stdbool.h>
void main(){
	int n,counter=0;
	bool flag = false;
	int arr[100];
	
	printf("Enter the limit of the array: ");
	scanf("%d",&n);

	printf("\nEnter the elements: \n");
	for (int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}

	for (int i=0;i<n;i++){
		for (int j=i+1;j<n-1;j++){
			if (arr[i]==arr[j]){
				printf("\narr[ i = %d] = %d, arr[ j = %d] = %d ",i,arr[i],j,arr[j]);
				flag = true;
				break;
			}
		if (flag == true){
			for (int k=j;k<n-1-counter;k++){
				arr[k]=arr[k+1];	
			}
			flag = false;
			counter++;
			i--;
			printf(" counter = %d",counter);
		}
		}
	}
	
	printf("\nAfter removing duplicates");
	for (int i=0;i<n-counter+1;i++){
		printf("%d",arr[i]);
	}

}
