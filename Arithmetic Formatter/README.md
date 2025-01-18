# Arithmetic Formatter in Python

This project formats and arranges simple arithmetic problems (addition and subtraction) for display. It supports up to 5 problems at once and optionally shows the results.

## Features:
- **Format Arithmetic Problems**: Aligns operands and operators.
- **Supports Up to 5 Problems**: Prevents overcrowding by limiting the input.
- **Optional Answers**: Display results if requested.

## Usage:
1. Create a list of arithmetic problems in the format `"number operator number"`.
2. Call `arithmetic_arranger()` with the list.
3. Pass `True` as the second argument to show answers.

## Example:
```python
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

problems_with_answers = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems_with_answers, True))
```

## Error Handling:
    - **Too many problems**: If there are more than 5 problems, it returns: Error: Too many problems.
    - **Invalid operator**: If the operator is not + or -, it returns: Error: Operator must be '+' or '-'
    - **Non-digit operands**: If any operand is not a digit, it returns: Error: Numbers must only contain digits.
    - **Operand length exceeds 4 digits**: If a number has more than 4 digits, it returns: Error: Numbers cannot be more than four digits.
