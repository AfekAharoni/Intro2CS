<div align="center">

# Exercise 9 - Object Oriented Programming: Rush Hour Game

**Object Oriented Programming: Rush Hour Game** is the ninth exercise I solved as part of Huji's **Introduction to Computer Science** course.  
The main goal of this exercise is to get familiar with **Python 3**, the **Math library**, and to practice Object Oriented Programming concepts by implementing the classic Rush Hour puzzle game.

[View All Exercises](https://github.com/AfekAharoni/Intro2CS)

</div>

---

## Exercise Description

This project includes:
1. `rush-hour.py` - The main driver script. It loads the car configuration from a JSON file, creates the game board, and starts the game loop.
2. `game.py` - Implements the `Game` class, which controls the game flow, player input, and win/lose conditions.
3. `board.py` - Implements the `Board` class, which represents the state of the game board and handles car placement and movement validation.
4. `car.py` - Implements the `Car` class, representing individual cars with their positions, lengths, and allowed movements.
5. `helper.py` - Provides a utility function to load JSON configurations into the game.
6. `car_config.json` - A sample configuration file defining the initial setup of the cars on the board.

### How It Works:
- The player loads a car configuration JSON file when running the game.
- Cars are added to a 7x7 board with one exit point.
- The player interacts with the game through the terminal, entering commands to move cars until the target car reaches the exit.

---

## How to Run the Code

Run the main program by providing the path to a JSON configuration file as a command-line argument.

Example usage:
```
python rush-hour.py car_config.json
```

Follow the on-screen instructions to move cars:
- Input format: `R,u`  
  - `R` is the car name  
  - `u` is the move direction (up/down/left/right with `u/d/l/r`)  
- Press `!` to exit the game at any time.

---

## Technologies Used
- **Math library** (`math` module)
- **Tkinter** and **Turtle graphics** (optional GUI for extensions)
- `json` module for loading configurations
- `sys` and `typing` for system operations and type annotations

---

## File Structure

```
Ex9-ObjectOrientedProgram/
├── rush-hour.py
├── game.py
├── board.py
├── car.py
├── helper.py
└── car_config.json
```

---
