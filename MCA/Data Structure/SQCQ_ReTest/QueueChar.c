#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Queue {
    int front, rear, size;
    char *arr;
} Queue;

void initialize(Queue *q, int size) {
    q->size = size;
    q->front = -1;
    q->rear = -1;
    q->arr = (char *)malloc(size * sizeof(char));
    if (q->arr == NULL) {
        printf("\nMemory allocation failed!");
        exit(1);
    }
}

bool isFull(Queue *q) {
    return q->rear == q->size - 1;
}

bool isEmpty(Queue *q) {
    return q->front == -1;
}

void enqueue(Queue *q) {
    if (isFull(q)) {
        printf("\nQueue Overflow\n");
    } else {
        char data;
        printf("Enter data: ");
        scanf(" %c", &data);
        if (isEmpty(q)) {
            q->front = 0;
        }
        q->rear++;
        q->arr[q->rear] = data;
        printf("%c enqueued to queue\n", data);
    }
}

char dequeue(Queue *q) {
    char data = q->arr[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front++;
    }
    return data;
}

void display(Queue *q) {
    if (isEmpty(q)) {
        printf("\nQueue is empty\n");
    } else {
        printf("\nQueue (Front to Rear):\nFRONT -> ");
        for (int i = q->front; i <= q->rear; i++) {
            printf("%c ", q->arr[i]);
        }
        printf("<- REAR\n");
    }
}

void peek(Queue *q) {
    if (isEmpty(q)) {
        printf("\nQueue is empty\n");
    } else {
        printf("\nFront element is: %c\n", q->arr[q->front]);
    }
}

int main() {
    int n, choice;
    char dequeued_val;
    Queue q;
    printf("\nEnter the size of the queue: ");
    scanf("%d", &n);
    initialize(&q, n);

    while (1) {
        printf("\n--- Linear Queue Menu (Array/char) ---\n");
        printf("1. Enqueue (Add)\n");
        printf("2. Dequeue (Remove)\n");
        printf("3. Display\n");
        printf("4. Peek (Show Front)\n");
        printf("5. Exit\n");
        printf("----------------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("\nInvalid input. Please enter a number.\n");
            continue;
        }

        while (getchar() != '\n');

        switch (choice) {
            case 1:
                enqueue(&q);
                break;
            case 2:
                if (isEmpty(&q)) {
                    printf("\nQueue Underflow! Cannot dequeue.\n");
                } else {
                    dequeued_val = dequeue(&q);
                    printf("\nDequeued element: %c\n", dequeued_val);
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