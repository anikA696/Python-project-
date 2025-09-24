start = int(input("Shuru kaha sy karey"))
end = int(input("End kaha per karey"))
   
for i in range(start,end+1):
    print( "\nTable of", i)
    for j in range(1,11):
        print(i, "x", j, "=", num*j)
