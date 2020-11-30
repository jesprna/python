def div(a,b):
    if(b == 0):
        return print("This is not possible. Are you Mad?")
    else:
        c= a/b
        return print(c);



a = input("Enter first value: ")
b = input("Enter second value: ")
a = int(a)
b = int(b)

div(a,b)