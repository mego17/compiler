import re
# Define token patterns using regular expressions
token_patterns = [
    (r'int', 'INT_KEYWORD'),
    (r'float', 'FLOAT_KEYWORD'),
    (r'if', 'IF_KEYWORD'),
    (r'else', 'ELSE_KEYWORD'),
    (r'while', 'WHILE_KEYWORD'),
    (r'for', 'FOR_KEYWORD'),
    (r'print', 'PRINT_KEYWORD'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'), 
    (r'\d+\.\d+', 'FLOAT_NUMBER'),
    (r'\d+', 'INT_NUMBER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS_OPERATORS'),
    (r'\*', 'MULTIPLY_OPERATORS'),
    (r'/', 'DIVIDE_OPERATORS'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'{', 'LBRACE'),
    (r'}', 'RBRACE'),
    (r';', 'SEMICOLON'),
    (r'=', 'ASSIGNMENT'),
]

# Combine token patterns into a single regular expression
token_regex = '|'.join(f'({pattern})' for pattern, _ in token_patterns)

# Function to tokenize the source code
def tokenize(source_code):
    tokens = []
    for match in re.finditer(token_regex, source_code):
        for i in range(1, len(match.groups()) + 1):
            if match.group(i):
                token_type = token_patterns[i - 1][1]
                tokens.append((token_type, match.group(i)))
    return tokens

# example of input statement
#source_code = "int main() { int x = 5; return x; }"
source_code= input("Enter a string: ")
tokens = tokenize(source_code)


file = open('Untitled-2.txt','w')
for token_type, token_value in tokens:
    file.write(f"<{token_type}> : {token_value}\n") # the output print on text file
    print(f"<{token_type}> : {token_value} ")  # the output print on console
file.close() 
