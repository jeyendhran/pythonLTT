readdata = [x.strip() for x in (l for l in open("line_text.txt"))]
splitdata = []
for i in readdata:
    print([i[start:start + 100] for start in range(0, len(i), 100)])
    splitdata.extend([i[start:start + 100] for start in range(0, len(i), 100)])

readdata = [" "*3+x.strip() for x in splitdata]
with open("new_text.txt","w") as f:
    f.write("\n".join(readdata))
