# Python Module 03: Data Alchemist and Python Fundamentals

This repository contains the exercises for "Python Module 03," a project focused on mastering fundamental Python concepts and data structures. The primary goal is to demonstrate a solid understanding of core Python features through practical, well-structured examples. Each exercise is designed to highlight specific aspects of Python for efficient data processing and analysis, prioritizing clarity and comprehension mastery.

## Concepts Covered

The module systematically explores the following key Python concepts:

*   **Command-Line Argument Processing (`sys.argv`):** Understanding how to interact with scripts via the command line.
*   **Basic Data Structures:** Lists, Tuples, Sets, and Dictionaries – their characteristics, use cases, and operations.
*   **List Comprehensions:** Efficiently creating and transforming lists.
*   **Dictionary Comprehensions:** Constructing dictionaries concisely.
*   **Set Comprehensions:** Generating sets for unique elements.
*   **Generators:** Implementing memory-efficient iterators for large data streams.
*   **Nested Data Structures:** Modeling complex data relationships using nested dictionaries.
*   **Error Handling:** Graceful management of exceptions and invalid inputs.

## Project Structure and Exercises

The project is organized into several exercises, each focusing on a specific Python concept:

### `ex0/ft_command_quest.py` - Command-Line Argument Processing
*   **Focus:** Demonstrates the use of `sys.argv` for accessing and processing command-line arguments, including displaying the program name, counting arguments, and handling individual arguments.

### `ex1/ft_score_analytics.py` - List Processing & Analytics
*   **Focus:** Processes a list of player scores provided via command-line arguments. It includes parsing numeric input, handling invalid input gracefully, and calculating basic analytics like total, average, and high/low scores.

### `ex2/ft_coordinate_system.py` - Tuple Operations
*   **Focus:** Explores tuple operations for managing 3D coordinate systems. Key areas include creating and manipulating 3D coordinate tuples, tuple unpacking, calculating Euclidean distances, and custom exception handling.

### `ex3/ft_achievement_tracker.py` - Set Operations
*   **Focus:** Utilizes sets for efficient data deduplication and analysis of unique items. It demonstrates operations like union, intersection, and difference to find commonalities or unique elements among collections.

### `ex4/ft_inventory_system.py` - Dictionary Operations & Data Modeling
*   **Focus:** Showcases comprehensive use of dictionaries, including nested dictionaries, for modeling complex data relationships, such as player inventories. It covers managing item quantities, categories, and demonstrating dictionary access and updates.

### `ex5/ft_data_stream.py` - Generators & Memory Efficiency
*   **Focus:** Introduces generators for processing data streams efficiently. This exercise highlights how generators use the `yield` keyword to produce values on-demand, making them highly memory efficient for large datasets.

### `ex6/ft_analytics_dashboard.py` - List, Dict, and Set Comprehensions
*   **Focus:** The core of this module, demonstrating mastery of list, dictionary, and set comprehensions. It applies these powerful constructs for elegant data transformation, filtering, and comprehensive analysis within a simulated game analytics dashboard.

## How to Run

To run any of the Python scripts, navigate to the project's root directory and execute them using `python3`. For exercises that accept command-line arguments, provide them as needed.

**Example for `ex0/ft_command_quest.py`:**
```bash
python3 ex0/ft_command_quest.py hello world 42
```

**Example for `ex6/ft_analytics_dashboard.py` (no arguments, runs all demonstrations):**
```bash
python3 ex6/ft_analytics_dashboard.py
```
