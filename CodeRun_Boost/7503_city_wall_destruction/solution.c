#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Simple stack implementation for integers (indices)
typedef struct {
    int* data;
    int top;
    int capacity;
} Stack;

Stack* createStack(int capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->data = (int*)malloc(sizeof(int) * capacity);
    stack->top = -1;
    return stack;
}

bool isEmpty(Stack* stack) {
    return stack->top == -1;
}

void push(Stack* stack, int item) {
    stack->data[++stack->top] = item;
}

int pop(Stack* stack) {
    return stack->data[stack->top--];
}

int peek(Stack* stack) {
    return stack->data[stack->top];
}

void clearStack(Stack* stack) {
    stack->top = -1;
}

void freeStack(Stack* stack) {
    free(stack->data);
    free(stack);
}

// Corrected solve function signature: 'a' parameter is now long long int*
long long solve(int n, long long int* a) {
    int* left_smaller = (int*)malloc(sizeof(int) * n);
    int* right_smaller = (int*)malloc(sizeof(int) * n);
    int* left_greater = (int*)malloc(sizeof(int) * n);
    int* right_greater = (int*)malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++) {
        left_smaller[i] = -1;
        left_greater[i] = -1;
        right_smaller[i] = n;
        right_greater[i] = n;
    }

    Stack* stack = createStack(n);

    for (int i = 0; i < n; i++) {
        while (!isEmpty(stack) && a[peek(stack)] > a[i]) {
            pop(stack);
        }
        left_smaller[i] = isEmpty(stack) ? -1 : peek(stack);
        push(stack, i);
    }

    clearStack(stack);
    for (int i = n - 1; i >= 0; i--) {
        while (!isEmpty(stack) && a[peek(stack)] > a[i]) {
            pop(stack);
        }
        right_smaller[i] = isEmpty(stack) ? n : peek(stack);
        push(stack, i);
    }

    clearStack(stack);
    for (int i = 0; i < n; i++) {
        while (!isEmpty(stack) && a[peek(stack)] < a[i]) {
            pop(stack);
        }
        left_greater[i] = isEmpty(stack) ? -1 : peek(stack);
        push(stack, i);
    }

    clearStack(stack);
    for (int i = n - 1; i >= 0; i--) {
        while (!isEmpty(stack) && a[peek(stack)] < a[i]) {
            pop(stack);
        }
        right_greater[i] = isEmpty(stack) ? n : peek(stack);
        push(stack, i);
    }

    long long result = 0;
    for (int i = 0; i < n; i++) {
        long long max_count = (long long)(i - left_greater[i]) * (right_greater[i] - i);
        long long min_count = (long long)(i - left_smaller[i]) * (right_smaller[i] - i);
        // Cast a[i] to long long to ensure multiplication is done in long long
        result += (long long)a[i] * (max_count - min_count);
    }

    free(left_smaller);
    free(right_smaller);
    free(left_greater);
    free(right_greater);
    freeStack(stack);

    return result;
}