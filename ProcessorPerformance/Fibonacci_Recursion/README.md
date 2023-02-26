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


| No. | Computed     | P #1 (sec)        | P #2 (sec)        | P #3 (sec)        | P #4 (sec)         | P #5 (sec) |
| --- | ------------ | ----------------- | ----------------- | ----------------- | ------------------ |------------|
| 1   | 1            | 0.0               | 0.0               | 0.0               | 0.0                | -          |
| 2   | 1            | 0.0               | 0.0               | 0.0               | 0.0                | -          |
| 4   | 3            | 0.0               | 0.0               | 0.0               | 0.0                | -          |
| 5   | 5            | 0.0               | 0.0               | 0.0               | 0.0                | -          |
| 6   | 8            | 0.0               | 0.0               | 0.0               | 0.0                | -          |
| 7   | 13           | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 8   | 21           | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 9   | 34           | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 10  | 55           | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 11  | 89           | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 12  | 144          | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 13  | 233          | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 14  | 377          | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 15  | 610          | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 16  | 987          | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 17  | 1597         | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 18  | 2584         | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 19  | 4181         | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 20  | 6765         | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 21  | 10946        | 0.0               | 0.0               | 0.0               | 0.0                |            |
| 22  | 17711        | 0.0               | 0.0               | 0.01              | 0.0                |            |
| 23  | 28657        | 0.0               | 0.01              | 0.01              | 0.01               |            |
| 24  | 46368        | 0.0               | 0.01              | 0.02              | 0.01               |            |
| 25  | 75025        | 0.0               | 0.02              | 0.03              | 0.02               |            |
| 26  | 121393       | 0.0               | 0.03              | 0.04              | 0.04               |            |
| 27  | 196418       | 0.0               | 0.05              | 0.07              | 0.05               |            |
| 28  | 317811       | 0.0               | 0.07              | 0.11              | 0.1                |            |
| 29  | 514229       | 0.0               | 0.12              | 0.17              | 0.15               |            |
| 30  | 832040       | 0.0               | 0.19              | 0.28              | 0.22               |            |
| 31  | 1346269      | 0.0               | 0.31              | 0.45              | 0.42               |            |
| 32  | 2178309      | 0.0               | 0.5               | 0.72              | 0.47               |            |
| 33  | 3524578      | 0.0               | 0.81              | 1.17              | 0.95               |            |
| 34  | 5702887      | 0.0               | 1.32              | 1.90              | 1.56               |            |
| 35  | 9227465      | 4.34              | 2.15              | 3.06              | 2.83               |            |
| 36  | 14930352     | 7.84              | 3.46              | 4.95              | 4.52               |            |
| 37  | 24157817     | 11.95             | 5.64              | 8.10              | 7.96               |            |
| 38  | 39088169     | 19.66             | 9.22              | 13.09             | 10.94              |            |
| 39  | 63245986     | 34.48             | 14.97             | 21.11             | 14.34              |            |
| 40  | 102334155    | 54.57             | 24.13             | 34.33             | 23.11              |            |
| 41  | 165580141    | 88.93             | 38.54             | 55.18             | 33.61              |            |
| 42  | 267914296    | 120.78            | 61.78             | 89.48             | 50.71              |            |
| 43  | 433494437    | 194.90            | 100.34            | 144.19            | 85.15              |            |
| 44  | 701408733    | 330.55            | 163.74            | 232.85            | 205.51             |            |
| 45  | 1134903170   | 690.03            | 332.6             | 380.30            | 330.06             |            |
| 46  | 1836311903   | 898.34            | 429.25            | 608.91            | 486.47             |            |
| 47  | 2971215073   | 1434.88           | 690.87            | 985.41            | 770.87             |            |
| 48  | 4807526976   | 2206.11           | 1176.5            | 1620.00           | 1212.81            |            |
| 49  | 7778742049   | 3736.79           | 1863.56           | 2741.78           | 1886.73            |            |
| 50  | 12586269025  | 4246.39           | 2935.28           | 4299.81           | 3077.2             |            |
| 51  | 20365011074  | 8221.40 (2.28 h)  | 4761.29 (1.32 h)  | 6760.56 (1.88 h)  | 4965.29 (1.38 h)   |            |
| 52  | 32951280099  | 14030.74 (3.9 h)  | 7685.59 (2.13 h)  | 11736.61 (3.26 h) | 8716.07 (2.42h)    |            |
| 53  | 53316291173  | 23300.53 (6.47 h) | 12442.76 (3.46 h) | 18562.78 (5.16 h) | 14259.41 (3.96h)   |            |
| 54  | 86267571272  | -                 | 20926.23 (5.81 h) | 29768.01 (8.26 h) | 23112.83 (6.42h)   |            |
| 55  | 139583862445 | -                 | 33833.51 (9.4 h)  | -                 | 37209.11 (10.34 h) |            |

## **Legend**


| Platform | Details                                                                                           |
| -------- |---------------------------------------------------------------------------------------------------|
| P #1     | Intel i7 7880 7th Generation 16G RAM Windows 10 Enterprise                                        |
| P #2     | Intel i7 1165G7 11th Generation 32G RAM Windows 10 Enterprise                                     |
| P #3     | Intel i5 8250U, 8th Generation 8G RAM Windows 10 Pro                                              |
| P #4     | Intel i3 1115G4 @ 3.00GHz 11th Generation 16G RAM Windows 11 Pro Version	22H2 OS build 22621.1265 |
| P #5     | Intel i3 3rd Generation 8G RAM Windows 7 Ultimate (Coming Soon...) (* Python 3.3)                 |

NOTE: All observations based on Python 3.8/3.9 (except stated otherwise).

## **Instructions for carrying out the above experiment:**

1. While the process is running, make sure nothing else is executed/running by the user that takes up the processor.
2. The observations can easily be obtained by running the experiment for one weekend on a machine (~48 hours).
