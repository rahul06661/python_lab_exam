def triangle(b,h):
    return (b*h)/2

def rectangle(l,b):
    return l*b

def circle(r):
    return 3.14*r*r

cont=True
while(cont):
    opt=int(input(""" \n1:triangle araa 
2: rectangle area
3 :circle area 
4 :exit """))
    if opt==1:
        bred=int(input("enter triangle breadth"))
        heig = int(input("enter triangle height"))
        print("Area of triangle is  ",triangle(bred,heig))
    if opt==2:
        bred=int(input("enter Rectangle breadth"))
        leng = int(input("enter Rectangle height"))
        print("Area of Rectangle is  ",rectangle(bred,leng))
    if opt==3:
        radius=int(input("enter circle radius"))
        print("Area of circle is ",circle(radius))
    if opt>3:
        cont=False




