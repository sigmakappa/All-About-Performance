import os
import sys
import time

import numpy as np
import psutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(SCRIPT_DIR).split("All-About-Performance")[0] + "All-About-Performance")

import SystemInfo as sysinfo

# Getting System Info to console
sysinfo.getSystemInfo()


def matrixMultiplication(A, B, C, D):
    # Create two random matrices A and B of size AxB and CxD
    A = np.random.rand(A, B)
    B = np.random.rand(C, D)

    t0 = time.perf_counter()

    # Multiply the two matrices
    C = np.dot(A, B)

    t1 = time.perf_counter()

    return round(t1 - t0, 2)


def getCPUPercentage(parent_thread):
    while parent_thread:
        parent_thread.join()
        print('The CPU usage is: ', psutil.cpu_percent(1))
        time.sleep(1)


mat_A_dim = [100, 100]
mat_B_dim = [100, 100]

if mat_A_dim[1] == mat_B_dim[0]:
    time = matrixMultiplication(mat_A_dim[0], mat_A_dim[1], mat_B_dim[0], mat_B_dim[1])
else:
    print("Condition Unsatisfied: The number of columns in Matrix-1 must be equal to the number of rows in Matrix-2.")
    sys.exit(1)

# Printing test description
print("Matrix Multiplication")
print("Matrix A :", mat_A_dim[0], "x", mat_A_dim[1])
print("Matrix B :", mat_B_dim[0], "x", mat_B_dim[1])
print("Time taken:", time, "second")

# print("\n\n")
print(np.show_config())
# print("\n\n")