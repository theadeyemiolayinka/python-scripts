def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_result = [fibonacci(i) for i in range(10)]
print("Fibonacci Sequence:", fib_result)
