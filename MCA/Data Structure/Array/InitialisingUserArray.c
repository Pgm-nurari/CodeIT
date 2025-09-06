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

int main(){

    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int arr[n];

    initializeArray(arr, n);
    displayArray(arr,n);

    return 0;
}