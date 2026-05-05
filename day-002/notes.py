# 2.14
# Subscripting
print("Hello"[0])   # Output: H
print("Hello"[4])   # Output: o

# String
print("123" + "345")

# Integer = whole number
print(123 + 345)

# Large Integers
"""
You can write large integers with _ between for better reading
Python will ignore the _ and treat it as just a large integer
"""
print(123_456_789)  # Output: 123456789
print(123456789)    # Output: 123456789 -- same as line 17

# Float = Floating Point Number
print(3.14159)      # ! It's a dot, not a comma

# Boolean
print(True)
print(False)

# 2.15
print(type("abc"))  # Output: <class 'str'>
print(type(123))    # Output: <class 'int'>
print(type(3.14))   # Output: <class 'float'>
print(type(True))   # Output: <class 'bool'>

# This line gives TypeError
# print("Number of letters in your name: " + len(input("Enter your name: ")))

# Correct way:
length_of_name = len(input("Enter your name: "))
print("Number of letters in your name: " + str(length_of_name))

# 2.16
print("My age: " + str(28))
print(123+ 456)
print(7 - 2)
print(3 * 2)
print(5 / 3)    # Returns a float
print(5 // 3)   # Returns a int (truncated)
print(2 ** 3)   # Power of/Exponents

# Priority PEMDAS/LR -> (), **, * or /, + or -. In same level, from left to right
print(3 * 3 + 3 / 3 - 3)    # Output: 7
print(3 * (3 + 3) / 3 - 3)    # Output: 3

# 2.17
bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))
print(round(bmi, 2))    # Number to round, number of decimals. Ex: 30.85

# Number manipulation
score = 1

score += 1  # Same as score = score + 1
score -= 1  # Same as score = score - 1
score *= 1  # Same as score = score * 1
score /= 1  # Same as score = score / 1

# f-strings
print(f"Your score is {score}")


