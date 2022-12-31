import re

def lexical_analyzer(expression):
    # regular expression that matches digits, alphabets, and characters
    pattern = r'\d+|[a-zA-Z]+|[^\s\d+a-zA-Z]+'
    #regular expression
    new_exp = re.findall(pattern, expression) #using builtin function findall

    return new_exp

# Test the lexical analyzer
expression = input("Enter an expression: ")
tokens = lexical_analyzer(expression)
print(tokens)