import re

#----------------Usage-----------------------------------
#  1) Ipnut txtPath from slides
#  2) Choose number of AE
#  3) Run and check your result
#----------------input--Here---------------------------------


txtPath = "/Users/rhe/Downloads/Grade 7_ Skill 13.4.txt"

numberOfAE = 2

#------------------init path-----------------------------------------

regex_txtPath = "\d+\.\d+"
fileName = re.search(regex_txtPath, txtPath, re.S)
skillNumber = fileName.group(0)
# fileName = txtPath.split()
# skillNumber = fileName[-1].strip(".txt")
# print "----------", skillNumber
print "----------"+fileName.group(0)

projectPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/7th/"
skillPath = projectPath + skillNumber + "/skill_problem.json"
print skillPath
#----------------get IDs from .txt-----------------------------------

index = 0
def do(m):
    global index
    text = "\"hintIds\": {0}".format(values[index])
    index = index + 1
    return text

def getIDListTwoAE( path ):
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


def getIDListOneAE( path ):
    data = ""
    with open(path, 'r') as f:
        data= f.read()


    regex_ae = "\(Assisted Exercise - Hints\).*?Tool Tip:"

    matchStrings = re.findall(regex_ae, data, re.S)

    print "Get {0} AE hints".format(len(matchStrings))

    # for string in matchStrings:
    #    print string
    aeLen = len(matchStrings)
    aeHintsLen =[]
    aeHintsLen.append(aeLen)
    regex_exe = "Exercise #\d+\)[\s\S].*?\(Exercise #\d* - Solution\)"
    exeMatches = re.findall(regex_exe, data, re.S)

    print "Get {0} Exe".format(len(exeMatches))

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
    start = 1
    for i in totalLen:
        temp = range(start,start+i)
        start += i
        hintIds.append(temp)

    return hintIds



if(numberOfAE == 1):
    values = getIDListOneAE(txtPath)
else:
    values = getIDListTwoAE(txtPath)

print values

# filePath = "sample.json"
data = ""
with open(skillPath, 'r') as f:
    data = f.read()



# regex_hint_id = "(\"hintIds\":\s+\[)(.*?)(\])"
regex_hint_id = "\"hintIds\":\s+\[.*?\]"
text = re.sub(regex_hint_id, do, data, 0, re.S)

# print text


with open(skillPath, 'w') as txtfile:
    txtfile.write(text)





# hintsMatches = re.findall(regex_hint_id, data, re.S)
# print "-- Get {0} hints ----".format(len(hintsMatches))
#
# for hint in hintsMatches:
#     print hint

# text = re.sub(regex_hint_id, lambda x: values[x.group()], data)




