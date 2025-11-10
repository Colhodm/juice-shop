#!/usr/bin/env python3

def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n_terms = 15
print(f"Fibonacci sequence (first {n_terms} numbers):")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
print()

print(f"\nThe 10th Fibonacci number is: {fibonacci(10)}")
print(f"The 20th Fibonacci number is: {fibonacci(20)}")
