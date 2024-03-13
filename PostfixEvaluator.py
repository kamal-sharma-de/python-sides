from collections import deque  # Using deque for efficient stack implementation

def balanced_parentheses(expression):
  """
  Checks if a given expression has balanced parentheses using a stack (deque).

  Args:
      expression: A string representing the mathematical expression.

  Returns:
      True if the expression has balanced parentheses, False otherwise.
  """
  stack = deque()
  opening_brackets = {"(": ")", "{": "}", "[": "]"}
  closing_brackets = set(opening_brackets.values())

  for char in expression:
    if char in opening_brackets:
      stack.append(char)
    elif char in closing_brackets:
      if not stack or opening_brackets[stack.pop()] != char:
        return False
  return not stack  # True if stack is empty (balanced), False otherwise

def evaluate_postfix(postfix_expression):
  """
  Evaluates a postfix expression using a stack (deque).

  Args:
      postfix_expression: A list of tokens representing the postfix expression.

  Returns:
      The numerical result of evaluating the postfix expression, or None if an error occurs.
  """
  stack = deque()
  for token in postfix_expression:
    if token.isdigit():
      stack.append(int(token))
    else:
      if len(stack) < 2:  # Check for sufficient operands before popping
        return None  # Indicate error (insufficient operands)
      operand2 = stack.pop()
      operand1 = stack.pop()
      result = eval(f"{operand1} {token} {operand2}")  # Using eval for basic arithmetic
      stack.append(result)
  return stack.pop()  # The final element in the stack is the result (or None if error)

# Example usage
expression = "({x + 2) * 3}"
if balanced_parentheses(expression):
  print("Expression has balanced parentheses.")
else:
  print("Expression has unbalanced parentheses.")

postfix_expr = ["2", "3", "+", "x"]  # Example with insufficient operands
result = evaluate_postfix(postfix_expr)
if result is not None:
  print(f"Postfix expression evaluation: {result}")
else:
  print("Error: Insufficient operands in postfix expression.")
