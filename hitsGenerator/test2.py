import io
import re
import json


#filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"

filePath = "/Users/rhe/Desktop/Grade 7_ Skill 11.9.txt"
data = ""

with open(filePath, 'r') as f:
    data= f.read()

# regex_ae = "\(Assisted Exercise [#\d]+ - Hints\).*?Tool Tip:"

regex_ae = "\(Assisted Exercise - Hints\).*?Tool Tip:"

matchStrings = re.findall(regex_ae, data, re.S)

print "Get {0} AE hints".format(len(matchStrings))

# for string in matchStrings:
#    print string
aeHint = matchStrings[len(matchStrings) - 1]

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











#----------------generate json-------------------------------
#-------a)-For AE--------------------------------------------
finalData = []
for i in range(0,len(finalAE)):
    tempObj = {"hint_id": i+1, "row": [
        {
            "type": "mathtex_wrapper",
            "value": " $\\begin{array}{rl}" + finalAELeft[i] + " \\end{array}$",
            "show": False
        },
        {
            "type": "mathtex_wrapper",
            "value": finalAE[i]
        }
    ]}
    # tempObj["row"][1]["value"] = finalAE[i]
    finalData.append(tempObj)
#-------b)-For Exercise--------------------------------------------
#to do for exercise
exeIndex = len(matchStrings)
for i in range(0,len(finalExeRight)):
    for j in range(0,len(finalExeRight[i])):
        tempObj = {"hint_id": exeIndex+1, "row": [
            {
                "type": "mathtex_wrapper",
                "value": " $\\begin{array}{rl}" + finalExeLeft[i][j]  + " \\end{array}$",
                "show": False
            },
            {
                "type": "mathtex_wrapper",
                "value": finalExeRight[i][j]
            }
        ]}
        # tempObj["row"][1]["value"] = finalAE[i]
        finalData.append(tempObj)
        exeIndex += 1

#----------------output file-------------------------------
with open('output.json', 'w') as txtfile:
    json.dump(finalData,txtfile)
# for extHint in exeHints:
#     print extHint