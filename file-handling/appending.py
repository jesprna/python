file = open("test-write.txt", "a")
x = ["reds", "blues", "greens", "blacks", "yellows", "oranges"]
for item in x:
    file.write(item+"\n")


file.close()