#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct CQueue {
    int front, rear, size;
    int *arr;
} CQueue;

void initialize(CQueue *q, int size) {
    q->size = size;
    q->front = -1;
    q->rear = -1;
    q->arr = (int *)malloc(size * sizeof(int));
    if (q->arr == NULL) {
        printf("\nMemory allocation failed!");
        exit(1);
    }
}

bool isFull(CQueue *q) {
    return (q->rear + 1) % q->size == q->front;
}


bool isEmpty(CQueue *q) {
    return q->front == -1;
}

void enqueue(CQueue *q) {
    if (isFull(q)) {
        printf("\nQueue Overflow\n");
    } else {
        int data;
        printf("Enter data: ");
        scanf("%d", &data);
        if (isEmpty(q)) {
            q->front = 0;
        }
        q->rear = (q->rear + 1) % q->size;
        q->arr[q->rear] = data;
        printf("%d enqueued to queue\n", data);
    }
}


int dequeue(CQueue *q) {
    int data = q->arr[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % q->size;
    }
    return data;
}


void display(CQueue *q) {
    if (isEmpty(q)) {
        printf("\nQueue is empty\n");
    } else {
        printf("\nQueue (Front to Rear):\nFRONT -> ");
        int i = q->front;
        while (1) {
            printf("%d ", q->arr[i]);
            if (i == q->rear) {
                break;
            }
            i = (i + 1) % q->size;
        }
        printf("<- REAR\n");
    }
}

void peek(CQueue *q) {
    if (isEmpty(q)) {
        printf("\nQueue is empty\n");
    } else {
        printf("\nFront element is: %d\n", q->arr[q->front]);
    }
}

int main() {
    int n, choice, dequeued_val;
    CQueue q;
    printf("\nEnter the size of the circular queue: ");
    scanf("%d", &n);
    initialize(&q, n);

    while (1) {
        printf("\n--- Circular Queue Menu (Array/int) ---\n");
        printf("1. Enqueue (Add)\n");
        printf("2. Dequeue (Remove)\n");
        printf("3. Display\n");
        printf("4. Peek (Show Front)\n");
        printf("5. Exit\n");
        printf("-----------------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("\nInvalid input. Please enter a number.\n");
            continue;
        }

        switch (choice) {
            case 1:
                enqueue(&q);
                break;
            case 2:
                if (isEmpty(&q)) {
                    printf("\nQueue Underflow! Cannot dequeue.\n");
                } else {
                    dequeued_val = dequeue(&q);
                    printf("\nDequeued element: %d\n", dequeued_val);
                }
                break;
            case 3:
                display(&q);
                break;
            case 4:
                peek(&q);
                break;
            case 5:
                printf("\nExiting. Freeing memory...\n");
                free(q.arr);
                exit(0);
            default:
                printf("\nInvalid choice. Please enter 1-5.\n");
        }
    }
    return 0;
}