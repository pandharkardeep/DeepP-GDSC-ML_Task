import re

def parse_expression(expression):

  tokens = []
  for token in re.split(r"(\d+|\(|\)|[+-*/])", expression):
    if token.strip():
      tokens.append(token)

  return tokens

def evaluate_expression(tokens):
  
  stack = []
  for token in tokens:
    if token.isdigit():
      stack.append(int(token))
    elif token == "(":
      stack.append(token)
    elif token == ")":
      operand2 = stack.pop()
      operand1 = stack.pop()
      operator = stack.pop()
      stack.append(eval(operator + " " + str(operand1) + " " + str(operand2)))
    else:
      operator = token

  return stack[-1]

def main():
  expression = input("Enter an expression: ")
  tokens = parse_expression(expression)
  result = evaluate_expression(tokens)
  print("The result is: ", result)

if __name__ == "__main__":
  main()