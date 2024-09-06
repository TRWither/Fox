# The Fox Programming Language
**Fox** is a minimalist, command-line programming language designed for quick and simple tasks. Fox doesn't require source files; everything happens directly in the terminal, making it an excellent choice for performing arithmetic operations, string manipulations, and file operations in an efficient, no-frills way.

## Features
### 1. Arithmetic operations
Fox supports basic arithmetic operations:
- Addition (`+`), substraction (`-`), multiplication (`*`), division (`/`), integer division (`//`), modulo (`%`)
- Supports parentheses and negative numbers for both integers and floats.
#### Example:
```
/ 3*(5+8/(-9))+12*(-3.5)+4//5%8
```
### 2. Text manipulation
You can easily manipulate strings in Fox:
- Convert a string to **uppercase** or **lowercase**
- **Reverse** a string
- Get the **length** of a string
- **Print** a string to the output
#### Example:
```
/ text reverse Hello world!
```

### 3. File manipulation
Fox provides basic file manipulation commands:
- **Create**, **delete**, **search**, **edit** and **empty** files
#### Example:
```
/ file find /path/to/your/file
```

## Installation
### On Linux
1. Clone the repository:
```bash
git clone https://github.com/TRWither/Fox
```
2. Run the interpreter:
```bash
chmod +x /path/to/FOX/cli.py
python3.x /path/to/FOX/cli.py
```
3. (Optional) Add a custom command to easily run Fox:
```bash
your_editor ~/.bashrc
```
Create a custom command in your .bashrc:
```bash
fox() {
    chmod +x /path/to/FOX/cli.py
    python3.x /path/to/FOX/cli.py
}
```
Then, source the .bashrc file and run Fox directly from the terminal:
```bash
source ~/.bashrc
fox
```
