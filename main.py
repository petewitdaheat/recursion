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