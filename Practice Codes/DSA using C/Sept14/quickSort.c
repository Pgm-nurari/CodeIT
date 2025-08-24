#include<stdio.h>

void swap(int *val1, int *val2){
    int temp = *val1;
    *val1 = *val2;
    *val2 = temp;
}
int partition(int arr[], int low, int high){
    int pivot = arr[low];
    int p = low+1; // for values greater than pivot.
    int q = high; // for values less than pivot.
    while (q>=p){
        while (q >= p && arr[q] >= pivot) {
            q--;
        }
        while (p <= q && arr[p] <= pivot) {
            p++;
        }
        if (q >= p) {
            swap(&arr[p], &arr[q]);
        }
    }
    swap(&arr[low],&arr[q]);
    return q;
}
void quickSort(int arr[], int low, int high){
    if (low<high){
        int pi = partition(arr,low,high);// Pivot index..
        quickSort(arr,low,pi-1);
        quickSort(arr,pi+1,high);
    }
}
int main(){
    int len = 5;
    int arr[] = {0,-9,8,4,-1};
    quickSort(arr,0,len-1);
    printf("\n");
    for (int i=0; i<len; i++){
        printf("%d ",arr[i]);
    }
    return 0;
}