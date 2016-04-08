import io
import re
import json


#filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"

filePath = "/Users/rhe/Downloads/Grade 7_ Skill 12.5.txt"
data = ""

with open(filePath, 'r') as f:
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
    aeHints.append(aeHintMatches[len(aeHintMatches)-1])


#------------get final Assisted Exercise Hints---------------------------
finalAERight = []
finalAELeft = []
for i in range(0,len(aeHintsLen)): #extHint in exeHints:
    aeHintList = aeHints[i].split("\n")
    aeAllHints = [x for x in aeHintList if x]
    finalAERight.append(aeAllHints[-aeHintsLen[i]-1:-1])
    finalAELeft.append( aeAllHints[4:4+aeHintsLen[i]])


# important for AE Debug
for test in finalAERight:
    print test


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


#----------------generate json-------------------------------
#-------a)-For AE--------------------------------------------
finalData = []
dataIndex = 1
for i in range(0,len(finalAERight)):
    for j in range(0,len(finalAERight[i])):
        tempObj = {"hint_id": dataIndex, "row": [
            {
                "type": "mathtex_wrapper",
                "value": " $\\begin{array}{rl}" + finalAELeft[i][j] + " \\end{array}$",
                "show": False
            },
            {
                "type": "mathtex_wrapper",
                "value": finalAERight[i][j]
            }
        ]}
        finalData.append(tempObj)
        dataIndex += 1

# -------b)-For Exercise--------------------------------------------
# to do for exercise

for i in range(0,len(finalExeRight)):
    for j in range(0,len(finalExeRight[i])):
        tempObj = {"hint_id": dataIndex, "row": [
            {
                "type": "mathtex_wrapper",
                "value": " $\\begin{array}{rl}"    + " \\end{array}$",
                "show": False
            },
            {
                "type": "mathtex_wrapper",
                "value": finalExeRight[i][j]
            }
        ]}
        finalData.append(tempObj)
        dataIndex += 1

#----------------output file-------------------------------
with open('output.json', 'w') as txtfile:
    json.dump(finalData,txtfile)
# for extHint in exeHints:
#     print extHint


