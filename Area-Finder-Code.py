#!/usr/bin/env python3
def area_find(height, width):
    return float(height) * float(width)

while True:
    try:
        height = input("Please enter the height: ")
        width  = input("Please enter the width: ")
        area = area_find(height, width)
        print("The area is {} cm²".format(area), "\n")
    except KeyboardInterrupt:
        exit()
