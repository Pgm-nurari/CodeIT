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

int linearSearch(int arr[], int limit, int value){
    for ( int i = 0; i<=limit; i++){
        if(arr[i]==value){
            return i+1;
        }
    }
    return -1;
}

int main(){

    int limit=7; //takes values from 0
    int arr[10] = {10,20,30,40,50,60,70,80,0,0};    

    displayArray(arr,limit);

    int pos, val;
    printf("\nEnter the value to be searched: ");
    scanf("%d", &val);

    pos = linearSearch(arr, limit, val);
    if (pos==-1){
        printf("\nNo such value exists in array!!");
    }
    else{
        printf("\n%d first found at position %d.", val, pos);
    }

    return 0;
}