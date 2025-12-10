import math

file = open("input_1.txt","r")

content= file.read()

list =content.split("\n")

# list = ["L68",
# "L30",
# "R48",
# "L5",
# "R60",
# "L55",
# "L1",
# "L99",
# "R14",
# "L82"]

position = 50
count=0

for x in list: 
    d= x[0]
    val= x[1:]
    val= int(val)


    dirValue= -1 if d=="L" else 1


    for i in range(abs(val)):
        position+=dirValue

        position= position%100
        if position==0:
            count+=1


print(count)