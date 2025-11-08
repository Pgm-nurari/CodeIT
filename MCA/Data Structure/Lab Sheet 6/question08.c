#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Deque {
    int front, rear, size;
    int *arr;
} Deque;

void initialize(Deque *dq, int size) {
    dq->size = size;
    dq->front = -1;
    dq->rear = -1;
    dq->arr = (int *)malloc(size * sizeof(int));
    if (dq->arr == NULL) {
        printf("\nMemory allocation failed!");
        exit(1);
    }
}

bool isFull(Deque *dq) {
    return (dq->rear + 1) % dq->size == dq->front;
}

bool isEmpty(Deque *dq) {
    return dq->front == -1;
}

void insertFront(Deque *dq) {
    if (isFull(dq)) {
        printf("\nDeque Overflow\n");
    } else {
        int data;
        printf("Enter data to insert at front: ");
        scanf("%d", &data);
        if (isEmpty(dq)) {
            dq->front = 0;
            dq->rear = 0;
        } else {
            dq->front = (dq->front - 1 + dq->size) % dq->size;
        }
        dq->arr[dq->front] = data;
        printf("%d inserted at front\n", data);
    }
}

void insertRear(Deque *dq) {
    if (isFull(dq)) {
        printf("\nDeque Overflow\n");
    } else {
        int data;
        printf("Enter data to insert at rear: ");
        scanf("%d", &data);
        if (isEmpty(dq)) {
            dq->front = 0;
            dq->rear = 0;
        } else {
            dq->rear = (dq->rear + 1) % dq->size;
        }
        dq->arr[dq->rear] = data;
        printf("%d inserted at rear\n", data);
    }
}

int deleteRear(Deque *dq) {
    int data = dq->arr[dq->rear];
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else {
        dq->rear = (dq->rear - 1 + dq->size) % dq->size;
    }
    return data;
}

void display(Deque *dq) {
    if (isEmpty(dq)) {
        printf("\nDeque is empty\n");
    } else {
        printf("\nDeque (Front to Rear):\nFRONT -> ");
        int i = dq->front;
        while (1) {
            printf("%d ", dq->arr[i]);
            if (i == dq->rear) {
                break;
            }
            i = (i + 1) % dq->size;
        }
        printf("<- REAR\n");
    }
}

int main() {
    int n, choice, val;
    Deque dq;
    printf("\nEnter the size of the deque: ");
    scanf("%d", &n);
    initialize(&dq, n);

    while (1) {
        printf("\n--- Output Restricted Deque (Output at Rear) ---\n");
        printf("1. Insert at Front\n");
        printf("2. Insert at Rear\n");
        printf("3. Delete from Rear\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("--------------------------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("\nInvalid input. Please enter a number.\n");
            continue;
        }

        switch (choice) {
            case 1:
                insertFront(&dq);
                break;
            case 2:
                insertRear(&dq);
                break;
            case 3:
                if (isEmpty(&dq)) {
                    printf("\nDeque Underflow\n");
                } else {
                    val = deleteRear(&dq);
                    printf("\nDeleted %d from rear\n", val);
                }
                break;
            case 4:
                display(&dq);
                break;
            case 5:
                printf("\nExiting. Freeing memory...\n");
                free(dq.arr);
                exit(0);
            default:
                printf("\nInvalid choice. Please enter 1-5.\n");
        }
    }
    return 0;
}