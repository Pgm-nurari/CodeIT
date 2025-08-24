#include <stdio.h>
#include <stdbool.h>

int main() {
    int n, counter = 0;
    bool flag = false;
    int arr[100];

    printf("Enter the limit of the array: ");
    scanf("%d", &n);

    printf("\nEnter the elements:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            flag = false;
            if (arr[i] == arr[j]) {
                flag = true;
            }
            if (flag == true) {
                
            }
        }
    }

    printf("\nAfter removing duplicates: ");
    for (int i = 0; i < n - counter; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
