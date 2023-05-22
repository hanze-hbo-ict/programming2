# Week 2.4: More on Dask

## Introduction

Last week, we had our introduction on Dask. We saw how we can employ Dask to parallize our computation on large datasets. This week, we are going to look at some optimalization steps you can use to further decrease the time it takes to have your data processed.

During the plenary part, we have discussed a few possible steps you can take to optimize your data and reduce the time to compute certain features. In the following exercises, we are going to use six transformations on our data and compute the time it takes for the same operation after each step. This way, we can get a nice feeling of the reduction of the computation time.

## step 0a: get the data

Download [the script `create_groupby_dask.py`](files/create_groupby_dask.py) and study its contents. You can use this script to generate large randomized datasets that contain a certain amount of groups (so that we can experiment with `groupby` in either Dask or Pandas). If you run this script in the following manner, a dataset of about fivehunderd megabytes will be create in the directory `test` (of course, you can change this directory to your liking):

```shell
python create_groupby_dask.py -n 10000000 -k 100 -nf 1 -dir test
```

The script will create a file with a name that mirrors the setting you used in your command; so `test/groupby-N_10000000_K_100_file_0.csv` means this is a dataset with 10_000_000 records (`N_10000000`) and hunderd groups (`K_100`).

Now load the data in a pandas dataframe to get an idea of its contents.

```ipython
In [1]: import pandas as pd

In [2]: df = pd.read_csv('test/groupby-N_1000000_K_100_file_0.csv')

In [3]: df.head()
Out[3]: 
     id1    id2           id3  id4  id5   id6  v1  v2         v3
0  id066  id009  id0000005920   59   62  1719   4  14  41.904603
1  id029  id027  id0000003135   87   44  1553   0  10  77.563258
2  id026  id089  id0000008985   39    0  5118   1   8  67.640243
3  id010  id002  id0000005883   49   19  1774   4  14  58.275440
4  id092  id052  id0000003463   59   83  9388   3  13  86.269280

In [4]: 
```

## step 0b: create a timing function

As we are creating a benchmark in this exercise, we are going to perform the same operation on the dataframe (either Dask or Pandas) multiple times, in which we are only interested in the time it took to perform that operation. So, it makes sense to create a function that receives a dataframe, performs the operation and returns the time it took to finish.

Create a function `perform_test()` that does exactly this. During this benchmark, we are going to group the dataframe on `id1` and sum up the values of `v1`. Note: since this function needs to be called with both a pandas dataframe and a dask dataframe, you need to take into account that the last one uses *lazy* evaluation; so if the dataframe is from dask, you need to call `compute()` in the end. Use `isinstance` to check which type of dataframe you are receiving.


## step 1: setting a dask baseline

Let’s run the same groupby query with Dask. We’re going to intentionally type all the columns except `v1` as object columns, which should give us a good worst case Dask performance benchmark. object columns are notoriously memory hungry and inefficient. Use `dask.read_csv` with the following dictionary for the `ntype`-parameter to load our test-dataset and change all the columns into `obect`s.

```python
dtypes = {
    "id1": "object",
    "id2": "object",
    "id3": "object",
    "id4": "object",
    "id5": "object",
    "id6": "object",
    "v1": "int64",
    "v2": "object",
    "v3": "object",
}
```

As you no doubt will see, this computation takes far longer than our standard pandas implementation. Now let's see if we can speed this up a little bit.

## step 2: avoid object columns

The datatype `object` is notoriously inefficient when it comes to computation and calculation. If we know the data-type of a column, it is always better to provide exactly this. 

We can type `id1`, `id2`, and `id3` as [`string[pyarrow]`](https://pandas.pydata.org/docs/dev/user_guide/pyarrow.html) type columns, which are way more efficient. The column `v3` seems to be a `float64` and the rest of the columns can be seen as `int64`. Change the parameter `dtype` to reflect these improvements and rerun the test. Do you see an increase in performance?

## step 3: using multiple files

Dask can read and write multiple files in parallel. Since parallel I/O is normally a lot faster than working with a single large file, it can make sense to split the data over multiple files. Use the [ddf.repartition()](https://docs.dask.org/en/stable/generated/dask.dataframe.DataFrame.repartition.html) method with a `partition_size` of `'100MB'` to create several different files. 

Look at the `test`-directory (or whereever you have stored the files) in order to see the files this method has created. Now, use `read_csv` with a wildcard to create a dask dataframe with all these newly created files (don't forget to include the correct datatype from the previous exercise). Next, run the `perform_test` again.

## step 4a: parquet instead of csv

CSV is actually a bad data format. It is, as we say, *row based*, so it is impossible to drop certain columns while reading in the data. Columnar file formats that are stored as binary usually perform better than row-based, text file formats like CSV. Compressing the files to create smaller file sizes also helps. Read more about dast dataframes and Parquet on [this documentation site](https://docs.dask.org/en/stable/dataframe-parquet.html).

Use [`dask.to_parquet`](https://docs.dask.org/en/stable/generated/dask.dataframe.to_parquet.html) in the same manner as you have created the several csv-files in the previous exercise. For now, use `compression=None` as a parameter. Also, use [`pyarrow`](https://arrow.apache.org/docs/python/index.html) as an engine (you might need to `pip install` this).

Next, use [`dask.read_parquet`](https://docs.dask.org/en/stable/generated/dask.dataframe.read_parquet.html) to read in the parquet-files (remember to use the same engine you used when creating the files) and perform the test again.

## step 4b: use `snappy` as a compressor

Recreate the parquet-files using [`snappy`](http://google.github.io/snappy/) (which you also probably need to `pip install`: be sure to install `python-snappy`) as an engine and reperform the test. Is there an increase in the efficiency?

## step 5: column pruning

In contrast to csv, parquet is a columnar file format, which means you can selectively grab certain columns from the file. This is commonly referred to as *column pruning*. Column pruning isn’t possible for row based file formats like CSV. Have a look at [the documentation for `dask.read_csv`](https://docs.dask.org/en/stable/generated/dask.dataframe.read_parquet.html) to see how you can select only the columns that are relevant for our query: `id1` and `v1`. Create a new dataframe from our parquet-files with only these columns and, again, perform the test.

## step 6: comparison with pandas

Now, after all this work, we need to see whether dask is actually performing better than pandas. Create a dataframe on basis of the csv-file and run our `perform_test`-function. Note the time it takes to execute; is this better than, just as good as, or worse than dask...?

You will probably see that pandas performs way better than dask, even with the last improvements on the data. So why go through all the hassle? You will see that when you redo the exercise with ten times as much data as the dataset that we had.

Create a file with 100_000_000 records (`python create_groupby_dask.py -n 100000000 -k 100 -nf 1 -dir test`), make the necessary improvements you have gone through and benchmark pandas and dask again. If all goes well, this time you *will* see a significant improvement.


















