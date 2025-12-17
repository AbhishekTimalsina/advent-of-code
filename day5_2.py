# file= open("tmp.txt","r")
file= open("input_5.txt","r")

unparsed_content= file.read()


unparsed_content= unparsed_content.split("\n\n")


unparsed_ranges= unparsed_content[0].splitlines()
ids = unparsed_content[1].splitlines()

ranges=[]

for r in unparsed_ranges:
    a, b = r.split("-")
    ranges.append((int(a), int(b)))


ranges.sort()

total= 0

cur_start, cur_end= ranges[0]

for start,end in ranges[1:]:
    if start<=cur_end+1:
        cur_end= max(cur_end,end)

    else:
        total+=cur_end-cur_start+1
        cur_start,cur_end= start,end

total += cur_end - cur_start + 1

print(total)

