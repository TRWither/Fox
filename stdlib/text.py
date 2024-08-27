def text(command, txt, replace=None, by=None):
    if command == "upper":
        print(txt.upper())
    
    elif command == "lower":
        print(txt.lower())
    
    elif command == "invert":
        print(txt[::-1])
    
    elif command == "length":
        print(len(txt))
    
    elif command == "output":
        print(txt)
    
    else:
        print(f"TextError: Command '{command}' not recognized.")