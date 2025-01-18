def arithmetic_arranger(problems, show_answers=False):
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize lists to hold formatted components
    top_numbers = []       # First line of each problem
    bottom_numbers = []    # Second line of each problem
    dashes = []            # Separator line
    answers = []           # Calculated answers (optional)
    
    # Process each problem
    for problem in problems:
        parts = problem.split()
        
        # Validate the format of the problem
        if len(parts) != 3:
            return "Error: Each problem must be a string formatted like 'number operator number'."
        
        left_operand, operator, right_operand = parts
        
        # Validate the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validate that both operands are numbers
        if not (left_operand.isdigit() and right_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Validate the length of each operand
        if len(left_operand) > 4 or len(right_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the result based on the operator
        if operator == '+':
            answer = str(int(left_operand) + int(right_operand))
        else:
            answer = str(int(left_operand) - int(right_operand))
        
        # Determine the width needed for formatting (based on the larger operand)
        max_length = max(len(left_operand), len(right_operand)) + 2  # +2 for the operator and space
        
        # Format each component and add to respective lists
        top_numbers.append(left_operand.rjust(max_length))
        bottom_numbers.append(operator + ' ' + right_operand.rjust(max_length - 2))
        dashes.append('-' * max_length)
        answers.append(answer.rjust(max_length))
    
    # Combine all components into a single formatted string
    arranged_problems = '    '.join(top_numbers) + '\n' + '    '.join(bottom_numbers) + '\n' + '    '.join(dashes)
    
    # Add the answers if requested
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
