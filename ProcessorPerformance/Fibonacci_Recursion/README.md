# **Fibonacci Numbers (or Hemachandra Numbers)**

D. E. Knuth writes: "Before Fibonacci wrote his work, the sequence F_{n} had already been
discussed by Indian scholars, who had long been interested in rhythmic patterns that are
formed from one-beat and two-beat notes. The number of such rhythms having n beats altogether
is F_{n+1}; therefore both Gopāla (before 1135) and Hemachandra (c. 1150) mentioned the
numbers 1, 2, 3, 5, 8, 13, 21, ... explicitly." (source The Art of Computer Programming:
Fundamental algorithms Vol. 1, 2nd ed. by Donald Knuth).

# **Fibonacci: by Recursion**

If you played around with calculating Fibonacci Numbers by recursion, you might
have noticed that the bigger the argument (or number) you provide, the longer the function
takes to run. Furthermore, the run time increases very quickly. On one of our machines,
fib(20) finishes instantly, fib(30) takes about a second, and fib(40) takes like a minute.

The following figure shows the so-called **recursion tree** corresponding to an execution of `fib(6)`:

![fib(6)](https://github.com/sigmakappa/All-About-Performance/blob/main/ProcessorPerformance/Fibonacci_Recursion/files/tree.png)

We tested this on different platforms; and also the results get better with time (as better
processors get available) as shown in table below.

# **Fibonacci: by Memoization [doing above the faster way! ;) ]**

In computing, memoization or memoisation is an optimization technique used primarily to
speed up computer programs by storing the results of expensive function calls and returning
the cached result when the same inputs occur again.

This program
is [here](https://github.com/sigmakappa/All-About-Performance/blob/main/ProcessorPerformance/Fibonacci_Recursion/Fibonacci_using_maps.py)

I'll keep adding more results as tested on different platforms. Please feel free to send
results from your machine too (and please don't forget to add your machine configurations).
Thanks in advance.

More reading on Fibonacci or Hemachandra Numbers:

* Wikipaedia [here](https://en.wikipedia.org/wiki/Fibonacci_number#Computer_science).
* Fibonacci Numbers on the Online encyclopedia of Integer Sequences can be read [here](https://oeis.org/A000045).
* N. J. A. Sloane, The first 2000 Fibonacci numbers: Table of n, F(n) for n = 0 to
  2000 [here](https://oeis.org/A000045/b000045.txt).

Fibonacci computational observations (by recursion) on different platforms are as below:


| No. | Computed     | P #1 (sec)         | P #2 (sec)       | P #3 (sec)       | P #4 (sec)       | P #5 (sec)         |
| --- | ------------ | ------------------ | ---------------- | ---------------- | ---------------- | ------------------ |
| 1   | 1            | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 2   | 1            | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 4   | 3            | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 5   | 5            | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 6   | 8            | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 7   | 13           | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 8   | 21           | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 9   | 34           | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 10  | 55           | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 11  | 89           | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 12  | 144          | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 13  | 233          | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 14  | 377          | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 15  | 610          | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 16  | 987          | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 17  | 1597         | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 18  | 2584         | 0.0                | 0.0              | 0.0              | 0.0              | 0.0                |
| 19  | 4181         | 0.01               | 0.0              | 0.0              | 0.0              | 0.0                |
| 20  | 6765         | 0.01               | 0.0              | 0.0              | 0.0              | 0.0                |
| 21  | 10946        | 0.02               | 0.0              | 0.0              | 0.0              | 0.0                |
| 22  | 17711        | 0.03               | 0.0              | 0.0              | 0.01             | 0.0                |
| 23  | 28657        | 0.04               | 0.0              | 0.01             | 0.01             | 0.01               |
| 24  | 46368        | 0.07               | 0.0              | 0.01             | 0.02             | 0.01               |
| 25  | 75025        | 0.1                | 0.0              | 0.02             | 0.03             | 0.02               |
| 26  | 121393       | 0.17               | 0.0              | 0.03             | 0.04             | 0.04               |
| 27  | 196418       | 0.27               | 0.0              | 0.05             | 0.07             | 0.05               |
| 28  | 317811       | 0.45               | 0.0              | 0.07             | 0.11             | 0.1                |
| 29  | 514229       | 0.71               | 0.0              | 0.12             | 0.17             | 0.15               |
| 30  | 832040       | 1.15               | 0.0              | 0.19             | 0.28             | 0.22               |
| 31  | 1346269      | 1.86               | 0.0              | 0.31             | 0.45             | 0.42               |
| 32  | 2178309      | 3.03               | 0.0              | 0.5              | 0.72             | 0.47               |
| 33  | 3524578      | 4.91               | 0.0              | 0.81             | 1.17             | 0.95               |
| 34  | 5702887      | 7.84               | 0.0              | 1.32             | 1.90             | 1.56               |
| 35  | 9227465      | 12.73              | 4.34             | 2.15             | 3.06             | 2.83               |
| 36  | 14930352     | 20.43              | 7.84             | 3.46             | 4.95             | 4.52               |
| 37  | 24157817     | 33.57              | 11.95            | 5.64             | 8.10             | 7.96               |
| 38  | 39088169     | 55.04              | 19.66            | 9.22             | 13.09            | 10.94              |
| 39  | 63245986     | 89.8               | 34.48            | 14.97            | 21.11            | 14.34              |
| 40  | 102334155    | 139.7              | 54.57            | 24.13            | 34.33            | 23.11              |
| 41  | 165580141    | 226.41             | 88.93            | 38.54            | 55.18            | 33.61              |
| 42  | 267914296    | 366.93             | 120.78           | 61.78            | 89.48            | 50.71              |
| 43  | 433494437    | 592.94             | 194.90           | 100.34           | 144.19           | 85.15              |
| 44  | 701408733    | 959.79             | 330.55           | 163.74           | 232.85           | 205.51             |
| 45  | 1134903170   | 1552.07            | 690.03           | 332.6            | 380.30           | 330.06             |
| 46  | 1836311903   | 2515.27            | 898.34           | 429.25           | 608.91           | 486.47             |
| 47  | 2971215073   | 4064.08            | 1434.88          | 690.87           | 985.41           | 770.87             |
| 48  | 4807526976   | 6564.74 (1.82h)    | 2206.11          | 1176.5           | 1620.00          | 1212.81            |
| 49  | 7778742049   | 10664.5 (2.96h)    | 3736.79          | 1863.56          | 2741.78          | 1886.73            |
| 50  | 12586269025  | 17295.56 (4.80h)   | 4246.39          | 2935.28          | 4299.81          | 3077.2             |
| 51  | 20365011074  | 28119.70 (7.81h)   | 8221.40 (2.28h)  | 4761.29 (1.32h)  | 6760.56 (1.88h)  | 4965.29 (1.38h)    |
| 52  | 32951280099  | 45838.24 (12.72h)  | 14030.74 (3.9h)  | 7685.59 (2.13h)  | 11736.61 (3.26h) | 8716.07 (2.42h)    |
| 53  | 53316291173  | 74594.97 (20.72h)  | 23300.53 (6.47h) | 12442.76 (3.46h) | 18562.78 (5.16h) | 14259.41 (3.96h)   |
| 54  | 86267571272  | 121561.51 (33.77h) | -                | 20926.23 (5.81h) | 29768.01 (8.26h) | 23112.83 (6.42h)   |
| 55  | 139583862445 | -                  | -                | 33833.51 (9.4h)  | -                | 37209.11 (10.34 h) |

### **Legend**


| **Platform** | **Details**                                                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| P #1         | Intel i3 2375M @ 1.5GHz 2nd Generation 8G RAM Windows 7 Ultimate (* Win 7 support limited till Python 3.3) |
| P #2         | Intel i7 7880 7th Generation 16G RAM Windows 10 Enterprise                                                 |
| P #3         | Intel i7 1165G7 11th Generation 32G RAM Windows 10 Enterprise                                              |
| P #4         | Intel i5 8250U, 8th Generation 8G RAM Windows 10 Pro                                                       |
| P #5         | Intel i3 1115G4 @ 3.00GHz 11th Generation 16G RAM Windows 11 Pro Version 22H2 OS build 22621.1265          |

NOTE: All observations based on Python 3.8/3.9 (except stated otherwise).

## **Fibonacci computational observations (by recursion) on same hardware but different Operating Systems**

Yours truly has an old 2013 machine (still working, issues mainly in battery and hence the power backup). I used this to record how the Fibonacci
calculations do perform on different Operating Systems (supporting this [here](https://askubuntu.com/questions/1148999/does-ubuntu-run-faster-than-windows-10)?).

In general, Ubuntu tends to be faster and more lightweight than Windows because it is a Linux-based operating system that is designed to be 
efficient and optimized for performance. Ubuntu typically requires less system resources than Windows, which can result in faster boot times,
smoother application performance, and more responsive system performance overall.

I also know its wrong comparing apples with oranges (Win7+Python3.3 v/s Ubuntu22+Python3.10). But still: :apple: v/s :orange: !!!
Also, Ubuntu/PopOS gave this old machine a [new life](https://www.makeuseof.com/tag/6-lightweight-linux-distributions-give-pc-lease-life/).

Numbers helping the above as below:


| No. | Computed     | OS #1 (sec)        | OS #2 (sec)        | OS #3 (sec)       |
| --- | ------------ | ------------------ | ------------------ | ----------------- |
| 1   | 1            | 0.0                | 0.0                | 0.0               |
| 2   | 1            | 0.0                | 0.0                | 0.0               |
| 3   | 2            | 0.0                | 0.0                | 0.0               |
| 4   | 3            | 0.0                | 0.0                | 0.0               |
| 5   | 5            | 0.0                | 0.0                | 0.0               |
| 6   | 8            | 0.0                | 0.0                | 0.0               |
| 7   | 13           | 0.0                | 0.0                | 0.0               |
| 8   | 21           | 0.0                | 0.0                | 0.0               |
| 9   | 34           | 0.0                | 0.0                | 0.0               |
| 10  | 55           | 0.0                | 0.0                | 0.0               |
| 11  | 89           | 0.0                | 0.0                | 0.0               |
| 12  | 144          | 0.0                | 0.0                | 0.0               |
| 13  | 233          | 0.0                | 0.0                | 0.0               |
| 14  | 377          | 0.0                | 0.0                | 0.0               |
| 15  | 610          | 0.0                | 0.0                | 0.0               |
| 16  | 987          | 0.0                | 0.0                | 0.0               |
| 17  | 1597         | 0.0                | 0.0                | 0.0               |
| 18  | 2584         | 0.0                | 0.0                | 0.0               |
| 19  | 4181         | 0.01               | 0.0                | 0.0               |
| 20  | 6765         | 0.01               | 0.01               | 0.01              |
| 21  | 10946        | 0.02               | 0.01               | 0.01              |
| 22  | 17711        | 0.03               | 0.02               | 0.01              |
| 23  | 28657        | 0.04               | 0.03               | 0.02              |
| 24  | 46368        | 0.07               | 0.04               | 0.04              |
| 25  | 75025        | 0.1                | 0.07               | 0.06              |
| 26  | 121393       | 0.17               | 0.11               | 0.1               |
| 27  | 196418       | 0.27               | 0.17               | 0.16              |
| 28  | 317811       | 0.45               | 0.28               | 0.26              |
| 29  | 514229       | 0.71               | 0.44               | 0.43              |
| 30  | 832040       | 1.15               | 0.71               | 0.71              |
| 31  | 1346269      | 1.86               | 1.17               | 1.16              |
| 32  | 2178309      | 3.03               | 1.9                | 2.08              |
| 33  | 3524578      | 4.91               | 3.1                | 3.32              |
| 34  | 5702887      | 7.84               | 4.95               | 5.13              |
| 35  | 9227465      | 12.73              | 8.08               | 8.26              |
| 36  | 14930352     | 20.43              | 12.73              | 13.49             |
| 37  | 24157817     | 33.57              | 20.31              | 21.28             |
| 38  | 39088169     | 55.04              | 32.61              | 33.17             |
| 39  | 63245986     | 89.8               | 54.86              | 54.45             |
| 40  | 102334155    | 139.7              | 88.45              | 84.94             |
| 41  | 165580141    | 226.41             | 142.85             | 135.66            |
| 42  | 267914296    | 366.93             | 232.51             | 213.58            |
| 43  | 433494437    | 592.94             | 375.51             | 343.47            |
| 44  | 701408733    | 959.79             | 603.41             | 557.06            |
| 45  | 1134903170   | 1552.07            | 969.43             | 903.33            |
| 46  | 1836311903   | 2515.27            | 1560.26            | 1580.26           |
| 47  | 2971215073   | 4064.08            | 2518.64            | 2677.89           |
| 48  | 4807526976   | 6564.74 (1.82h)    | 4098.09 (1.13h)    | 3899.26 (1.08h)   |
| 49  | 7778742049   | 10664.5 (2.96h)    | 6628.09 (1.84h)    | 6257.27 (1.74h)   |
| 50  | 12586269025  | 17295.56 (4.80h)   | 10754.14 (2.98h)   | 10188.36 (2.83h)  |
| 51  | 20365011074  | 28119.70 (7.81h)   | 16127.31 (4.47h)   | 17873.36 (4.96h)  |
| 52  | 32951280099  | 45838.24 (12.72h)  | 26123.1 (7.25h)    | 27929.01 (7.76h)  |
| 53  | 53316291173  | 74594.97 (20.72h)  | 43318.48 (12.03h)  | 42786.71 (11.89h) |
| 54  | 86267571272  | 121561.51 (33.77h) | 71266.8 (19.79h)   | 70813.76 (19.67h) |
| 55  | 139583862445 | -                  | 115850.15 (32.18h) | -                 |

### **Legend (for above same hardware with different OSs experiment)**


| **Platform** | **Details**                                      |
| ------------ | ------------------------------------------------ |
| OS #1        | Windows 7 Ultimate (Python 3.3)                  |
| OS #2        | Ubuntu 22.04.2 LTS Jammy Jellyfish (Python 3.10) |
| OS #3        | Pop!_OS 22.04 LTS (Python 3.10)                  |
| -            | -                                                |
| **Hardware** | Intel i3 2375M @ 1.5GHz 2nd Generation 8G RAM    |

## **Instructions for carrying out the above experiment:**

1. While the process is running, make sure nothing else is executed/running by the user that takes up the processor.
2. The observations can easily be obtained by running the experiment for one weekend on a machine (~48 hours) (* excpetion being my Intel Gen2 Processor)
