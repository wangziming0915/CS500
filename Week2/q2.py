print("This program calculate the area of simple shapes.")
def get_rectangle_area(length, width):
    return length * width

def get_triangle_area(base,height):
    return base * height / 2

def get_circle_area(radius):
    return radius * radius * 3.14

shape = input("Please enter the shape: ")

if(shape == 'rectangle'):
    length = int(input("Please enter length: "))
    width = int(input("Please enter width: "))
    print("The area of the shape is: " + str(get_rectangle_area(length, width)))
elif(shape == 'triangle'):
    base = int(input("Please enter base: "))
    height = int(input("Please enter height: "))
    print("The area of the shape is: " + str(get_triangle_area(base, height)))
else:
    radius = int(input("Please enter radius: "))
    print("The area of the shape is: " + str(get_circle_area(radius)))