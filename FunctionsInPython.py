# Functions Creation

def printing(name , steps ):

    for i in range( 0 , steps , 1):

        print(name,end="\n")


name = str(input("Enter Your Name : "))

steps = int(input("Enter the number of steps You want to print Your Name : "))

print()

printing(name , steps )         # Functions Calling


