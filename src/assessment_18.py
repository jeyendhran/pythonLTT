def unexpandtab(string):
    newstring = string.replace("  ","\t")
    newstring = list(newstring)
    for i in range(0,len(newstring)-1):
        if newstring[i] == "\t" and newstring[i+1] == " ":
            newstring[i+1] = "\t"
    return "".join(newstring)

string = "This\tis a\tbig string\twith tabs"
print(string.expandtabs(20))
string = "This    is   a string    with tabs"
print(unexpandtab(string))
