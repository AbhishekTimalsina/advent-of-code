file= open("input_4.txt","r")
# file= open("tmp.txt","r")

unparsed_content= file.read()

content= unparsed_content.split("\n")

valid_positions= [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]

new_positions= [row[:] for row in content]


is_valid_present= True

total_valid=0


while(is_valid_present):
    valid_paper_rolls= 0
    for y in range(0,len(new_positions)):
        data = new_positions[y]
        for x in range(0, len(data)):
            count=0


            if data[x]==".":
                continue

            for py,px in valid_positions:

                curPosX = x+px
                curPosY = y+py



                if curPosX<0 or curPosY<0:
                    continue

                
                if curPosX>=len(data) or curPosY>=len(new_positions):
                    continue


                # print( curPosY,curPosX,"py:",py,"px:",px,content[curPosY][curPosX])
                if (new_positions[curPosY][curPosX]) =="@":
                    count+=1



            if count<4:
                tmpList= list(new_positions[y])
                tmpList[x]="."


                new_positions[y]="".join(tmpList) 
                valid_paper_rolls+= 1

                    
    if valid_paper_rolls==0:
        is_valid_present=False
    else:
        total_valid+=valid_paper_rolls
        valid_paper_rolls=0


print(total_valid)