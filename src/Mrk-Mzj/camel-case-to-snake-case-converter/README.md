# Camel Case to Snake Case converter
convert camelCase (or PascalCase) string to snake_case.

# Operation
code uses regular expressions to:
- find lowercase to uppercase letter combinations,
- find where numbers meet letters,
- replace special characters with underscores.

# Usage
simply pass a string containing a camel or pascal case to the function, and it will return the STR with the snake case. 
The code is commented for readability and includes tests.

# Requirements
standard library re module.
