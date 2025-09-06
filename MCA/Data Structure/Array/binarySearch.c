#include<stdio.h>

void displayArray(int arr[], int limit){
    printf("Displaying the array: ");
    for (int i=0; i<=limit; i++){
        printf("%d ", arr[i]);
    }
}

int binarySearch(int arr[], int limit, int val){
    int low = 0;
    int high = limit;
    int mid;

    while(high>low){
        mid = (low+high)/2;
        if (val>arr[mid]){
            low = mid + 1;
        }
        else if (val<arr[mid]){
            high = mid - 1;
        }
        else{
            return mid + 1;
        }
    }
    return -1;
}

int main(){

    int arr[10] = {3,3,3,4,6,6,7,8,24,0};

    int limit = 8;

    displayArray(arr,limit);

    int pos, val;
    printf("\nEnter the value to be searched: ");
    scanf("%d", &val);

    pos = binarySearch(arr, limit, val);
    if (pos==-1){
        printf("\nNo such value exists in array!!");
    }
    else{
        printf("\n%d first found at position %d.", val, pos);
    }
    
    return 0;
}