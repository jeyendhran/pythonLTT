
def checkPalindrome(string):
    # Way 1
    # l = lambda x:x.replace(" ","").lower()
    # string = l(string)
    # l = lambda x:x.replace(",","")
    # palinstr = l(string)

    # Way 2
    # palinstr = string.replace(" ","").replace(",","").replace(";","").lower()

    # Way 3
    palinstr = "".join(list(filter(lambda x:x.isalpha(),list(string)))).lower()

    # Way 4
    import re
    pattern = re.compile('[a-z]')
    palinstr = pattern.findall(string.lower())

    if palinstr == palinstr[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"


def revWords(string):
    # Way 1
    # import re
    # print(re.split("\W+",string)[::-1])
    # Way 2
    palinstr = "".join(list(filter(lambda x: x.isalpha() if x!=" " else x, list(string))))
    print(palinstr.split(" ")[::-1])

    revStr = []
    for i in string.split(" "):
        if i.isalpha():
            revStr.append(i[::-1])
        else:
            l = list(i[::-1])
            l.append(l.pop(0))
            revStr.append("".join(l))
    print(" ".join(revStr))



print("The input string is",checkPalindrome("A man, a plan, a canal; panama"))
print("The input string is",checkPalindrome("madam"))
print("The input string is",checkPalindrome("madama"))
revWords("A man, a plan, a canal; panama")


