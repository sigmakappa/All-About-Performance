import sys
import time
from threading import Thread

import numpy as np
import psutil

print("Python version:", sys.version)
print("Numpy version:", np.version.version)


def matrixMultiplication():
    t0 = time.perf_counter()

    # Create two random matrices A and B of size 10000x10000
    A = np.random.rand(10000, 10000)
    B = np.random.rand(10000, 10000)

    # Multiply the two matrices
    C = np.dot(A, B)

    print("Done")
    t1 = time.perf_counter()

    print(round(t1 - t0, 2))


def getCPUPercentage(parent_thread):
    while parent_thread:
        parent_thread.join()
        print('The CPU usage is: ', psutil.cpu_percent(1))
        time.sleep(1)


thread1 = Thread(target=matrixMultiplication)
# thread2 = Thread(target=getCPUPercentage, args=(thread1,))


thread1.start()
# thread2.start()


# for thread in threads:
#     thread.join()
