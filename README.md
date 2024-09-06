# The Fox Programming Language
Fox is a minimalist programming language that works solely via the command line. It can be used to perform simple tasks, such as simple arithmetic operations and string and file manipulation. The code cannot be written to a source file.

## Functionnalities
**1. Arithmetic operations**
You can perform simple operations such as addition (+), subtraction (-), multiplication (*), division (/), integer division (//) and modulo (%). You can also use parentheses and negative numbers, both integers and floats.

**2. Text manipulation**
You can also perform the following operations on strings: uppercase or lowercase all characters, invert a string, obtain the length of a string or print a string.

**3. File manipulation**
You can also manipulate files. You can create, delete, search, edit, read and empty files.

## Installation
### Linux
**Step 1: clone the repository**
```
git clone https://github.com/TRWither/Fox
```
**Step 2: run the interpreter**
```
chmod +x /path/to/FOX/cli.py
python3.x /path/to/FOX/cli.py
```
**Step 3 (Optionnal): create a custom command to run it easier**
```bash
your_editor ~/.bashrc          # Or similar file
# In .bashrc:
fox() {
    chmod +x /path/to/FOX/cli.py
    python3.11 /path/to/FOX/cli.py
}
# Close your editor
source ~/.bashrc
fox
```

## Some examples
### 1. Check if a file exists
```
/ file find path/to/your/file
```
### 2. Reverse a string
```
/ text reverse "Hello world!"
```
### 3. Some maths
```
/ 3*(5+8/(-9))+12*(-3.5)+4//5%8
```
