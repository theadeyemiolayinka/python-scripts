# camel case to snake case converter
code transforming camelCase (or PascalCase) string to snake_case. 

# operation
code uses regular expression operations to separate words with "_":
- at the meeting point of lowercase and uppercase letters,
- where numbers meet letters,
- and to replace any special characters with underscores.

# usage
simpy pass STR containing camel case to function; it will return STR with snake case. The code is commented for readability and includes tests.

# requirements
standard library 're' module.
