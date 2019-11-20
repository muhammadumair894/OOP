
import  re
# get data file names
#path =r'C:\Users\muham\Desktop\AutoPhrase.text'
file = open("Complete_AutoPhrase.txt", 'w',encoding='UTF-8' )
newfile = open("AlNumRemove_AutoPhrase.txt", 'r', encoding="UTF-8")
newfile.readline()



for i in newfile:
    stripstr = i.strip()
    if(len(stripstr)==0):
        print("Empty field detected ")
    else:
        print("Data After Striping spaces = " + stripstr)
        v = stripstr
        s = v[:13]
        print("Data in S variable = "+s)
        Val = s[2:4]
        minVal = int (Val)
        #print("Data in minval variable = "+ minVal)
        sr = v[13:]
        print("Data in string variable = " + sr)
        c = (re.findall(r'[^\S]+', sr))
        print("White Exits OR NOT")
        print(c)
        print(len(c))
        length = len(c)
        if (length != 0):
            file.write(i.strip() + "\n")
        elif(minVal>=80):
            file.write(i.strip() + "\n")
    #print(sr)
    #x = re.findall("[0-9]", sr) #trim All numarics in the text



    """
    if (not x and not len(stripstr)==0 ):
        file.write(i.strip() + "\n")
        print("MultiWorld  "+i.strip())
    elif(x and int(minVal)>=80 and not len(stripstr)==0):
        print("SingleWorld " + i.strip())
        file.write(i.strip() + "\n")
    elif():
        print()
        """
newfile.close()
file.close()
