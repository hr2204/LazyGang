"""
Test
"""
import re
import json
from G8IdReplace import replaceID

skillNumber = "10.7"
keyword = "Identifying"
offsetLeft = 2
offsetRight = 2

filePath = "/Users/rhe/Downloads/Grade 8_.Skill " + skillNumber + ".txt"
outputPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/8th/" + skillNumber + "/hints.json"

# filePath = "/Users/rhe/Downloads/Grade 7_ Skill 12.5.txt"
data = ""

with open(filePath, 'r') as f:
    data = f.read()

regex_ae = r"Assisted Exercise[ #\d+]*?\)[\s\S]*?\(Assisted Exercise[ #\d*]? - Solution\)"

aeMatches = re.findall(regex_ae, data, re.S)

print "Get {0} AE".format(len(aeMatches))
aeHints = []
aeHintsLen = []
for ae in aeMatches:
    # regex_exe_hints = "\(Assisted Exercise #\d+ - Hints\).*?Tool Tip:"
    regex_exe_hints = r"Text.*?\d+\.\d+ " + keyword

    aeHintMatches = re.findall(regex_exe_hints, ae, re.S)
    aeHintsLen.append(len(aeHintMatches))
    aeHints.append(aeHintMatches[len(aeHintMatches) - 1])

# ------------get final Assisted Exercise Hints---------------------------
finalAERight = []
finalAELeft = []
for i in range(0, len(aeHintsLen)):  # extHint in exeHints:
    aeHintList = aeHints[i].split("\n")
    aeAllHints = [x for x in aeHintList if x]
    finalAERight.append(aeAllHints[-aeHintsLen[i] - offsetRight:-offsetRight])
    finalAELeft.append(aeAllHints[offsetLeft:offsetLeft + aeHintsLen[i]])

# important for AE Debug
for test in finalAERight:
    print test

regex_exe = r"Exercise #\d+\)[\s\S].*?Exercise #\d* - Solution\)"
exeMatches = re.findall(regex_exe, data, re.S)

print "Get {0} Exe".format(len(exeMatches))
# for x in exeMatches:
#     print x

exeHints = []
exeHintsLen = []
for exe in exeMatches:
    regex_exe_hints = r"Text.*?\d+\.\d+ " + keyword
    exeHintMatches = re.findall(regex_exe_hints, exe, re.S)
    exeHintsLen.append(len(exeHintMatches))
    if len(exeHintMatches) != 0:
        exeHints.append(exeHintMatches[len(exeHintMatches) - 1])

print aeHintsLen + exeHintsLen
# ------------get final Exercise Hints---------------------------
finalExeRight = []
finalExeLeft = []
for i in range(0, len(exeHints)):  # extHint in exeHints:
    exHintList = exeHints[i].split("\n")
    exeAllHints = [x for x in exHintList if x]
    finalExeRight.append(exeAllHints[-exeHintsLen[i] - offsetRight:-offsetRight])
    finalExeLeft.append(exeAllHints[offsetLeft:offsetLeft + exeHintsLen[i]])
index_show = 1
# important for Exercise Debug
for test in finalExeLeft:
    # print "Exercise #" + finalExeLeft.index(test) + ":"
    print "Exercise #" + str(index_show) + str(test)
    index_show += 1

# for test in finalExeRight:
#     print test

# ----------------generate json-------------------------------
# -------a)-For AE--------------------------------------------
finalData = []
dataIndex = 1
# finalData = simpleVersion.generateJson(finalAELeft,finalAERight,1, finalData)
# print finalData

for i in range(0, len(finalAERight)):
    for j in range(0, len(finalAERight[i])):
        tempLeft = finalAELeft[i][j].replace("\\\\", "\\")
        tempRight = finalAERight[i][j].replace("\\\\", "\\")
        tempObj = {"hint_id": dataIndex, "row": [
            {
            },
            {
                "type": "mathtex_wrapper",
                "value": tempRight
            }
        ]}
        if j == 1 or j == 2:
            tempObj["row"][0] = {
                    "type": "img",
                    "value": "9.4/math-g8-c11-12-ap" + str(i + 1) + "-h" + str(1) + "-img1.png",
                }
        else:
            tempObj["row"][0] = {
                    "type": "mathtex_wrapper",
                    "value": " "
                }
        finalData.append(tempObj)
        dataIndex += 1

# -------b)-For Exercise--------------------------------------------
# to do for exercise

for i in range(0, len(finalExeRight)):
    for j in range(0, len(finalExeRight[i])):
        tempLeft = finalExeLeft[i][j].replace("\\\\", "\\")
        tempRight = finalExeRight[i][j].replace("\\\\", "\\")

        tempObj = {"hint_id": dataIndex, "row": [
            {
            },
            {
                "type": "mathtex_wrapper",
                "value": tempRight
            }
        ]}
        if j == 1 or j == 2:
            tempObj["row"][0] = {
                    "type": "img",
                    "value": "11.13/math-g8-c11-s12-p" + str(i + 1) + "-h" + str(j+1) + "-img1.png",
                }
        else:
            tempObj["row"][0] = {
                    "type": "mathtex_wrapper",
                    "value": " "
                }
        finalData.append(tempObj)
        dataIndex += 1

# ----------------output file-------------------------------
with open(outputPath, 'w') as txtfile:
    json.dump(finalData, txtfile)
# for extHint in exeHints:
#     print extHint


replaceID(skillNumber, aeHintsLen + exeHintsLen, "two_columns_hint_a")
