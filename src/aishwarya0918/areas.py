def areacircle():
    r_c=float(input("Enter radius of circle:"))
    area=float(3.14*r_c*r_c)
    print("The area of circle is",area)
    return

def areasquare():
    s_s=float(input("Enter length of side of square:"))
    area=float(s_s*s_s)
    print("The area of square is",area)
    return
    
def arearectangle():
    l_r=float(input("Enter length of rectangle:"))
    b_r=float(input("Enter breadth of rectangle:"))
    area=float(l_r*b_r)
    print("The area of rectangle is",area)
    return
    
def areatrapezoid():
    b1_t=float(input("Enter length of base1 of trapezoid:"))
    b2_t=float(input("Enter length of base2 of trapezoid:"))
    h_t=float(input("Enter heigth of trapezoid:"))
    area=float(((b1_t+b2_t)*h_t)/2)
    print("The area of Trapezoid is",area)
    return
    
def main():
    option=0
    while(option!=5):
        print("\nMENU")
        print("Enter the choice you want")
        print("1.Area of Circle")
        print("2.Area of Square")
        print("3.Area of Rectangle")
        print("4.Area of Trapezoid")
        print("5.Exit")
        option = int(input("Enter your choice:"))
        if (option==1):
            areacircle()
        if (option==2):
            areasquare()
        if (option==3):
            arearectangle()
        if (option==4):
            areatrapezoid()
        elif (option==5):
            print("THANK YOU!")
main()
