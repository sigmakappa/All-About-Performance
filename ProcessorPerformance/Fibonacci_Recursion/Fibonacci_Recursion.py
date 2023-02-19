import time


def printData(data):
    """
    prints and appends data to the corresponding "Your_Fibonacci_Recursion_Data.txt" file
    :param data: List of data points collected
    """
    # Open the file with access mode 'a'
    with open("Your_Fibonacci_Recursion_Data.txt", "a") as file_object:
        # Append at the end of file
        file_object.write(str(data[0]) + "\t\t\t" + str(data[1]) + "\t\t\t" + str(data[2]))
        file_object.write("\n")
        print("{0} = {1}, ({2} secs)".format(data[0], data[1], data[2]))


def printLog(data):
    """
        prints and appends data to the corresponding "Fibonacci_Recursion.log" file
        :param data: logs
    """
    with open("Fibonacci_Recursion.log", "a") as file_object:
        file_object.write(data)
        file_object.write("\n")
        print(data)


def fib(n):
    if n <= 1:
        return n
    t = fib(n - 1) + fib(n - 2)
    return t


for n in range(40, 55, 1):
    t0 = time.perf_counter()
    printLog(
        str("Running for : " + str(n) + "\tStart Time : " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())))

    result = fib(n)
    t1 = time.perf_counter()

    printData(["fib(" + str(n) + ")", result, str(round(t1 - t0, 2))])
