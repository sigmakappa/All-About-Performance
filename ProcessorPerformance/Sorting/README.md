# Performance with Sorting Algorithms

Welcome to processor performance testing with sorting algorithms! This section is all about putting sorting
algorithms to the test and measuring their speed and efficiency. Whether you're a curious developer or an algorithm
enthusiast, you've come to the right place.

## Table of Contents

- [Getting Started](#getting-started)
- [Sorting Algorithms](#sorting-algorithms)
- [Running the Tests](#running-performance-tests)
- [What's Happening in the Processor?](#whats-happening-in-the-processor)
- [Comparison of algorithms](#comparison-of-algorithms)
- [Performance Numbers](#performance-numbers)
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

## Sorting Algorithms

We've got a bunch of sorting algorithms in our arsenal, and they're all ready to groove. Each algorithm struts its
stuff in its own module, making it easy to test and compare their performance.

Check out these below algorithms:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort

Get ready to witness some algorithmic magic on the dance floor!

## Running Performance Tests

When you're ready to roll, head over to the module of the sorting algorithm you want to test. Run this sweet command:

```
python calling_sorts.py
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

## Comparison of Algorithms<sup>[1]</sup>

|    **Name**    | **Best Case** |   **Average Case**    |    **Worst Case**     | **Memory** |     **Method**      | 
|:--------------:|:-------------:|:---------------------:|:---------------------:|:----------:|:-------------------:|
|  **Timsort**   |    **_n_**    |      **_nlogn_**      |      **_nlogn_**      |  _**n**_   | Insertion & Merging |
| **Merge Sort** |  **_nlogn_**  |      **_nlogn_**      |      **_nlogn_**      |  **_n_**   |       Merging       |
| **Shell Sort** |  **_nlogn_**  | **_n<sup>4/3</sup>_** | **_n<sup>3/2</sup>_** |  **_1_**   |      Insertion      |
| **Heap Sort**  |  **_nlogn_**  |      **_nlogn_**      |      **_nlogn_**      |  **_1_**   |      Selection      |

#### Radix Sort

* Time Complexity:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Radix sort is a non-comparative integer sorting algorithm that sorts
data with integer keys by grouping the keys by the individual digits which share the same significant position and
value. It has a time complexity of **_O(d * (n + b))_**, where **_d_** is the number of digits, **_n_** is the number of
elements, and **_b_** is the base of the number system being used.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In practical implementations, radix sort is often faster than other
comparison-based sorting algorithms, such as quicksort or merge sort, for large datasets, especially when the keys have
many digits. However, its time complexity grows linearly with the number of digits, and so it is not as efficient for
small datasets.

* Space Complexity:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Radix sort also has a space complexity of **_O(n + b)_**, where **_n_**
is the number of elements and **_b_** is the
base of the number system. This space complexity comes from the need to create buckets for each digit value and to copy
the elements back to the original array after each digit has been sorted.

## Performance Numbers

|    **Name**    | **Best Case** |   **Average Case**    |    **Worst Case**     | **Memory** |     **Method**      | 
|:--------------:|:-------------:|:---------------------:|:---------------------:|:----------:|:-------------------:|
|  **Timsort**   |    **_n_**    |      **_nlogn_**      |      **_nlogn_**      |  _**n**_   | Insertion & Merging |
| **Merge Sort** |  **_nlogn_**  |      **_nlogn_**      |      **_nlogn_**      |  **_n_**   |       Merging       |
| **Shell Sort** |  **_nlogn_**  | **_n<sup>4/3</sup>_** | **_n<sup>3/2</sup>_** |  **_1_**   |      Insertion      |
| **Heap Sort**  |  **_nlogn_**  |      **_nlogn_**      |      **_nlogn_**      |  **_1_**   |      Selection      |



## Contributing

Feeling the rhythm and want to contribute to this repository? We love it when people join the party! Here's how you can
make your move:

1. Fork this repository to your own GitHub account.
2. Create a cool new branch for your changes.
3. Make your groovy changes and commit them to your branch.
4. Push your changes to your forked repository.
5. Show us your moves by creating a pull request to merge your changes into the main repository.

Let's keep this party going and make this repository even funkier!

## License

This repository is licensed under the MIT license, so you can shake, shuffle, and spin it however you like. Check out
the `LICENSE` file for all the funky details.

## External Links

[1](https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms)




