def ctof():
     c =float(input("Enter value in degree Celsius:"))
     f= (c*1.8)+32
     print("The corresponding value in degree Fahrenheit is:")
     print(f)
     return
 
def ftoc():
     f =float(input("Enter value in degree Fahrenheit:"))
     c = ((f-32)*5)/9
     print("The corresponding value in degree Celsius is:")
     print(c)
     return
    
def main():
    option=0
    while(option!=3):
        print("\nMENU")
        print("Enter the conversion you want to do:")
        print("1.Celcius to Fahrenheit")
        print("2.Fahrenheit to Celsius")
        print("3.Exit")
        option = int(input("Enter your choice:"))
        if (option==1):
            ctof()
        if (option==2):
            ftoc()
        elif (option==3):
            print("THANK YOU!")
main()
