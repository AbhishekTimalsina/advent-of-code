# file= open("tmp.txt","r")
file= open("input_5.txt","r")

unparsed_content= file.read()


unparsed_content= unparsed_content.split("\n\n")


ranges= unparsed_content[0].splitlines()
ids = unparsed_content[1].splitlines()


fresh_id_count= 0


for i in ids:
    for r in ranges:
        i= int(i)
        l,u= [int(i) for i in r.split("-")]

        if i >=l and i <=u:
            fresh_id_count+=1
            break

print(fresh_id_count)