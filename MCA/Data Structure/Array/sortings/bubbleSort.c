#include<stdio.h>

void displayArray(int arr[], int size){
    for (int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }
}

void bubbleSort(int arr[], int size){
    for (int i = 0; i < size; i++){
        for(int j = 0; j < size - 1; j++){
            if (arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1]; 
                arr[j+1] = temp;
            }
        }
    }
}

int main(){

    int arr[11] = {2,4,59,-9,6,8,98,45,21,97,-12};
    int n = sizeof(arr)/sizeof(int);

    printf("\nArray before the bubble sort: ");
    displayArray(arr, n);
    
    printf("\nArray after the bubble sort: ");
    bubbleSort(arr,n);
    displayArray(arr,n);
    return 0;
}