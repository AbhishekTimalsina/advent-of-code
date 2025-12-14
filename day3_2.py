file= open("input_3.txt","r")
# file= open("tmp.txt","r") 

unparsed_content= file.read()

content= unparsed_content.split("\n")

highest_joltage= []

def findBiggest(seq,original):
    sequence1 = sorted([int(s) for s in list(seq)])

    highest_index= original.find(str(sequence1[-1]))


    highest_num= str(sequence1[-1])
    return highest_num,highest_index

for seq in content:
    biggest_index= 0
    joltage= []
    abs_index= len(seq)


    for i in range(11,-1,-1):
        seq= seq[biggest_index:]
        sliced_seq= seq[:-i] if i !=0 else seq
        big_num, big_i= findBiggest(sliced_seq,seq)
        joltage.append(big_num)
        biggest_index= big_i+1

    highest_joltage.append(int("".join(joltage)))



print(highest_joltage)
print(sum(highest_joltage))