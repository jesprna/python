file = open("test-write.txt", "w")
x = ["red", "blue", "green", "black", "yellow", "orange"]
for item in x:
    file.write(item+"\n")


file.close()


file2 = open("test-write.txt", "r")
y = file2.read()
print(y)

