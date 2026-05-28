# Assignment 3: List comprehensions and generators

## Motif Discovery via Custom Python Module with CLI Support

Counting *k-mers* (substrings of length `k` in DNA sequence data) is an essential component of many methods in bioinformatics, including for genome and transcriptome assembly, for metagenomic sequencing, and for error correction of sequence reads. 

Motif discovery, such as identifying overrepresented *k-mers*, is a core technique in genomic analysis. Your goal is to build a robust command-line tool that researchers can use to process DNA sequences, identify top motifs, and optionally filter them by GC content.

Your code should eventually consist of the following files. The requirements are described sequentially below.

1. `motiftools.py` – your *reusable module*
2. `motifcli.py` – a *command-line interface script*
3. Example data – a FASTA file or sequence list in `.txt` or `.csv`
4. `README.md` – documentation, usage examples, and development notes


__1. `motiftools.py`:__ Module Functions

Make a class `MotifTools` which contains the functionality that is described below.

- When you initialize an instance of `MotifTools` you need to give it a DNA-sequence and a value for $k$.

- When you *iterate* over this instance, you receive the all the overlapping k-mers from the sequence. Make use of [the *iterator-pattern*](https://refactoring.guru/design-patterns/iterator) and delegate the iteration to a seperate class.

```python
tools = MotifTools("ATGCG", 3)
for item in tools:
    print(item)

# result:
ATG
TGC
GCG
```

- Provide your `MotifTools` with a method `count`, which returns a `dict[str, int]`, that represents all the *k-mers* across the input sequence. Make use of [python's `defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict).

```python
print(tools.count())

# result:
defaultdict(<class 'int'>, {'ATG': 1, 'TGC': 1, 'GCG': 1})
```

- Make a method `find_top_kmers(top_n = 10)`, that returns the most frequent *k-mers* sorted by frequency. Return only the `top_n` number of *k_mers*. Make a seperate class for this and use the results of the `count`-method that you made in the previous step.

- Make a method `gc_content()` that computes [the GC percentage](https://en.wikipedia.org/wiki/GC-content) of the sequence. Make use generator expressions.

- Finally, make a method `filter_kmers_by_gc(min_gc)` that returns a list with only those *k-mers* that have a GC content above the given threshold `min_gc`. Make use of a list-comprehension.


__2. `motifcli.py`:__ Command-Line Interface

Make a script `motifcli.py` that enables researchers to use your program using a nice command line interface. It should have the following command line options:

- `--input` (str): Path to a `.txt` file with one sequence per line (or FASTA)
- `--k` (int): Length of the motif (k-mer)
- `--top` (int): Number of top motifs to display
- `--min-gc` (float, optional): Minimum GC content to filter motifs

```bash
python motifcli.py --input sequences.txt --k 5 --top 8 --min-gc 50
```

Should return something like:

```bash
Top 8 motifs (k=5):
ATGCG - 15
GCGAT - 13
...
Filtered by GC content > 50%:
ATGCG
GCGAT
...
```

Implement this module using [`argparse`](https://docs.python.org/3/library/argparse.html).