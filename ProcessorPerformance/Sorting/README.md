# Performance with Sorting Algorithms

Welcome to processor performance testing with sorting algorithms! This section is all about putting sorting
algorithms to the test and measuring their speed and efficiency. Whether you're a curious developer or an algorithm
enthusiast, you've come to the right place.

## Table of Contents

- [Getting Started](#getting-started)
- [Comparison of algorithms](#comparison-of-algorithms)
- [Running the Tests](#running-the-test)
- [What's Happening in the Processor?](#whats-happening-in-the-processor)
- [Performance Numbers](#performance-numbers)
- [Legend of Platforms tested upon](#legend)
- [Contributing](#contributing)
- [License](#license)
- [External Links](#external-links)

## Getting Started

Before we dive into the testing extravaganza, make sure you have the following prerequisites:

- A computer that rocks Linux, macOS, or Windows
- Python 3.7 or later, because we like it fresh
- pip, the ultimate package installer for Python

To get the required Python packages, run this righteous command:

```
pip install -r requirements.txt
```

## Comparison of Sorting Algorithms

We've got a bunch of sorting algorithms [^3] in our arsenal, and they're all ready to groove. Each algorithm struts its
stuff in its own module, making it easy to test and compare their performance.

Check out these below performant algorithms [^4] in this section (well others **_stuck-off_** were not too performant in
comparison hence were not considered for this test :beers:):

|        **Name**        | **Best Case** |   **Average Case**    |         **Worst Case**          | **Memory** |     **Method**      | 
|:----------------------:|:-------------:|:---------------------:|:-------------------------------:|:----------:|:-------------------:|
|      **Timsort**       |    **_n_**    |      **_nlogn_**      |           **_nlogn_**           |  _**n**_   | Insertion & Merging |
|     **Merge Sort**     |  **_nlogn_**  |      **_nlogn_**      |           **_nlogn_**           |  **_n_**   |       Merging       |
|     **Shell Sort**     |  **_nlogn_**  | **_n<sup>4/3</sup>_** |      **_n<sup>3/2</sup>_**      |  **_1_**   |      Insertion      |
|     **Heap Sort**      |  **_nlogn_**  |      **_nlogn_**      |           **_nlogn_**           |  **_1_**   |      Selection      |
|  ~~**Bubble Sort**~~   |    **_n_**    |  **_n<sup>2</sup>_**  |       **_n<sup>2</sup>_**       |  **_1_**   |     Exchanging      |
| ~~**Insertion Sort**~~ |    **_n_**    |  **_n<sup>2</sup>_**  |       **_n<sup>2</sup>_**       |  **_1_**   |      Insertion      |
|   ~~**Quick Sort**~~   |  **_nlogn_**  |      **_nlogn_**      |       **_n<sup>2</sup>_**       | **_logn_** |    Partitioning     |
|   ~~**Tree Sort**~~    |  **_nlogn_**  |      **_nlogn_**      | **_nlogn_**<br> (balanced tree) |   **n**    |      Insertion      |

Source: [^1]

#### Radix Sort

* **Time Complexity:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Radix sort is a non-comparative integer sorting algorithm that sorts
data with integer keys by grouping the keys by the individual digits which share the same significant position and
value. It has a time complexity of **_O(d * (n + b))_**, where:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* **_d_** is the number of digits,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* **_n_** is the number of elements, and<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* **_b_** is the base of the number system being used.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In practical implementations, radix sort is often faster than other
comparison-based sorting algorithms, such as quicksort or merge sort, for large datasets, especially when the keys have
many digits. However, its time complexity grows linearly with the number of digits, and so it is not as efficient for
small datasets.

* **Space Complexity:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Radix sort also has a space complexity of **_O(n + b)_**, where:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* **_n_** is the number of elements and<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* **_b_** is the base of the number system.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This space complexity comes from the need to create buckets for each
digit value and to copy the elements back to the
original array after each digit has been sorted.

Source: [^2]

<mark>**Seed data for this test has descending ordered list of 10M numbers which is required to be sorted in
ascending order (which is the worst case scenario for these sorting algorithms).**</mark>

## Running the Test

When you're ready to roll, head over to the main folder i.e. `Sorting` and run this sweet command:

```
python calling_sorts.py > sorting_observations.data
```

You'll see the algorithm in action, doing its thing and showing off its moves right there in the console. We'll give you
the lowdown on execution time and other groovy metrics.

## What's Happening in the Processor?

Now, let's take a moment to appreciate the funky stuff happening in your computer's processor when we run these sorting
algorithms. Brace yourself for a wild ride!

1. **Fetching**: The processor fetches the instructions of the algorithm from memory and gets ready to rock.
2. **Decoding**: The processor decodes those instructions into micro-operations, understanding what needs to be done.
3. **Executing**: This is where the magic happens! The processor performs the actual sorting operations, comparing
   elements, swapping them around, and getting everything in order.
4. **Memory Access**: The processor fetches and stores data from memory, accessing the elements to be sorted.
5. **Write Back**: After all the hard work, the processor writes back the sorted data to memory, making sure it's stored
   properly.

It's a funky dance of fetching, decoding, executing, memory access, and write back that keeps your algorithms grooving
to the beat!

## Performance Numbers

|    **Name**    | **P#1** | **P#2** | **P#3** | **P#4** | **P#5** | 
|:--------------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  **Timsort**   |  0.14   |  0.06   |         |         |         |
| **Merge Sort** | 168.61  |  31.29  |         |         |         |
| **Shell Sort** | 166.52  |  45.96  |         |         |         |
| **Heap Sort**  | 281.02  |  43.94  |         |         |         |
| **Radix Sort** | 113.23  |  27.63  |         |         |         |

### **Legend**

| **Platform** | **Details**                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| P#1          | Intel i3 2375M @ 1.5GHz 2nd Generation 8G RAM Pop!_OS 22.04 LTS (Kernel: Linux 6.2.6-76060206-generic) (Python 3.10.6) |
| P#2          | Intel i7 11800H @ 2.30GHz 16G RAM, Windows 11 Enterprise (version 22H2, OS Build 22621.1848) (Python 3.11.4)           |
| P#3          | Intel i7 1165G7 11th Generation 32G RAM Windows 10 Enterprise (Python 3.11.3)                                          |

## Contributing

Feeling the rhythm and want to contribute to this repository? We love it when people join the party! Here's how you can
make your move:

1. Fork this repository to your own GitHub account.
2. Create a cool new branch for your changes.
3. Make your changes and commit them to your branch.
4. Push your changes to your forked repository.
5. Show us your moves by creating a pull request to merge your changes into the main repository.

Let's keep this party going and make this repository even funkier!

## License

This repository is licensed under the MIT license, so you can shake, shuffle, and spin it however you like. Check out
the [`LICENSE`](../../LICENSE) file for all the funky details.

## External Links

[^1]: [Comparison of Sorting Algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms)
[^2]: [Time and Space Complexity of Radix Sort](https://www.geeksforgeeks.org/radix-sort/)
[^3]: [See Sorting Algorithms Graphically](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)
[^4]: [Time Complexity](https://en.wikipedia.org/wiki/Time_complexity)



