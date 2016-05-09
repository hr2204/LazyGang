import io
import re
import json
from G8IdReplace import do
from G8IdReplace import replaceID



skillNumber = "4.5"
keyword = "Comparing"

# filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"

filePath = "/Users/rhe/Downloads/Grade 8_ Skill 4.5.txt"
data = ""

with open(filePath, 'r') as f:
    data = f.read()

regex_ae = "Assisted Exercise #\d+\)[\s\S].*?\(Assisted Exercise #\d* - Solution\)"


aeMatches = re.findall(regex_ae, data, re.S)

print "Get {0} AE".format(len(aeMatches))
aeHints = []
aeHintsLen = []
for ae in aeMatches:
    # regex_exe_hints = "\(Assisted Exercise #\d+ - Hints\).*?Tool Tip:"
    regex_exe_hints = "Text.*?\d+\.\d+ " + keyword

    aeHintMatches = re.findall(regex_exe_hints, ae, re.S)
    aeHintsLen.append(len(aeHintMatches))
    if len(aeHintMatches)!= 0:
        aeHints.append(aeHintMatches[len(aeHintMatches) - 1])
print aeHintsLen


# ------------get final Assisted Exercise Hints---------------------------
finalAE = []
for i in range(0, len(aeHintsLen)):  # extHint in exeHints:
    aeHintList = aeHints[i].split("\n")
    aeAllHints = [x for x in aeHintList if x]
    finalAE.append(aeAllHints[-aeHintsLen[i] - 1:-1])
    # finalAE.append(aeAllHints[3:3 + aeHintsLen[i]])


# important for AE Debug
for test in finalAE:
    print test

regex_exe = "\(Exercise #\d+\)[\s\S].*?\(Exercise #\d* - Solution\)"
exeMatches = re.findall(regex_exe, data, re.S)

print "Get {0} Exe".format(len(exeMatches))

exeHints = []
exeHintsLen = []

for exe in exeMatches:
    regex_exe_hints = "Text.*?\d+\.\d+ " + keyword
    exeHintMatches = re.findall(regex_exe_hints, exe, re.S)
    exeHintsLen.append(len(exeHintMatches))
    if len(exeHintMatches)!=0:
        exeHints.append(exeHintMatches[len(exeHintMatches) - 1])

print exeHintsLen

# ------------get final Exercise Hints---------------------------
finalExe = []
for i in range(0, len(exeHints)):  # extHint in exeHints:
    exHintList = exeHints[i].split("\n")
    exeAllHints = [x for x in exHintList if x]
    finalExe.append(exeAllHints[-exeHintsLen[i] - 1:-1])

# important for Exercise Debug
for test in finalExe:
    print test


# ----------------generate json-------------------------------
# -------a)-For AE--------------------------------------------
finalData = []
dataIndex = 1
for i in range(0, len(finalAE)):
    for j in range(0, len(finalAE[i])):
        tempObj =\
        {
            "hint_id": dataIndex,
            "type": "mathtex_wrapper",
            "value": finalAE[i][j]
        }
        finalData.append(tempObj)
        dataIndex += 1
# # -------b)-For Exercise--------------------------------------------
# # to do for exercise
#
for i in range(0, len(finalExe)):
    for j in range(0, len(finalExe[i])):
        temp = finalExe[i][j].replace("\\\\","\\")
        tempObj = {
                "hint_id": dataIndex,
                "type": "mathtex_wrapper",
                "value": temp
            }
        finalData.append(tempObj)
        dataIndex += 1

# # ----------------output file-------------------------------
with open('output.json', 'w') as txtfile:
    json.dump(finalData, txtfile)
    # for extHint in exeHints:
    #     print extHint

finalList = aeHintsLen + exeHintsLen
print aeHintsLen + exeHintsLen
totalLen = aeHintsLen + exeHintsLen

replaceID(skillNumber,totalLen,"singleColumn")
