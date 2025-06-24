# prints out the first n fibonacci numbers using for loop.
def fibonacci(n):
    last_fibs = [1, 1]
    for i in range(n):
        if i < 2:
            print(last_fibs[i])
        else:
            new_fib = sum(last_fibs)
            last_fibs[0], last_fibs[1] = last_fibs[1], new_fib
            print(new_fib)


fibonacci(5)
