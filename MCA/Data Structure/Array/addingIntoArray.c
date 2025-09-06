#include<stdio.h>

void initializeArray(int arr[], int size){
    for (int i=0; i<size; i++){
        arr[i] = 0;
    }
}

void displayArray(int arr[], int limit){
    printf("Displaying the array: ");
    for (int i=0; i<limit; i++){
        printf("%d ", arr[i]);
    }
}

void addingValuesToLimit(int arr[], int limit){
    printf("Enter the new values: ");
    for (int i=0; i<limit; i++){
        scanf("%d ", &arr[i]);
    }
}

int main(){

    int n = 10;
    int arr[n];
    initializeArray(arr, n);

    int limit;
    printf("Enter the limit ( < = %d ): ", n);
    scanf("%d",&limit);
    addingValuesToLimit(arr,limit);
    displayArray(arr,n);

    return 0;
}