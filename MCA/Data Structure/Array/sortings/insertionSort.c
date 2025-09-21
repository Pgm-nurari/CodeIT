#include<stdio.h>

void displayArray(int arr[], int size){
    for (int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }
}

void insertionSort(int arr[], int size){
    
}

int main(){
    int arr[11] = {2,4,59,-9,6,8,98,45,21,97,-12};
    int n = sizeof(arr)/sizeof(int);

    printf("\nArray before the insertion sort: ");
    displayArray(arr, n);
    
    printf("\nArray after the insertion sort: ");
    insertionSort(arr,n);
    displayArray(arr,n);
    return 0;
}