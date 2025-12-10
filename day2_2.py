
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
        str_len = len(str_num)



        if str_num[0]=='0' or str_len==1:
            continue

        
        if len(set(str_num))==1:
            patterns.append(str_num)
            continue

        valid_divider=[]

        for i in range(2,(str_len//2)+1):
            if str_len%i==0:
                valid_divider.append(i)



        for n in valid_divider:
            chunks= [str_num[i:i+n] for i in range(0,str_len,n)]
            is_pattern= len(set(chunks))==1


            if is_pattern:
                patterns.append(str_num)
                break



patterns= list(map(int, patterns))

print(sum(patterns))

# print(patterns)

