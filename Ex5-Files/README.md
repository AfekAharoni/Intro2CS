<div align="center">

# Exercise 5 - Word Search

**Word Search** is the fifth exercise I solved as part of Huji's **Introduction to Computer Science** course.  
The main goal of this exercise is to get familiar with **Python 3**, the **Math library**, and to practice file handling, string manipulation, and algorithm design.

[View All Exercises](https://github.com/AfekAharoni/Intro2CS)

</div>

---

## Exercise Description

This project includes:
1. `wordsearch.py` - Implements a word search puzzle solver. The program reads a list of words and a character matrix from files, then searches for the words in various directions and outputs the results to a file.
2. `wordsearch_test.py` - A testing module containing multiple unit tests that validate the functionality of the main program, including reading files, searching words, and output writing.

In this exercise:
- The user provides a word list file, a matrix file, and directions to search.
- The program processes these inputs and outputs how many times each word appears in the matrix, following the given directions.
- Supports multiple directions (up, down, left, right, diagonal, etc.) and avoids duplicate counting.

---

## How to Run the Code

### 1. `wordsearch.py`  
Run the program with the following arguments:  
`<word_list_file> <matrix_file> <output_file> <directions>`

Example usage:  
```
python wordsearch.py wordlist.txt matrix.txt output.txt udlr
```

### 2. `wordsearch_test.py`  
Run the test file to validate functionality:  
```
python wordsearch_test.py
```

---

## Technologies Used
- **Math library** (`math` module)
- `sys`, `os` modules for file handling and process management
- `copy` module for deep copies of data structures

---

## File Structure

```
Ex5-Files/
├── wordsearch.py
└── wordsearch_test.py
```

---
