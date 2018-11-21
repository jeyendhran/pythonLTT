f = open("line_text.txt")
readdata = list(map(lambda x: x.strip(),f.readlines()))
f.close()
splitdata = []
for i in readdata:
    splitdata.extend([i[start:start + 150] for start in range(0, len(i), 150)])
readdata = list(map(lambda x: "  "+x,splitdata))


f = open("new_text.txt","w")
f.write("\n".join(readdata))
f.close()
