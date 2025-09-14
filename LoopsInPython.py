# For Loop in Python

for i in range(0 , 5, 1):

    print(i,end=" -> ")

print("End")


# while Loop in Python

num = 0

while( num <= 10):

    print(num , end="->")

    num+=1


print("End")


# break And Continue in python

for i in range( 0 , 10 , 1):

    if(i == 5):

        break

    print(i, end=" -> ")

print("Break End ! !")


for i in range( 0 , 3 ):

    for j in range( 0 , 3):

        if( i == j):

            print(i , "  ", j , " XXX ")
            continue

        print(" i: ",i,"   j: ",j,end="\n")

print("Continue Ended !! ")