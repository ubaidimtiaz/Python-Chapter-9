import math

def area_circle(r):
    #This function is generates area of circle by using radius r
    print('The area of the circle is ', math.pi*(r**2))
    return

def input_radius():
    #This function asks the user for radius
    x=input('What is the radius for which you wanna calculate the area of circle\n')
    return x


def calculate_radius(xc,yc, xp, yp):
    dx=abs(xp-xc)
    dy=abs(yp-yc)
    radius = math.sqrt(dx**2 + dy**2)
    return area_circle(radius)


def input_points():
    xc, yc, xp, yp = input("Please enter the points in the following order seperated by spaces xc,yc,xp,yp\n").split()
    return (int(xc), int(yc), int(xp), int(yp))


def is_divisible(x, y):
    return x%y==0


def factorial(n):
    if n==0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n*recurse
        return result


#print(factorial(4))


