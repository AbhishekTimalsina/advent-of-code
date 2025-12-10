
file = open("input_2.txt","r")
# file = open("tmp.txt","r")

unparsed_content= file.read()

unparsed_content= unparsed_content.split(",")

content= []

patterns=[]

for r in unparsed_content:
    a,b = map(int,r.split("-"))
    content.append([a,b])


for a,b in content:

    for number in range(a,b+1):
        str_num= str(number)
        str_len= len(str_num)

        if str_num[0]=='0' or str_len==3:
            continue

        if str_len%2==0:
            mid_point= str_len//2

            first_half= str_num[:mid_point]
            second_half= str_num[mid_point:]

            if first_half==second_half:
                patterns.append(str_num)
            
        # else:
        #     is_pattern=  len(set(str_num))==1

        #     if is_pattern:
        #         patterns.append(str_num) 



patterns= list(map(int, patterns))

print(sum(patterns))

# print(patterns)