# Python Learning Repository

This repository serves as a personal playground for learning Python through hands-on practice. By implementing simple functions and building small programs incrementally, the goal is to build proficiency and confidence in Python programming.

## Learning Journey Overview

Started with basic scripts and progressed to more structured code, incorporating functions, data structures, and file operations. Each script demonstrates a concept or builds upon previous knowledge.

## What You'll Learn

- **Basic Python Syntax**: Variables, print statements, and simple expressions.
- **Control Flow**: Loops (`for` loops) and conditional statements (`if`, `elif`, `else`).
- **Input and Output**: Reading user input with `input()` and displaying results with `print()`.
- **Data Structures**: Lists for storing collections of data, and dictionaries for key-value pairs.
- **Functions**: Defining reusable functions to organize code and avoid repetition.
- **File I/O**: Reading from and writing to text files for data persistence.
- **String Formatting**: Using f-strings for clean output formatting.
- **Logic and Algorithms**: Implementing basic logic gates and data filtering algorithms.

## Repository Contents

- `lgs.py` - Logic Gate Simulator: Demonstrates conditional logic by simulating AND, OR, and XOR gates with user inputs.
- `sensor_filter.py` - Sensor Filter: Introduces list processing and filtering to separate valid sensor readings from faults.
- `Sensor_data_sorter.py` - Sensor Data Sorter: Refactors filtering into a function, showing code reusability and modular design.
- `sensor_dict.py` - Sensor Dictionary: Uses dictionaries to store sensor metadata and loops to display formatted readings.
- `sensor_log.txt` - Sample Log File: Contains timestamped sensor data for practicing file reading operations.

## How to Run the Scripts

1. Ensure Python is installed on your system.
2. Open a terminal in the repository directory.
3. Execute any script with: `python <filename>.py`

Examples:
```bash
python lgs.py          # Run the logic gate simulator
python sensor_filter.py # Analyze sensor data
python Sensor_data_sorter.py # Use the sorter function
python sensor_dict.py  # Display sensor info from dictionaries
```

For file I/O practice, you can create scripts that read from `sensor_log.txt`.

## Key Concepts Demonstrated

- **Conditionals**: Used in `lgs.py` for gate logic and in filtering scripts for range checks.
- **Loops**: `for` loops in all scripts for iterating over lists or data.
- **Functions**: Introduced in `Sensor_data_sorter.py` to encapsulate logic.
- **Data Structures**: Lists in early scripts, dictionaries in `sensor_dict.py`.
- **File Handling**: `sensor_log.txt` as a data source for future file-reading exercises.
- **Modularity**: Progressing from procedural code to functional code.

## Ideas for Further Practice

- Add error handling for invalid inputs in `lgs.py`.
- Implement file reading in `Sensor_data_sorter.py` to process `sensor_log.txt`.
- Create a script that writes logs to `sensor_log.txt`.
- Experiment with classes for object-oriented sensor representations.
- Add more data structures like sets or tuples.
- Build a simple GUI or web interface for the logic gate simulator.

## Learning Tips

- Run each script and modify values to see how outputs change.
- Try rewriting scripts using different approaches (e.g., list comprehensions).
- Add comments to explain what each part does.
- Commit changes frequently to track progress.
- When stuck, refer to Python documentation or experiment in a REPL.

Experiment freely and enjoy the process of building Python skills one step at a time!
