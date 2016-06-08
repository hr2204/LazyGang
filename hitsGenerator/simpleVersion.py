import io
import re
import json



#filePath = "/Users/hhuang/Desktop/Grade 7- Skill 14.6.txt"

filePath = "/Users/rhe/Downloads/Grade 7-.Skill 3.10 - UPDATED 3-12-16.txt"
data = ""

with open(filePath, 'r') as f:
    data= f.read()




regex_hints = "Text.*?Tool Tip:"
regex_len = "Image.*?Hint"
# regex_exe_hints = "\(Exercise #\d+ - Hints\).*?Tool Tip:"

hintsMatches = re.findall(regex_hints, data, re.S)
hintlen = re.findall(regex_len, data, re.S)

hints = []
hintsLen = []
for exe in hintsMatches:
    print exe
# print len(hintsLen)
for x in hintlen:
    hintsLen.append(int(x[7]))


print hintsLen
hintsLen = [6, 7, 7, 5, 6, 7, 7, 7, 8, 6]
#------------get final Exercise Hints---------------------------
finalExeRight = []
finalExeLeft = []
for i in range(0,len(hintsLen)): #extHint in exeHints:
    exHintList = hintsMatches[i].split("\n")
    exeAllHints = [x for x in exHintList if x]
    finalExeRight.append(exeAllHints[-hintsLen[i]-1:-1])
    finalExeLeft.append(exeAllHints[1:hintsLen[i]+1])



print "left----------------------"
for hint in finalExeLeft:
    print hint

print "right----------------------"
for hint in finalExeRight:
    print hint


finalData = []


def generateJson(finalExeLeft, finalExeRight, starIndex, finalData):
    for i in range(0,len(finalExeRight)):
        for j in range(0,len(finalExeRight[i])):
            tempObj = {"hint_id": starIndex, "row": [
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
            finalData.append(tempObj)
            starIndex += 1
    return finalData

finalData = generateJson(finalExeLeft,finalExeRight,1,finalData)


#----------------output file-------------------------------
with open('output.json', 'w') as txtfile:
    json.dump(finalData,txtfile)
# for extHint in exeHints:
