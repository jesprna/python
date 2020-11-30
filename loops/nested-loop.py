x = ["big", "small", "bold", "light", "heavy"]

y = ["iron", "silver", "gold", "platinum", "diamond"]


a=0
for i in x:
    b=0
    for j in y:
        print(i,j)
        print(x[a], y[b])
        b += 1
    a +=1