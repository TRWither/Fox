import os

def file_(command, filename, write=None):
    try:
        if command == "read":
            if os.path.isfile(filename):
                with open(filename, 'r') as file:
                    print(file.read())
            else:
                print("FileError: file not found or is a directory")

        elif command == "write":
            if os.path.isdir(filename):
                print("FileError: cannot write to a directory")
            else:
                with open(filename, 'w') as file:
                    if write is not None:
                        file.write(write)
                        print("File written successfully.")
                    else:
                        print("FileError: you must provide content to write in the file")

        elif command == "empty":
            if os.path.isfile(filename):
                with open(filename, 'w') as file:
                    pass
                print("File emptied successfully.")
            else:
                print("FileError: file not found or is a directory")

        elif command == "make":
            if not os.path.exists(filename):
                with open(filename, 'a').close():
                    print("File created successfully.")
            else:
                print("FileError: file already exists")

        elif command == "remove":
            if os.path.isfile(filename):
                os.remove(filename)
                print("File removed successfully.")
            else:
                print("FileError: file not found or is a directory")

        elif command == "find":
            if os.path.exists(filename):
                print("File found.")
            else:
                print("FileError: file not found")

        else:
            print(f"FileError: command '{command}' not recognized")

    except Exception as e:
        print(f"FileError: {e}")