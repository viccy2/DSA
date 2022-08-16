# implementing Fibonacci sequence using while loop
def fibonacci(n):
    val1 = 1
    val2 = 1
    count = 0
    if n <= 0:
        print('enter positive number')
        return
    if n == 1:
        return n
    else:
        while count < n:
            print(val1, end=' ')
            val3 = val1 + val2
            val1 = val2
            val2 = val3
            count += 1


fibonacci(3)
