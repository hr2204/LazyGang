import io
import re
import json


#filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"

filePath = "/Users/rhe/Downloads/Grade 7_ Skill 13.1.txt"
data = ""

with open(filePath, 'r') as f:
    data= f.read()

# regex_ae = "\(Assisted Exercise [#\d]+ - Hints\).*?Tool Tip:"

regex_ae = "\(Assisted Exercise - Hints\).*?Tool Tip:"

matchStrings = re.findall(regex_ae, data, re.S)

print "Get {0} AE hints".format(len(matchStrings))

# for string in matchStrings:
#    print string
if(len(matchStrings)!=0):
    aeHint = matchStrings[len(matchStrings) - 1]
else:
    aeHint = []


regex_exe = "Exercise #\d+\)[\s\S].*?\(Exercise #\d* - Solution\)"
exeMatches = re.findall(regex_exe, data, re.S)

print "Get {0} Exe".format(len(exeMatches))

exeHints = []
exeHintsLen = []
for exe in exeMatches:
    regex_exe_hints = "\(Exercise #\d+ - Hints\).*?Tool Tip:"
    exeHintMatches = re.findall(regex_exe_hints, exe, re.S)
    exeHintsLen.append(len(exeHintMatches))
    exeHints.append(exeHintMatches[len(exeHintMatches)-1])



#------------get final Exercise Hints---------------------------
finalExeRight = []
finalExeLeft = []
for i in range(0,len(exeHints)): #extHint in exeHints:
    exHintList = exeHints[i].split("\n")
    exeAllHints = [x for x in exHintList if x]
    finalExeRight.append(exeAllHints[-exeHintsLen[i]-1:-1])
    finalExeLeft.append( exeAllHints[4:4+exeHintsLen[i]])
# important for Exercise Debug
for test in finalExeRight:
    print test


# print "Exercise Hint length:"
# print exeHintsLen
# print aeHint
#------------get final AE Hints---------------------------
aehintList = aeHint.split("\n")
aeAllHints = [x for x in aehintList if x]
# print -len(matchStrings)
finalAE  = aeAllHints[-len(matchStrings)-1:-1]
finalAELeft = aeAllHints[4:4+len(matchStrings)]


# print exeHints
# print "matchStrings=" + str(len(matchStrings))
# print aeHint









# ----------------generate json-------------------------------
# -------a)-For AE--------------------------------------------
finalData = []
dataIndex = 1
for i in range(0, len(finalAE)):
        tempObj =\
        {
            "hint_id": dataIndex,
            "type": "mathtex_wrapper",
            "value": finalAE[i]
        }
        finalData.append(tempObj)
        dataIndex += 1
print "***final json:***",finalData
# # -------b)-For Exercise--------------------------------------------
# # to do for exercise
#
for i in range(0, len(finalExeRight)):
    for j in range(0, len(finalExeRight[i])):
        tempObj = {
                "hint_id": dataIndex,
                "type": "mathtex_wrapper",
                "value": finalExeRight[i][j]
            }
        finalData.append(tempObj)
        dataIndex += 1

# # ----------------output file-------------------------------
with open('output.json', 'w') as txtfile:
    json.dump(finalData, txtfile)
    # for extHint in exeHints:
    #     print extHint
