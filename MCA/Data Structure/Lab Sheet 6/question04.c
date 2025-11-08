#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_NAME_LENGTH 50

typedef struct Queue {
    int front, rear, size;
    char **arr;
} Queue;

void initialize(Queue *q, int size) {
    q->size = size;
    q->front = -1;
    q->rear = -1;
    q->arr = (char **)malloc(size * sizeof(char *));
    if (q->arr == NULL) {
        printf("\nMemory allocation failed (array of pointers)!");
        exit(1);
    }
    for (int i = 0; i < size; i++) {
        q->arr[i] = (char *)malloc(MAX_NAME_LENGTH * sizeof(char));
        if (q->arr[i] == NULL) {
            printf("\nMemory allocation failed (string %d)!", i);
            exit(1);
        }
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
        char data[MAX_NAME_LENGTH];
        printf("Enter name to enqueue: ");
        scanf(" %[^\n]s", data); 
        
        if (isEmpty(q)) {
            q->front = 0;
        }
        q->rear++;
        strcpy(q->arr[q->rear], data);
        printf("\"%s\" enqueued to queue\n", data);
    }
}

char* dequeue(Queue *q) {
    char* data = q->arr[q->front];
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
            printf("\"%s\" ", q->arr[i]);
        }
        printf("<- REAR\n");
    }
}

int main() {
    int n, choice;
    char* dequeued_val;
    Queue q;
    printf("\nEnter the size of the name queue: ");
    scanf("%d", &n);
    initialize(&q, n);

    while (1) {
        printf("\n--- Name Queue Menu (Array) ---\n");
        printf("1. Enqueue (Add)\n");
        printf("2. Dequeue (Remove)\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("----------------------------------\n");
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
                    printf("\nDequeued name: %s\n", dequeued_val);
                }
                break;
            case 3:
                display(&q);
                break;
            case 4:
                printf("\nExiting. Freeing memory...\n");
                for (int i = 0; i < q.size; i++) {
                    free(q.arr[i]);
                }
                free(q.arr);
                exit(0);
            default:
                printf("\nInvalid choice. Please enter 1-4.\n");
        }
    }
    return 0;
}