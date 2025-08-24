
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

    for (int i=1;i<n;i++) {
        int temp = arr[i];
        for (int j=i-1;j>=0;j--){
            if (arr[j] > temp) {
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
            else { continue;}
        }
    }
    
    printf("Array after bubble sorting: ");
    for (int i=0;i<n;i++) {
        printf("%d ",arr[i]);
    }
    
    return 0;
}