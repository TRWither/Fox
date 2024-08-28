from stdlib.calc import calc
from stdlib.file import file_
from stdlib.text import text

def main():
    while True:
        cmd = input("/ ").split(maxsplit=2)
        
        if not cmd:
            continue
        
        s = cmd[0]
        
        if s == "calc":
            if len(cmd) < 2:
                print("Usage: calc <expression>")
            else:
                expression = cmd[1]
                calc(expression)
        
        elif s == "file":
            if len(cmd) < 3:
                print("Usage: file <command> <filename> [<write>]")
            else:
                command = cmd[1]
                filename = cmd[2].split(maxsplit=1)[0]
                write = cmd[2].split(maxsplit=1)[1] if len(cmd[2].split(maxsplit=1)) > 1 else None
                file_(command, filename, write)
        
        elif s == "text":
            if len(cmd) < 3:
                print("Usage: text <command> <text>")
            else:
                command = cmd[1]
                txt = cmd[2]
                replace = cmd[3] if len(cmd) > 3 else None
                by = cmd[4] if len(cmd) > 4 else None
                text(command, txt, replace, by)
        
        elif s == "exit":
            break
        
        else:
            print(f"CommandError: unknow command {s}")

if __name__ == "__main__":
    main()
