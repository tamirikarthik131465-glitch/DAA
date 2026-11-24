
# Factorial using Iterative Method
def iterative_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Factorial using Recursive Method
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)


# Main Program
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("\nUsing Iterative Method:")
    print("Factorial =", iterative_factorial(n))

    print("\nUsing Recursive Method:")
    print("Factorial =", recursive_factorial(n))


# Time and Space Complexity
print("\nTime and Space Complexity:")
print("Iterative: Time = O(n), Space = O(1)")
print("Recursive: Time = O(n), Space = O(n)")
