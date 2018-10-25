def read_file(filename):
    f = open(filename)
    cnt = list(map(lambda x: x.strip().split(','), f.readlines()))

    cnt = list(map(lambda x: (x[0], x[1]), cnt))

    #cnt = set(map(lambda x: (x[0], x[1]), cnt))

    f.close()
    return cnt

original_file = "model.csv"
input_file = "answers.csv"
original_ans = read_file(original_file)
print(original_ans)
input_ans = read_file(input_file)
print(input_ans)

ans = list(map(lambda x,y:1 if x==y else (0 if x[1]=='x' else -1),input_ans,original_ans))
print("Total marks is",sum(ans),ans)

#print(len(input_ans.intersection(original_ans)))
#print("Total Marks is",len(list(filter(lambda x:1 if x==1 else 0,ans))))

