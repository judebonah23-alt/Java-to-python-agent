---
name: java-to-python
description: Read a Java string reversal method, convert it to Python, verify the conversion with unit tests, and summarize the results.
---

# Java to Python Conversion Agent

You are a code conversion agent. Your job is to translate a Java method into equivalent Python code while keeping the same behavior.

## Source

The Java method is located in `ReverseString.java` at the root of the repository.

Read the file and understand how the `reverseString` method works before writing any Python code.

## Tasks

Complete the following steps in order:

1. Read the `reverseString` method in `ReverseString.java`.
2. Convert the method into an equivalent Python function named `reverse_string`.
3. Create a new file named `reverse_string.py` that contains:
   - The converted function
   - Type hints
   - A short docstring
   - A comment explaining how the Python code matches the Java loop
   - An `if __name__ == "__main__":` block that prints:

   ```text
   Input: hello
   Output: olleh
   ```

4. Make sure the Python function behaves the same as the Java method:
   - `"hello"` returns `"olleh"`
   - An empty string returns an empty string
   - Passing `None` should naturally raise an exception (do not add special handling)

5. Create a file named `test_reverse_string.py` using Python's built-in `unittest` module.

6. Write tests for:
   - A normal string (`"hello"`)
   - An empty string
   - A single character
   - A palindrome (`"racecar"`)
   - A string with spaces and punctuation (`"Hello, World!"`)
   - Passing `None` raises an exception

7. Run the following commands and make sure all tests pass:

   ```bash
   python -m unittest -v test_reverse_string.py
   python reverse_string.py
   ```

8. If any tests fail, update the Python implementation and rerun the tests until they all pass.

9. Provide a short summary that includes:
   - How the Java method was converted into Python
   - The terminal output from the test command
   - The terminal output from running `python reverse_string.py`
   - Any small differences between Java and Python that are relevant

## Rules

- Do not modify or delete `ReverseString.java`.
- Only create the following files:
  - `reverse_string.py`
  - `test_reverse_string.py`

