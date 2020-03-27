print("Day 003: Loops and Lists")
print("Activity\n")

print("Print numbers between 10 and 20:\n")

x = 10
while x <= 20:
    print x
    x = x + 1
print("\n\nPrint 100 to 0 at step 5:\n")
y = 100
while y > -1:
    print y
    y = y - 5
print("\n\nVersion 1: Print 1 to 100 with X at every other number:\n")
skip = 1
while skip <= 100:
    print skip
    print("X")
    skip = skip + 2
print("\n\nVersion 2: Print 1 to 100 with X at every even number:\n")
skip2 = 1
while skip2 <= 100:
    if (skip2%2):
        print("X")
    else:
        print skip2
    skip2 = skip2 + 1
print("\n\n\nPrint 5 to 25 on a single line:\n")

numbers = ""
add5 = 5
while add5 <= 25:
    numbers = numbers + str(add5) + " "
    add5 = add5 + 5
print numbers

