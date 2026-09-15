# pytodo — A Python CLI To-Do List Application

A command-line (CLI) To-Do list application built from scratch in Python.
Tasker lets you add, view, and delete tasks from an in-memory list, with
full input validation and error handling at every step.

> **Where you run your day.**

---

## Features

- **Add tasks** — enter a new task with validation (blank, whitespace-only,
  and over-250-character inputs are rejected with a clear error message).
- **View tasks** — displays all current tasks in a numbered list. Shows an
  error if the list is empty.
- **Delete tasks** — shows the current task list, then lets you remove a task
  by its number. Handles empty lists, out-of-range numbers, and non-integer
  input.Shows an error if the list is empty.
- **Quit** — asks for confirmation (Y/N) before exiting to avoid accidental
  user fat fingers.
- **Input validation** — every user input is checked. Invalid menu selections,
  non-integer input, and other bad inputs produce a descriptive error message
  and prompt you to try again.
- **Cross-platform** — works on Windows, macOS, and Linux.

---

## Requirements

- **Python 3.8+** (uses the walrus operator `:=`)
- No external dependencies — only the Python standard library (`os`,
  `subprocess`) is used.

---

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python tasker.py
   ```
