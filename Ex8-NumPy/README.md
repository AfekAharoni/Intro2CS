<div align="center">

# Exercise 8 - NumPy and Matrix Manipulation

**NumPy and Matrix Manipulation** is the eighth exercise I solved as part of Huji's **Introduction to Computer Science** course.  
The main goal of this exercise is to get familiar with **Python 3**, the **Math library**, and the **NumPy library**, by working on matrix manipulations, simulations, and algorithm implementations.

[View All Exercises](https://github.com/AfekAharoni/Intro2CS)

</div>

---

## Exercise Description

This project includes:
1. `game_of_life.py` - Implements **Conway's Game of Life**, both in its classic form and an extended version using kernels to calculate cell density and survival.
2. `general_functions_native.py` - Contains matrix manipulation functions **without using NumPy**, including:
   - Matrix equality checks
   - Row and column summations
   - Matrix multiplication
   - Identity matrix creation
   - Inverse matrix verification
3. `general_functions_vec.py` - Contains optimized matrix manipulation functions **using NumPy**, covering the same functionality as the native implementation, including:
   - Matrix equality with error threshold
   - Row and column summations
   - Matrix multiplication
   - Inverse matrix verification
4. `test_for_functions.py` - A comprehensive test suite that verifies the correctness of the implementations in both `general_functions_native.py` and `general_functions_vec.py`.

---

## How to Run the Code

### 1. `game_of_life.py`  
Run simulations of Conway's Game of Life on a board of your choice.

```
python game_of_life.py
```

### 2. `general_functions_native.py`  
Use the provided functions for manual testing or import them into other projects.  
Functions include matrix sum, multiplication, identity matrix creation, etc.

### 3. `general_functions_vec.py`  
Use the NumPy-based implementations for optimized performance.  
Functions mirror those in the native implementation but leverage NumPy's power.

### 4. `test_for_functions.py`  
Run this script to execute all unit tests and verify the functionality of both native and NumPy implementations.

```
python test_for_functions.py
```

---

## Technologies Used
- **Math library** (`math` module)
- **NumPy library** (`numpy` module)
- `sys`, `copy` modules for system and data handling
- `typing` module for type annotations

---

## File Structure

```
Ex8-NumPy/
├── game_of_life.py
├── general_functions_native.py
├── general_functions_vec.py
└── test_for_functions.py
```

---
