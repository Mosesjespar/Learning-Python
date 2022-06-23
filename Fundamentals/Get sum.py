# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)

def get_sum(a,b):
    #good luck!
    sum = 0
    if a == b:
        return a
    elif a<b:
        for i in range(a,b+1):
            sum+=i
        return sum
    elif a>b:
        for i in range(b,a+1):
            sum+=i
        return sum