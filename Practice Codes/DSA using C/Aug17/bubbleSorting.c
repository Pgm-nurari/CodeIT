// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int n;
    printf("enter a limit: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n-1; j++) {
            if ( arr[j] > arr[j+1] ) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    printf("Array after bubble sorting: ");
    for (int i=0;i<n;i++) {
        printf("%d ",arr[i]);
    }
    
    return 0;
}