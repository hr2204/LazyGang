import re
import json
import LoadJsonData


#filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"
jsonLoader = LoadJsonData.LoadJson()
problemFilePath = "/Users/rhe/Desktop/forId/skill_problem.json"

jsonObjs = jsonLoader.readJson(problemFilePath)
# d = json.loads(jsonObjs)

print type(jsonObjs)
with open(problemFilePath, 'r') as f:
    data = f.read()

# print data

str1 = "hintIds"
regex_hintId = "\"hintIds\": [.*]"

print  [i for i in range(len(data)) if data.startswith(str1, i)]
print  [i for i in range(len(data)) if data.startswith("specified_tim", i)]
print data[351:393]
temp = data[351:393]
data.replace(data[351:393],"aaa")
print data

#------------------------------------------------------------
filePath = "/Users/rhe/Desktop/Grade 7_ Skill 12.4.txt"
def getIDList( path ):
    data = ""
    with open(path, 'r') as f:
        data= f.read()


    regex_ae = "Assisted Exercise #\d+\)[\s\S].*?\(Assisted Exercise #\d* - Solution\)"

    aeMatches = re.findall(regex_ae, data, re.S)

    print "Get {0} AE".format(len(aeMatches))
    aeHints = []
    aeHintsLen = []
    for ae in aeMatches:
        regex_exe_hints = "\(Assisted Exercise #\d+ - Hints\).*?Tool Tip:"
        aeHintMatches = re.findall(regex_exe_hints, ae, re.S)
        aeHintsLen.append(len(aeHintMatches))



    regex_exe = "Exercise #\d+\)[\s\S].*?\(Exercise #\d* - Solution\)"
    exeMatches = re.findall(regex_exe, data, re.S)

    print "Get {0} Exe".format(len(exeMatches))

    exeHints = []
    exeHintsLen = []
    for exe in exeMatches:
        regex_exe_hints = "\(Exercise #\d+ - Hints\).*?Tool Tip:"
        exeHintMatches = re.findall(regex_exe_hints, exe, re.S)
        exeHintsLen.append(len(exeHintMatches))

    print aeHintsLen
    print exeHintsLen
    totalLen = aeHintsLen + exeHintsLen
    print sum(totalLen)
    hintIds = []
    allIds = range(1,sum(totalLen))
    start = 1
    for i in totalLen:
        temp = range(start,start+i)
        start += i
        hintIds.append(temp)

    return hintIds

hintIds = getIDList(filePath)





#-----------output---skill.json
for i in range(len(jsonObjs)):
    jsonObjs[i]["hintIds"] = hintIds[i]



with open('output.json', 'w') as txtfile:
    json.dump(jsonObjs,txtfile)
