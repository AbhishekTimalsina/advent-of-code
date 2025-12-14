file= open("input_3.txt","r")
# file= open("tmp.txt","r") 

unparsed_content= file.read()

content= unparsed_content.split("\n")

highest_joltage= []

for seq in content:
    sequence1 = sorted([int(s) for s in list(seq)])

    highest_index= seq.find(str(sequence1[-1]))

    highest_num= str(sequence1[-1])
    # print(seq[highest_index+1:])

    new_seq= seq[highest_index+1:]

    is_high_last= False
    if new_seq=="":
        is_high_last= True
        new_seq= seq[:highest_index]
    

    sequence2 = sorted([int(s) for s in list(new_seq)])

    second_high= str(sequence2[-1])

    jolt= int(highest_num+second_high)
    
    if is_high_last:
        jolt = int(second_high+ highest_num)


    highest_joltage.append(jolt)

print(sum(highest_joltage))

