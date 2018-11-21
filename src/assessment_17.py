f = open("para.txt")
readdata = f.readlines()
readdata = (para for para in list(filter(lambda x: x != "\n" ,readdata)))
para = 0
for i in readdata:
    print(i)
    para += 1

s = "The\tno of paragraphs in the file is".expandtabs(10)
print(s)