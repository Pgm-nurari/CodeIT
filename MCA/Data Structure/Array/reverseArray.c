#include<stdio.h>

void initializeArray(int arr[], int size){
    for (int i=0; i<size; i++){
        arr[i] = 0;
    }
}

void displayArray(int arr[], int limit){
    printf("Displaying the array: ");
    for (int i=0; i<=limit; i++){
        printf("%d ", arr[i]);
    }
}

void reverseArray(int arr[], int limit){
    for (int i=0; i<=(limit/2); i++){
        int temp = arr[i];
        arr[i] = arr[limit-i];
        arr[limit - i] = temp;
    }
}

int main(){

    int limit=7; //takes values from 0
    int arr[10] = {10,20,30,40,50,60,70,80,0,0};    

    displayArray(arr,limit);

    printf("\nReversed Array is: ");
    
    reverseArray(arr, limit);
    displayArray(arr,9);


    return 0;
}