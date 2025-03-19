<div align="center">

# Lab 4 - Nim Game

**Nim Game** is an exercise I solved as part of Huji's **Introduction to Computer Science** course.  
The main goal of this lab is to get familiar with **Python 3**, the **Math library**, and to practice loops, input validation, and game logic implementation.

[View All Exercises](https://github.com/AfekAharoni/Intro2CS)

</div>

---

## Exercise Description

This project includes:
1. `lab4.py` - Implements a terminal-based Nim Game for two players.  
   The game features:
   - A board with rows of "nims" represented by the `|` symbol.
   - Input validation for row selection and number of nims to remove.
   - Turn-based logic for two players.
   - Win condition detection.
   - Colored terminal messages indicating player turns and game results (red for Player 1, blue for Player 2, green for the winner).

### How It Works:
- Each player takes turns removing one or more nims from a single row.
- The player forced to take the last nim **loses**.
- The game runs in the terminal and prints color-coded messages for better user experience.

---

## How to Run the Code

Run the program in your terminal with:

```
python lab4.py
```

Follow the on-screen prompts:
- Enter the row number you want to play on.
- Enter the number of nims you want to remove from that row.

---

## Technologies Used
- **Math library** (`math` module)
- `sys` and `os` for terminal input/output (implicitly via `input()` and printing)
- ANSI escape codes for terminal color formatting

---

## File Structure

```
Lab4/
└── lab4.py
```

---
