#include <stdio.h>
#include <stdlib.h>

int getLastIndex(int arr[], int size){
    int lastValue = -1;
    for (int i=0; i<size; i++){
        if (arr[i] > 0) {
            lastValue = i;
        } else {
            break;
        }
    }
    return lastValue;
}

void displayArray(int arr1[], int size){
    printf("\n");
    for (int i = 0; i < size; i++){
        printf(" %d", arr1[i]);
    }
}

void insertInIndex(int arr1[], int size, int position, int value){
    int index = position - 1;  // convert to 0-based
    int lp = getLastIndex(arr1, size);

    if (index < 0 || index > lp+1) {
        printf("\nInvalid position!");
        return;
    }
    if (lp == size - 1) {
        printf("\nArray is full!");
        return;
    }

    for (int i = lp; i >= index; i--) {
        arr1[i+1] = arr1[i];
    }
    arr1[index] = value;

    printf("\nValue inserted");
    displayArray(arr1, size);
}

void deleteAtIndex(int arr1[], int size, int position){
    int index = position - 1;
    if (index<1 || index>size){
        printf("\nInvalid index. Not in the range of the array");
    }
    else if (index==size) {
        int delValue = arr1[index-1];
        arr1[index-1] = 0;
        printf("\nThe number deleted is %d", delValue);
    }
    else{
        int delValue = arr1[index-1];
        for (int i=index-1;i<size-1;i++){
            if (arr1[i+1]!=0)
                arr1[i]=arr1[i+1];
            else
                arr1[i]=0;
        }
        arr1[size-1]=0;
        printf("\nThe number deleted is %d", delValue);
    }
    
}


int main(){
    int arr[10] = {10,20,40,50,60,70,80,90,100,0};
    int size = sizeof(arr) / sizeof(arr[0]);

    displayArray(arr, size);

    insertInIndex(arr, size, 3, 10000);  // Insert at position 3

    return 0;
}
