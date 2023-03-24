print("input")
number = int(input("Please specify the number of pyramid floors : "))
print("output")
for x in range(number) : 
    for y in range(number-x-1) :
        print(" ",end=" ")
    for z in range(2*x+1) :
        print("*", end=" ")
    print()
