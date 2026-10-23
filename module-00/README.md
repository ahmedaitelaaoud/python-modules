# 🌱 Growing Code - Python Module 00

**Python Fundamentals Through Garden Data**

A beginner-friendly introduction to Python programming through community garden scenarios. This module covers fundamental syntax and semantics while analyzing garden data to support sustainable community initiatives.

## 📋 Project Overview

This project introduces Python's core concepts through practical, real-world exercises. Each exercise builds upon the previous one, developing essential programming skills in an engaging context.

**Version:** 1.0  
**Language:** Python 3.10+  
**Code Standard:** flake8 compliant

## 🎯 Learning Objectives

- Master Python expressions and variables
- Understand function definitions and calls
- Implement control flow (conditionals and loops)
- Learn both iterative and recursive approaches
- Introduction to type annotations
- Handle user input and output operations

## 📚 Exercises

### Exercise 0: Hello Garden
**File:** `ex0/ft_hello_garden.py`

Your first Python function! Displays a welcome message to the garden community.

```python
>>> ft_hello_garden()
Hello, Garden Community!
```

### Exercise 1: Garden Plot Area
**File:** `ex1/ft_plot_area.py`

Calculates the area of a rectangular garden plot based on user input.

```python
>>> ft_plot_area()
Enter length: 5
Enter width: 3
Plot area: 15
```

### Exercise 2: Harvest Total
**File:** `ex2/ft_harvest_total.py`

Sums up harvest weights from 3 different days.

```python
>>> ft_harvest_total()
Day 1 harvest: 5
Day 2 harvest: 8
Day 3 harvest: 3
Total harvest: 16
```

### Exercise 3: Plant Age Check
**File:** `ex3/ft_plant_age.py`

Determines if a plant is ready to harvest based on its age (>60 days).

```python
>>> ft_plant_age()
Enter plant age in days: 75
Plant is ready to harvest!
```

### Exercise 4: Water Reminder
**File:** `ex4/ft_water_reminder.py`

Checks if plants need watering based on days since last watering (>2 days).

```python
>>> ft_water_reminder()
Days since last watering: 4
Water the plants!
```

### Exercise 5: Count to Harvest
**Files:** `ex5/ft_count_harvest_iterative.py`, `ex5/ft_count_harvest_recursive.py`

Implements both iterative and recursive approaches to count down days until harvest.

```python
>>> ft_count_harvest_iterative()
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```

### Exercise 6: Garden Summary
**File:** `ex6/ft_garden_summary.py`

Creates a formatted summary of garden information.

```python
>>> ft_garden_summary()
Enter garden name: Community Garden
Enter number of plants: 25
Garden: Community Garden
Plants: 25
Status: Growing well!
```

### Exercise 7: Seed Inventory with Type Annotations
**File:** `ex7/ft_seed_inventory.py`

Manages seed inventory with type hints, supporting multiple unit types.

```python
>>> ft_seed_inventory("tomato", 15, "packets")
Tomato seeds: 15 packets available
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- flake8 linter (for code quality checks)

### Installation

```bash
# Clone the repository
git clone [your-repo-url]
cd python-module-00

# Install flake8 (optional, for linting)
pip install flake8
```

### Testing Your Code

A helper file `main.py` is provided to test your exercises:

```bash
python3 main.py
```

This will let you:
- Test individual exercises
- Run all exercises at once
- See clear error messages

## 📝 General Instructions

- Each exercise must be in its own directory
- Each file should contain **only** the requested function
- Function names must match exactly as specified
- Write functions only (no `if __name__ == "__main__":` blocks)
- Input validation is not required unless explicitly mentioned
- Code must be flake8 compliant

## 🛠️ Project Structure

```
python-module-00/
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_plot_area.py
├── ex2/
│   └── ft_harvest_total.py
├── ex3/
│   └── ft_plant_age.py
├── ex4/
│   └── ft_water_reminder.py
├── ex5/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
├── ex6/
│   └── ft_garden_summary.py
├── ex7/
│   └── ft_seed_inventory.py
└── main.py (helper file for testing)
```

## 🤖 AI Usage Guidelines

This project encourages thoughtful AI usage:

✅ **Good Practice:**
- Use AI to understand concepts and explore ideas
- Review AI-generated code with peers
- Only use code you fully understand

❌ **Bad Practice:**
- Copy-paste AI code without understanding
- Rely solely on AI without peer review
- Submit code you can't explain during evaluation

## 📖 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## ⚠️ Evaluation Notes

During evaluation, you may be asked to:
- Explain your code line by line
- Trace through execution
- Modify your solutions
- Discuss alternative approaches

Make sure you understand every line you write!

## 📄 License

This project is part of a programming curriculum focused on sustainable community initiatives and educational excellence.

---

**Happy Coding! 🌱**

*Remember: Programming, like gardening, is about nurturing growth—both in code and in the communities we serve.*
