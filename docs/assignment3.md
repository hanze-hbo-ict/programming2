# Assignment 3: List comprehensions and generators


## Motif Discovery via Custom Python Module with CLI Support

Motif discovery, such as identifying overrepresented **k-mers**, is a core technique in genomic analysis. Your goal is to build a robust command-line tool that researchers can use to process DNA sequences, identify top motifs, and optionally filter them by GC content.

Your code should eventually consist of the following files. The requirements are described sequentially below.

1. `motiftools.py` – your **reusable module**
2. `motifcli.py` – a **command-line interface script**
3. Example data – a FASTA file or sequence list in `.txt` or `.csv`
4. `README.md` – documentation, usage examples, and development notes


__1. `motiftools.py`:__ Module Functions

This file contains your module functions: 

- `kmer_generator(seq: str, k: int) -> Generator[str, None, None]`:  yields all overlapping k-mers from the sequence.

Example: `kmer_generator("ATGCG", 3)` yields `"ATG"`, `"TGC"`, `"GCG"`


- `count_kmers(sequences: list[str], k: int) -> dict[str, int]`: counts all k-mers across the input sequences.


- `find_top_kmers(kmer_counts: dict[str, int], top_n: int = 10) -> list[tuple[str, int]]`: returns the most frequent k-mers sorted by frequency.


- `gc_content(seq: str) -> float`: computes GC percentage of a sequence (use generator expressions).

- `filter_kmers_by_gc(kmer_counts: dict[str, int], min_gc: float) -> list[str]`: returns only those k-mers with GC content above the threshold.

Use **generator expressions**, **list comprehensions**, and good function design.

__2. `motifcli.py`:__ Command-Line Interface

This script should enable researchers to use your program using a nice comman line interface. It should have the following command line options:

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