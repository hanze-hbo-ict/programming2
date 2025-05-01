# Assignment 4: Parallellisation

## Introduction

In the plenairy part we have discussed how you can make use of Python's [`multiprocessor` module](https://docs.python.org/3/library/multiprocessing.html) to distribute the computation of your problem over multiple cores on your CPU. We have seen how this increased performances when you are working with a lot of data, or when you need to do complex calculations.

![The comparison of calculations in serial and multiprocessor mode](imgs/comparison-serial-mp.png)

Even though the `multiprocessor` module is quite complex, the basic workings of it is quite simple. You provide your code with the number of cores you wish to use, some data you want to work with and a function that needs to be called for all the elements of your data. You use [the function `map`](https://docs.python.org/3/library/functions.html#map) for this minimal working example. For easy reference, the relevant portion of the code of the plenairy part is repeated below:

```python
import multiprocessing as mp
with mp.Pool() as p:
    res = p.map(sum_squared, numbers)
```

In this exercise, we are going to determine the fluctuation of CG-pairs over the genome of an organism. To do this, we need to count the amount of CG in (overlapping or non-overlapping) 'windows' (e.g. 10_000bp). We do this both in a sequential and in a non-sequential way, keeping track of the time it takes in both cases.

## Assignment

Download [the genome of the *E.coli*](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz). Write a Python-program that accepts a command-line argument `-w, --window_size` that represents the window-size 🤯 with which the program flows over the genome, returning the percentage of CG in that window:

```shell
> python count.py -w 10_000 | head
00000-10000: 0.521
10000-20000: 0.499
20000-30000: 0.526
30000-40000: 0.532
40000-50000: 0.528
50000-60000: 0.516
60000-70000: 0.556
70000-80000: 0.536
80000-90000: 0.500
>
```

Write the results to a csv-file. 


