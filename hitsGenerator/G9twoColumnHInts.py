"""
Test
"""
import re
import json
from G8IdReplace import replaceID

skillNumber = "7.7"
# offsetLeft = 2
# offsetRight = 2

filePath = "/Users/rhe/Downloads/Algebra 1_ Skill " + skillNumber + ".txt"
outputPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/9th/" + skillNumber + "/hints.json"
data = ""

with open(filePath, 'r') as f:
    data = f.read()

regex_exe = r"Image \( Hint\)[\s\S].*?Tool Tip"
exeMatches = re.findall(regex_exe, data, re.S)

print "Get {0} Exe".format(len(exeMatches))


def goupHints(hintList):
    groupedHints = []
    blankIndexes = [i for i, x in enumerate(hintList) if x == '']
    # print blankIndexes

    idx = 0
    while idx < len(blankIndexes) - 1:
        start = blankIndexes[idx]
        end = blankIndexes[idx + 1]
        if idx == 0:
            firstBlank = blankIndexes[0]
            lastBlank = blankIndexes[-1]
        if end - start > 1:
            hintList[start:end] = [''.join(hintList[start:end])]
            blankIndexes = [index - (end - start - 1) for index in blankIndexes]
            lastBlank = blankIndexes[-1]

        idx += 1
    if idx != 0:
        hintList[lastBlank + 1:] = [''.join(hintList[lastBlank + 1:])]
        hintList[0:firstBlank] = [''.join(hintList[0:firstBlank])]

    groupedHints = [x for x in hintList if x.strip()]
    return groupedHints


finalExeRight = []
finalExeLeft = []
exeHintsLen = []
for hints in exeMatches:
    exHintList = hints.split("\n")
    exeAllHints = [x for x in exHintList if x.strip()]
    # exeAllHints = [x for x in exeAllHints if x.rstrip()]
    # Right Column
    exeAllHints = exeAllHints[3:-1]
    tempMiddle = [s for s in exeAllHints if "\\\\end{array}" in s][0]
    middelInx = exeAllHints.index(tempMiddle)

    rightHints = exeAllHints[middelInx + 1:]
    finalExeRight.append(rightHints)
    exeHintsLen.append(len(rightHints))
    # Left Column
    middelInx_left = exHintList.index(tempMiddle)
    leftHints = exHintList[3:middelInx_left]
    # print leftHints
    leftHints = goupHints(leftHints)
    finalExeLeft.append(leftHints)

    print "Exe #{0} right Hints (".format(exeMatches.index(hints) + 1), len(rightHints), ")", rightHints

print "===================================="
for x in finalExeLeft:
    print "Exe #{0} left Hints (".format(finalExeLeft.index(x) + 1), len(x), ")", x

# ----------------generate json-------------------------------
# -------a)-For AE--------------------------------------------
finalData = []
dataIndex = 1

for i in range(0, len(finalExeRight)):
    for j in range(0, len(finalExeRight[i])):
        tempLeft = finalExeLeft[i][j].replace("\\\\", "\\")
        tempRight = finalExeRight[i][j].replace("\\\\", "\\")
        tempLeft = tempLeft.replace("skip", "")

        tempObj = {"hint_id": dataIndex, "row": [
            {
                "type": "img",
                "value": "7.7/math-g9-c7-s7-7-p"+str(i) + "-h"+str(j+1) +"-img1.png"
            },
            {
                "type": "mathtex_wrapper",
                "value": " $\\begin{array}{rl} " + tempLeft + " \\end{array}$"
            },
            {
                "type": "mathtex_wrapper",
                "value": tempRight
            }
        ]}
        finalData.append(tempObj)
        dataIndex += 1

# ----------------output file-------------------------------
with open(outputPath, 'w') as txtfile:
    json.dump(finalData, txtfile)

replaceID(skillNumber, exeHintsLen, "twoColumn")
