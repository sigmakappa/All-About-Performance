import gc
import os
import sys
import time

import psutil
from prettytable import PrettyTable

import Algorithms.bubble_sort as bubble
import Algorithms.insertion_sort as insert
import Algorithms.merge_sort as merge
import Algorithms.quick_sort as quick
import Algorithms.shell_sort as shell
import Algorithms.radix_sort as radix
import Algorithms.heap_sort as heap
import Algorithms.tree_sort as tree

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(SCRIPT_DIR).split("All-About-Performance")[0] + "All-About-Performance")

import SystemInfo as sysinfo

# Getting System Info to console
sysinfo.getSystemInfo()

numbers = []
process = psutil.Process()

# Creating data
data_volume = 10_000_000
for datum in range(data_volume, 1, -1):
    numbers.append(datum)

performance_numbers = {}

print("Seed Data Size:", f'{data_volume:,}')

print("Start Memory Status (Seed data loaded):", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")

print("Start Inbuilt sort (TimSort)")
numbers_inbuilt = numbers.copy()
t0 = time.perf_counter()
inbuilt_sorted = numbers_inbuilt.sort()
t1 = time.perf_counter()
print("Inbuilt (TimSort) Sorted!")
inbuilt_time = round(t1 - t0, 2)
del numbers_inbuilt
gc.collect()
print("Memory Status :", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
performance_numbers['timsort'] = inbuilt_time
print("Time for inbuilt sort (TimSort) :", inbuilt_time)

# print("Start Bubble sort")
# numbers_bubble = numbers.copy()
# t0 = time.perf_counter()
# bubble.bubblesort(numbers_bubble)
# t1 = time.perf_counter()
# print("Bubble Sorted!")
# bubble_time = round(t1 - t0, 2)
# performance_numbers['bubble'] = bubble_time
# print("Time for Bubble sort:", bubble_time)


# print("Start Quick sort")
# numbers_quick = numbers.copy()
# t0 = time.perf_counter()
# size = len(numbers_quick)
# quick.quickSort(numbers_quick, 0, size - 1)
# t1 = time.perf_counter()
# print("Quick Sorted!")
# quick_time = round(t1 - t0, 2)
# performance_numbers['quick'] = quick_time
# print("Time for Quick sort:", quick_time)


print("Start Merge sort")
numbers_merge = numbers.copy()
t0 = time.perf_counter()
size = len(numbers_merge)
merge.mergeSort(numbers_merge, 0, size - 1)
t1 = time.perf_counter()
print("Merge Sorted!")
merge_time = round(t1 - t0, 2)
del numbers_merge
gc.collect()
print("Memory Status :", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
performance_numbers['merge'] = merge_time
print("Time for Merge sort:", merge_time)

# print("Start Insertion sort")
# numbers_insert = numbers.copy()
# t0 = time.perf_counter()
# insert.insertionSort(numbers_insert)
# t1 = time.perf_counter()
# print("Insertion Sorted!")
# insertion_time = round(t1 - t0, 2)
# performance_numbers['insertion'] = insertion_time
# print("Time for Insertion sort:", insertion_time)


print("Start Shell sort")
numbers_shell = numbers.copy()
t0 = time.perf_counter()
size = len(numbers_shell)
shell.shellSort(numbers_shell, size)
t1 = time.perf_counter()
print("Shell Sorted!")
shell_time = round(t1 - t0, 2)
del numbers_shell
gc.collect()
print("Memory Status :", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
performance_numbers['shell'] = shell_time
print("Time for Shell sort:", shell_time)

print("Start Heap sort")
numbers_heap = numbers.copy()
t0 = time.perf_counter()
heap.heapSort(numbers_heap)
t1 = time.perf_counter()
print("Heap Sorted!")
heap_time = round(t1 - t0, 2)
del numbers_heap
gc.collect()
print("Memory Status :", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
performance_numbers['heap'] = heap_time
print("Time for Heap sort:", heap_time)

print("Start Radix sort")
numbers_radix = numbers.copy()
t0 = time.perf_counter()
radix.radixSort(numbers_radix)
t1 = time.perf_counter()
print("Radix Sorted!")
radix_time = round(t1 - t0, 2)
del numbers_radix
gc.collect()
print("Memory Status :", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
performance_numbers['radix'] = radix_time
print("Time for Radix sort:", radix_time)

# print("Start Tree sort")
# numbers_tree = numbers.copy()
# t0 = time.perf_counter()
# numbers_tree = tree.treeins(numbers_tree)
# # tree.inorderRec(numbers_tree)
# t1 = time.perf_counter()
# print("Tree Sorted!")
# tree_time = round(t1 - t0, 2)
# del numbers_tree
# gc.collect()
# print("Memory Status :", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
# performance_numbers['tree'] = tree_time
# print("Time for Heap sort:", tree_time)


# for key in performance_numbers:
#     print(key, " : ", performance_numbers[key])


performanceTable = PrettyTable(["Algorithm", "Run Times"])

for key in performance_numbers:
    performanceTable.add_row([key, performance_numbers[key]])

print(performanceTable)
