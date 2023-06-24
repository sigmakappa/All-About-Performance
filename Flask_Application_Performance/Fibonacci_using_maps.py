import time

import sys
print("Recursion Limit:", sys.getrecursionlimit())

start = time.perf_counter()

alreadyknown = {0: 0, 1: 1}


def fib(n):
    if n not in alreadyknown:
        new_value = fib(n - 1) + fib(n - 2)
        alreadyknown[n] = new_value

    return alreadyknown[n]


print("Fib 10 :", fib(10))
print(alreadyknown)

end = time.perf_counter()
print("Time Taken : ", str(end - start))

# http://openbookproject.net/thinkcs/python/english3e/dictionaries.html#memoization
#
# If you played around with the fibo function from the chapter on recursion, you might
# have noticed that the bigger the argument you provide, the longer the function takes to run.
# Furthermore, the run time increases very quickly. On one of our machines, fib(20) finishes
# instantly, fib(30) takes about a second, and fib(40) takes roughly forever.
#
# A good solution is to keep track of values that have already been computed by storing them in
# a dictionary. A previously computed value that is stored for later use is called a memo.
# The above is an implementation of fib using memos.


# Memoization - Wikipedia
#
# In computing, memoization or memoisation is an optimization technique used primarily to
# speed up computer programs by storing the results of expensive function calls and returning
# the cached result when the same inputs occur again.


# Using this version of fib, our machines can compute fib(100) in an eyeblink.
#
# >>> fib(100)
# 354224848179261915075
