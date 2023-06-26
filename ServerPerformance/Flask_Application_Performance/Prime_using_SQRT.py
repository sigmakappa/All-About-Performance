from math import sqrt
import time

start = time.perf_counter()

# Number to be checked for prime
n = 22_637_299_228_301
# n = 325


def isPrime(n):
    flag = 0
    if (n > 1):
        for k in range(2, int(sqrt(n)) + 1):
            if (n % k == 0):
                flag = 1
                break
        if (flag == 0):
            return (str(n) + " is Prime!")
        else:
            return (str(n) + " is Non-Prime.")
    else:
        return (str(n) + " is Non-Prime.")


status = isPrime(n)
print(status)
end = time.perf_counter()
print("Time Taken : ", str(end - start))
