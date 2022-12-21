def fibonacci(n):
    # Base cases
    if n <= 1:
        return n

    # recurrence relation
    return fibonacci(n - 1) + fibonacci(n - 2)

    # Driver code to test above methods
n = 9
print(fibonacci(n))

def lucas(n):
    # Base cases
    if n == 0:
        return 2;
    if n == 1:
        return 1;

    # recurrence relation
    return lucas(n - 1) + lucas(n - 2);


# Driver code to test above methods
n = 9;
print(lucas(n));


def sum_series(n, num1=0, num2=1):
    #Base cases
    if num1 == 0 and num2 == 1:
        return fibonacci(n)
    if num1 == 2 and num2 == 1:
        #print("hi")
        return lucas(n)
    else:
        if n == 0:
            return num1
        if n == 1:
            return num2
        #print(num1, num2)


    # recurrence ralation
        return sum_series(n-1, num1, num2) + sum_series(n-2, num1, num2)
         #sum_series(num - 1, a, b) + sum_series(num - 2, a, b)

# Driver code to test above methods
#print(sum_series(9))
print(sum_series(5, 3, 4))
