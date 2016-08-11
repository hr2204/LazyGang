import io
import re
import json
from G8IdReplace import do
from G8IdReplace import replaceID



skillNumber = "3.4"
offset = 0
# filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"

filePath = "/Users/rhe/Downloads/Algebra 1_ Skill "+ skillNumber + ".txt"
outputPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/9th/" + skillNumber +"/hints.json"

data = ""

with open(filePath, 'r') as f:
    data = f.read()

regex_exe = "Image \( Hint\)[\s\S].*?Tool Tip"
exeMatches = re.findall(regex_exe, data, re.S)

print "Get {0} Exe".format(len(exeMatches))

allHints = []
exeHintsLen = []
for hints in exeMatches:  # extHint in exeHints:
    exHintList = hints.split("\n")
    exeAllHints = [x for x in exHintList if x.strip()]
    allHints.append(exeAllHints[2 - offset:-1])
    exeHintsLen.append(len(exeAllHints[2 - offset:-1]))
    # print exeAllHints[2 - offset:-1]

# print allHints
for index, test in enumerate(allHints):
    print "Exe #{0} Hints".format(index+1), test


# # ----------------generate json-------------------------------
finalData = []
dataIndex = 1
# # -------b)-For Exercise--------------------------------------------
# # to do for exercise
#
for i in range(0, len(allHints)):
    for j in range(0, len(allHints[i])):
        temp = allHints[i][j].replace("\\\\","\\")
        tempObj = {
                "hint_id": dataIndex,
                "type": "mathtex_wrapper",
                "value": temp
            }
        finalData.append(tempObj)
        dataIndex += 1

# # ----------------output file-------------------------------
with open(outputPath, 'w') as txtfile:
    json.dump(finalData, txtfile)
    # for extHint in exeHints:
    #     print extHint

print exeHintsLen
#
replaceID(skillNumber,exeHintsLen,"singleColumn")
