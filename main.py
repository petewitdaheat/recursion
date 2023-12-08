from loops import *
from recursion import *

print ("Factorial of 6 using a loop is:", loops.factorial(6))
print ("Factorial of 6 using a loop is:", loops.factorial(5))
print ("Factorial of 6 using a loop is:", loops.factorial(1))

print ("Factorial of 6 using recursion is:", recursion.factorial(6))
print ("Factorial of 6 using recursion is:", recursion.factorial(5))
print ("Factorial of 6 using recursion is:", recursion.factorial(1))

print("2 to the 5th power using a loop is :", loops.power(2, 5))
print("2 to the 4th power using a loop is :", loops.power(2, 4))
print("2 to the 0 power using a loop is :", loops.power(2, 0))

print("2 to the 5th power using recursion is :", recursion.power(2, 5))
print("2 to the 4th power using recursion is :", recursion.power(2, 4))
print("2 to the 0 power using recursion is :", recursion.power(2, 0))

nums = [5, 12, 3, 4]
print("Minimum number using a loop is:", loops.computeMin(nums))
print("Minimum number using recursion is:", recursion.computeMin(nums, 0, nums[0]))

s = "CAT"
loops.reverse(s)
recursion.reverse(s, len(s))

# -7 42 70 39 3 63 8

a = list(map(int,input("Enter seven numbers separated by a space: ").split()))
first = int(input("Enter the index at which the search will begin: "))
size = int(input("Enter the size of the list that will be searched: "))
target = int(input("Enter the target value to search for: "))
print("Target found at index...", recursion.search(a, first, size, target, 0, False))