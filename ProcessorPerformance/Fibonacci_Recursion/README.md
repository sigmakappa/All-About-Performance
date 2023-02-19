D. E. Knuth writes: "Before Fibonacci wrote his work, the sequence F_{n} had already been
discussed by Indian scholars, who had long been interested in rhythmic patterns that are
formed from one-beat and two-beat notes. The number of such rhythms having n beats altogether
is F_{n+1}; therefore both Gopāla (before 1135) and Hemachandra (c. 1150) mentioned the
numbers 1, 2, 3, 5, 8, 13, 21, ... explicitly." (source The Art of Computer Programming:
Fundamental algorithms Vol. 1, 2nd ed. by Donald Knuth).

If you played around with calculating Fibonacci Numbers by recursion, you might
have noticed that the bigger the argument (or number) you provide, the longer the function
takes to run. Furthermore, the run time increases very quickly. On one of our machines,
fib(20) finishes instantly, fib(30) takes about a second, and fib(40) takes like a minute.

The following figure shows the so-called **recursion tree** corresponding to an execution of `fib(6)`:

![fib(6)](https://github.com/sigmakappa/All-About-Performance/blob/main/ProcessorPerformance/Fibonacci_Recursion/files/tree.png)

We tested this on different platforms; and also the results get better with time (as better
processors get available) as shown in table below.

I'll keep adding more results as tested on different platforms. Please feel free to send
results from your machine too (and please don't forget to add your machine configurations).
Thanks in advance.

More reading on Fibonacci or Hemachandra Numbers:

* Wikipaedia [here](https://en.wikipedia.org/wiki/Fibonacci_number#Computer_science).
* Fibonacci Numbers on the Online encyclopedia of Integer Sequences can be read [here](https://oeis.org/A000045)
* N. J. A. Sloane, The first 2000 Fibonacci numbers: Table of n, F(n) for n = 0 to
  2000 [here](https://oeis.org/A000045/b000045.txt)

Fibonacci computational observations on different platforms:


| No. | Computed    | P #1 (seconds)    | P #2 (seconds) | P #3 (seconds)    | P #4 (seconds) |
| --- | ----------- | ----------------- | -------------- | ----------------- | -------------- |
| 1   | 1           | 0.0               | 0.0            | 0.0               | 0.0            |
| 2   | 1           | 0.0               | 0.0            | 0.0               | 0.0            |
| 4   | 3           | 0.0               | 0.0            | 0.0               | 0.0            |
| 5   | 5           | 0.0               | 0.0            | 0.0               | 0.0            |
| 6   | 8           | 0.0               | 0.0            | 0.0               | 0.0            |
| 7   | 13          | 0.0               | 0.0            | 0.0               | 0.0            |
| 8   | 21          | 0.0               | 0.0            | 0.0               | 0.0            |
| 9   | 34          | 0.0               | 0.0            | 0.0               | 0.0            |
| 10  | 55          | 0.0               | 0.0            | 0.0               | 0.0            |
| 11  | 89          | 0.0               | 0.0            | 0.0               | 0.0            |
| 12  | 144         | 0.0               | 0.0            | 0.0               | 0.0            |
| 13  | 233         | 0.0               | 0.0            | 0.0               | 0.0            |
| 14  | 377         | 0.0               | 0.0            | 0.0               | 0.0            |
| 15  | 610         | 0.0               | 0.0            | 0.0               | 0.0            |
| 16  | 987         | 0.0               | 0.0            | 0.0               | 0.0            |
| 17  | 1597        | 0.0               | 0.0            | 0.0               | 0.0            |
| 18  | 2584        | 0.0               | 0.0            | 0.0               | 0.0            |
| 19  | 4181        | 0.0               | 0.0            | 0.0               | 0.0            |
| 20  | 6765        | 0.0               | 0.0            | 0.0               | 0.0            |
| 21  | 10946       | 0.0               | 0.0            | 0.0               | 0.0            |
| 22  | 17711       | 0.0               | 0.0            | 0.01              |                |
| 23  | 28657       | 0.0               | 0.01           | 0.01              |                |
| 24  | 46368       | 0.0               | 0.01           | 0.02              |                |
| 25  | 75025       | 0.0               | 0.02           | 0.03              |                |
| 26  | 121393      | 0.0               | 0.03           | 0.04              |                |
| 27  | 196418      | 0.0               | 0.05           | 0.07              |                |
| 28  | 317811      | 0.0               | 0.07           | 0.11              |                |
| 29  | 514229      | 0.0               | 0.12           | 0.17              |                |
| 30  | 832040      | 0.0               | 0.19           | 0.28              |                |
| 31  | 1346269     | 0.0               | 0.31           | 0.45              |                |
| 32  | 2178309     | 0.0               | 0.5            | 0.72              |                |
| 33  | 3524578     | 0.0               | 0.81           | 1.17              |                |
| 34  | 5702887     | 0.0               | 1.32           | 1.90              |                |
| 35  | 9227465     | 4.34              | 2.15           | 3.06              |                |
| 36  | 14930352    | 7.84              | 3.46           | 4.95              |                |
| 37  | 24157817    | 11.95             | 5.64           | 8.10              |                |
| 38  | 39088169    | 19.66             | 9.22           | 13.09             |                |
| 39  | 63245986    | 34.48             | 14.97          | 21.11             |                |
| 40  | 102334155   | 54.57             | 30.78          | 34.33             |                |
| 41  | 165580141   | 88.93             | 49.46          | 55.18             |                |
| 42  | 267914296   | 120.78            | 75.97          | 89.48             |                |
| 43  | 433494437   | 194.90            | 128.2          | 144.19            |                |
| 44  | 701408733   | 330.55            | 197.38         | 232.85            |                |
| 45  | 1134903170  | 690.03            | 338.49         | 380.30            |                |
| 46  | 1836311903  | 898.34            | 532.99         | 608.91            |                |
| 47  | 2971215073  | 1434.88           | 848.25         | 985.41            |                |
| 48  | 4807526976  | 2206.11           | 1353.57        | 1620.00           |                |
| 49  | 7778742049  | 3736.79           | 2251.44        | 2741.78           |                |
| 50  | 12586269025 | 4246.39           |                | 4299.81           |                |
| 51  | 20365011074 | 8221.40           |                | 6760.56 (1.88 h)  |                |
| 52  | 32951280099 | 14030.74 (3.9 h)  |                | 11736.61 (3.26 h) |                |
| 53  | 53316291173 | 23300.53 (6.47 h) |                | 18562.78 (5.16 h) |                |
| 54  | 86267571272 |                   |                | 29768.01 (8.26 h) |                |

# **Legend**


| Platform | Details                                                        |
| -------- | -------------------------------------------------------------- |
| P #1     | Intel i7 7880 7th Generation 16G RAM Windows 10 Enterprise     |
| P #2     | Intel i7 1165G7 11th Generation 32G RAM Windows 10 Enterprise  |
| P #3     | Intel i5 8250U, 8th Generation 8G RAM Windows 10 Pro           |
| P #4     | Intel i3 11th Generation 8G RAM Windows 11 Home (Coming soon!) |

NOTE: All observations based on Python 3.8/3.9.