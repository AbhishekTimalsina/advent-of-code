file= open("input_4.txt","r")

unparsed_content= file.read()

content= unparsed_content.split("\n")

valid_positions= [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]

valid_paper_rolls= 0


for y in range(0,len(content)):
    data = content[y]
    for x in range(0, len(data)):


        count=0


        if data[x]==".":
            continue

        for py,px in valid_positions:

            curPosX = x+px
            curPosY = y+py



            if curPosX<0 or curPosY<0:
                continue

            
            if curPosX>=len(data) or curPosY>=len(content):
                continue


            # print( curPosY,curPosX,"py:",py,"px:",px,content[curPosY][curPosX])
            if (content[curPosY][curPosX]) =="@":
                count+=1

    

        if count<4:
            valid_paper_rolls+= 1


print(valid_paper_rolls)