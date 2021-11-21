def inputInt( message ):
    message = int(input("Enter your number:"))
    return message

def inputFloat( message ):
    message = float(input("Enter your number:"))
    return message
def inputBoolean( message ):
    message = bool(input("Enter your number:"))
    return message

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print(n+m)