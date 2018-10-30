import json

with open("sample_json.json","r") as jsondata:
    jsoncontent = json.load(jsondata)
print(jsoncontent)

mydata ={ "color":"light green","value":"dsgsdg" },{ "color":"light yellow","value":"ddgsg" }
with open("sample_json.json","a") as jsondata:
    json.dump(mydata,jsondata)