// Binary searching using Iteration

/*
    do until the pointers low and high meet each other.
        mid = (low + high)/2
        if (x == arr[mid])
            return mid
        else if (x > arr[mid]) // x is on the right side
            low = mid + 1
        else                       // x is on the left side
            high = mid - 1
*/

#include<stdio.h>

int main(){

    int n, temp=0;
    int value;

    printf("Enter the limit: ");
    scanf("%d",&n);
    int arr[n];

    printf("\nEnter the elements: \n");
    for (int i=0;i<n;i++) {
        printf("Element %d: ",i+1);
        scanf("%d",&arr[i]);        
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n-1-i; j++) {
            if ( arr[j] > arr[j+1] ) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }    

    printf("\nEnter what you wanna search: ");
    scanf("%d",&value);

    int low = 0;
    int high = n-1;

    while (low <= high) {
        int mid = (low + high)/2;
        if (arr[mid] == value) {
            printf("\nThe index of %d is %d\n",value,mid);
            break;
        }
        else if (arr[mid]>value) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }

    }

    return 0;
}