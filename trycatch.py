#try catch

try:
    number=int(input("Enter the no:"))
    print(1/number)
except ZeroDivisionError:                 #zerodivisionerror
    print("Cannot divide using zero")
except ValueError:
    print("Invalid input enter valid number")
except Exception:
    print("Invalid output")
finally:
    print("Fix the code")
