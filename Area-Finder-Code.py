def AreaFinder():
    height = float(input("Please enter the height: "))

    width  = float(input("Please enter the width: "))

    area = height * width

    print("The area is {}cm\u00b2".format(area), "\n")

while(True):
    AreaFinder()
