# Python Learning Repository

This repository is a personal Python learning workspace. It contains small practice programs and step-by-step improvements that help build confidence in writing Python code.

## Learning Goals

- Practice writing simple Python scripts
- Learn how to use conditionals, loops, functions, and data structures
- Understand basic input/output and file handling
- Write reusable code and organize logic into functions
- Work with external APIs and handle runtime exceptions
- Keep building gradually by adding new concepts to the repository

## What You Have Learned So Far

- Basic Python syntax with `print()` and variables
- Conditional logic using `if`, `elif`, and `else`
- Looping over data with `for`
- Accepting input from users and displaying results
- Filtering list data based on rules
- Creating reusable functions for repeated logic
- Using dictionaries to represent structured data
- Reading and writing data from files
- Formatting output cleanly with f-strings
- Working with external web APIs using `requests`
- Handling errors and retrying operations when something goes wrong
- Using a virtual environment for dependency isolation

## Repository Contents

- `lgs.py` - Logic Gate Simulator
  - Prompts for two binary inputs and a gate type
  - Computes AND, OR, or XOR logic and displays the result
- `sensor_filter.py` - Sensor Filter
  - Filters a list of sensor values into valid readings and faults
- `Sensor_data_sorter.py` - Sensor Data Sorter
  - Refactors sensor filtering into a reusable function
  - Prints totals for valid and fault readings
- `sensor_dict.py` - Sensor Dictionary Example
  - Stores sensor metadata in dictionaries
  - Iterates through sensor records and prints formatted output
- `sensor_log.txt` - Sample sensor log data
  - Timestamped sensor readings useful for file I/O practice
- `space_monitor.py` - Space Monitor
  - Fetches live ISS position data from a web API
  - Uses `requests`, JSON parsing, and exception handling
  - Retries automatically when the network connection fails

## How to Run

1. Activate your virtual environment if you have one:
   ```bash
   e:\python-learning\.venv\Scripts\Activate.ps1
   ```
2. Run any script from the project folder:
   ```bash
   python lgs.py
   python sensor_filter.py
   python Sensor_data_sorter.py
   python sensor_dict.py
   python space_monitor.py
   ```

> Note: `space_monitor.py` requires internet access and the `requests` library.

## Practical Next Steps

- Add input validation to `lgs.py` so only `0` or `1` values are accepted
- Update `Sensor_data_sorter.py` to read values from `sensor_log.txt`
- Create a new script that writes new sensor entries into `sensor_log.txt`
- Add a function to `sensor_dict.py` that calculates summary statistics
- Build a safe retry mechanism and logging for `space_monitor.py`
- Try writing a class for a sensor object or an ISS tracker

## Learning Advice

- Make small changes often and test immediately
- Comment your code to explain what each part does
- Compare different ways to solve the same problem
- Keep the repository as a record of your progress
- Experiment with new Python features as you learn them

This repository is a growing journal of your Python practice. Keep adding simple programs, then turn those programs into reusable functions and more organized code over time.
