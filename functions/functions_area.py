def area(a,b,shape='triangle'):
    if shape == 'triangle':
        print(f"Base: {a}")
        print(f"Height: {b}")
        return f"Area of triangle is {1/2*(a)*(b)}"
    else:
        print(f"Length: {a}")
        print(f"Width: {b}")
        return f"Area of rectangle is {a*b}"
print(area(3,4,'rectangle'))