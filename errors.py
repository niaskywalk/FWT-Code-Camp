import sys
value1 = int(sys.argv[1])
value2 = int(sys.argv[2])

if(value1 > value2):
    print("The first parameter is larger.")
elif (value1 < value2):
    print("The second parameter is larger.")
else:
    print("The parameters are equal.")

