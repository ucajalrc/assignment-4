## Overview

This repository contains all Python code, demonstration scripts, and the full written report for analyzing and comparing two fundamental algorithms: **Randomized Quicksort** and **Hash Table with Chaining**.  
You will find original, well-commented code, benchmarking tools, and a detailed report documenting both theory and results.

## File Structure & Guide

### 1. Sorting Algorithms

- **`randomized_quicksort.py`**  
  Implements Randomized Quicksort (recursive, picks a random pivot each time).  
  Extensively commented to help you learn how it works.

- **`deterministic_quicksort.py`**  
  Implements Deterministic Quicksort (always uses the first element as pivot).  
  Demonstrates worst-case behavior on sorted/reverse data.

### 2. Benchmarking

- **`benchmark.py`**  
  Runs and times both quicksort algorithms on:
  - Random arrays
  - Already sorted arrays
  - Reverse-sorted arrays
  - Arrays with repeated values  
  Handles `RecursionError` if deterministic quicksort fails on large, sorted inputs.  
  Prints results in a readable table for your analysis/report.

### 3. Hash Table

- **`hash_table.py`**  
  Implements a hash table with chaining (buckets are lists).  
  Supports `insert`, `search`, and `delete` operations.

- **`hash_table_demo.py`**  
  Demonstrates basic hash table usage, including insertion, update, lookup, and deletion.  
  Prints results so you can see everything works as expected.

### 4. Documentation

- **`report.docx` or `report.pdf`**  
  Contains the full written analysis, code explanations, discussion of theoretical vs. practical results, screenshots, and APA references.  
  **Be sure to open/read this file for the full story behind the code!**

## How to Run the Code

1. **Make sure you have Python 3 installed.**
2. **Benchmark the sorting algorithms:**  
   ```bash
        python3 benchmark.py
    ```

This will show you how fast each algorithm is on different input types and sizes.
If you see a "RecursionError" for deterministic quicksort, this is expected for large, sorted or reversed data.

3. **Test hash table operations:**

   ```bash
   python3 hash_table_demo.py
   ```
   This will print the results of insertion, updating, lookup, and deletion in the hash table.

## Notes & Tips

* For very large arrays, deterministic quicksort may hit a recursion limit and crash. This is expected, and demonstrates why randomized quicksort is more reliable in practice.
* If you want to run with larger arrays, you can increase the recursion limit in Python by adding:

  ```python
  import sys
  sys.setrecursionlimit(2000)
  ```

