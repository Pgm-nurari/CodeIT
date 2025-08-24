#include <stdio.h>

int main() {
    int n,index = 0;
    printf("enter a limit: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
    }

    for (int i=0; i<n-1; i++){
        index = i;
        // Searching the smallest element
        for (int j=i+1; j<n; j++){
            if (arr[j]<arr[index]){ 
                index = j;
            }
            else{ continue; }
        }
        // Swapping the 2 elements
        int temp = arr[i];
        arr[i] = arr[index];
        arr[index] = temp;
    }

    printf("Array after selection sorting: ");
    for (int i=0;i<n;i++) {
        printf("%d ",arr[i]);
    }
    
    return 0;
}
