def calc(expression):
    try:
        result = eval(expression)
        print(result)
    except ZeroDivisionError:
        print("CalcError: cannot divide a number by 0")
    except Exception as e:
        print(f"CalcError: {e}")