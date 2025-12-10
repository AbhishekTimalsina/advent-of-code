file = open("input_1.txt","r")

content= file.read()

# list =content.split("\n")


list = ["L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"]

position = 50
count=0

for x in list: 
    d= x[0]
    val= x[1:]
    val= int(val)
    if d=="L":
        val= val* -1

    current= position+ val
    print(current)
    position= current%100


    if position==0:
        count+=1


print(count)