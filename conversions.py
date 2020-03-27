import sys

# Convert Fahrenheit to Celsius
# ({numF} - 32)*5/9 
def FtoC(F):
    return (F - 32)*5/9

# Convert Celsius to Fahrenheit
# ({numC} * 5/9) + 32
def CtoF(C):
    return C * 9/5 + 32

# Convert Miles to Kilometers
# MILES * 1.609
def milestoKM(miles):
    return miles * 1.609

# Convert Kilometers to Miles
# KM / 1.609
def KMtoMiles(KM):
    return KM / 1.609

# Convert Cups to Tablespoons
# 1 Cup = 16 Tbsp
def cuptoTbsp(cup):
    return float(cup * 16)

# Convert Tablespoons to Cups
# 1 Tbsp = 1/16 Cup
def TbsptoCup(Tbsp):
    return float(Tbsp * 1/16)

# Convert Tablespoons to Teaspoons
# 1 Tbsp = 3 tsp
def TbsptoTsp(Tbsp):
    return Tbsp * 3

# Convert Teaspoons to Tablespoons
# 1 tsp = .33 Tbsp
def tspToTbsp(tsp):
    return float(tsp * (1/3))

# Liquid Measure - Cups to Liters
# 1 cup = 236.5882365mL
def cupToL(cup):
    return cup * 236.5882365

# Liquid Measure - Liters to Cups
# 1 L = 4.22675 cup
def LtoCup(L):
    return L * 4.22675

# Dry Measure - Sugar, granulated - Cups to Grams
# 1 cup = 200g
def cuptoG(cup):
    return cup * 200

# Dry Measure - Sugar, granulated - Grams to Cups
# 1 gram = .005 cup | 4.17 g = 1 tsp | .52 g = 1/8 tsp
def gtoCup(g):
    return float(g * .005) 


direction = 0
endRun = False
print("\n\tWhat would you like to convert today?\n")
direction=int(raw_input("\n\t1. Temperature (F, C)\n\t2. Distance (Miles, KM)\n\t3. Measure (Cups, Tbsp)\n\t4. Nothing, take me away from here\n\nEnter number: "))

while (not endRun):

    if (direction == 1):
        print("\nWhich to you know? C or F")
        cf = raw_input(": ")
        if (cf == "c" or cf == "C"):
            cel = float(raw_input("Enter Celsius: "))
            print("\n%4.1fC is %4.1fF.\n" % (cel, CtoF(cel)))
        elif (cf == "f" or cf == "F"):
            fah = float(raw_input("Enter Fahrenheit: "))
            print("\n%4.1fF is %4.1fC.\n" % (fah, FtoC(fah)))
        else:
            break
        endRun = False
    if (direction == 2):
        print("\nWhich do you know? (M)iles or (K)M")
        mk = raw_input(": ")
        if (mk == "m" or mk == "M" or mk == "miles" or mk == "Miles"):
            miles = float(raw_input("Enter Miles: "))
            print("\n" + str(miles) + " miles is equivalent to %4.2fkm\n" % milestoKM(miles))
        elif (mk == "k" or mk == "K" or mk == "km" or mk == "KM"):
            km = float(raw_input("Enter Kilometers: "))
            print("\n" + str(km) + "km is equivalent to %4.2f Miles\n" % KMtoMiles(km))
        else:
            break
        endRun = False
    if (direction == 3):
        print("\nWhich do you know? (C)ups or (T)ablespoons")
        ct = raw_input(": ")
        if (ct == "c" or ct == "C"):
            cupsMeasure = float(raw_input("How many cups? "))
            print("\n" + str(cupsMeasure) + " cups is " + str(cuptoTbsp(cupsMeasure)) + " tablespoons.\n")
        elif (ct == "t" or ct == "T"):
            tbspMeasure = float(raw_input("How many Tablespoons? "))
            print("\n" + str(tbspMeasure) + " Tablespoons is " + str(TbsptoCup(tbspMeasure)) + " cups\n")
        else:
            break
        endRun = False
    if (direction == 4 or direction ==""):
        print("\n\tExiting program.....\n") 
        sys.exit()

    if (direction > 4 or isinstance(direction, str)):
        break

    direction=int(raw_input("\n\t1. Temperature (F, C)\n\t2. Distance (Miles, KM)\n\t3. Measure (Cups, Tbsp)\n\t4. Nothing, take me away from here\n\nEnter number: "))

else:
    print("\n\tExiting program.....\n")
    sys.exit()
