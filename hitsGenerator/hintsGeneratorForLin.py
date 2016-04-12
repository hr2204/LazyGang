import re
import json

filePath = "Copy of Grade 7- Skill 10.3.txt"
data = ""

with open(filePath, 'r') as f:
    data = f.read()

regex_ae = "Assisted Exercise\)[\s\S].*?\(Assisted Exercise - Solution\)"

aeMatches = re.findall(regex_ae, data, re.S)

print "Get {0} AE".format(len(aeMatches))

aeHints = []
aeHintsLen = []
for ae in aeMatches:
    regex_exe_hints = "\(Assisted Exercise - Hints\).*?Tool Tip:"
    aeHintMatches = re.findall(regex_exe_hints, ae, re.S)
    aeHintsLen.append(len(aeHintMatches))
    aeHints.append(aeHintMatches[len(aeHintMatches) - 1])

for aeHint in aeHints:
    print aeHint

regex_exe = "Exercise #\d+\)[\s\S].*?\(Exercise #\d* - Solution\)"
exeMatches = re.findall(regex_exe, data, re.S)

print "Get {0} Exe".format(len(exeMatches))

exeHints = []
exeHintsLen = []
for exe in exeMatches:
    regex_exe_hints = "\(Exercise #\d+ - Hints\).*?Tool Tip:"
    exeHintMatches = re.findall(regex_exe_hints, exe, re.S)
    exeHintsLen.append(len(exeHintMatches))
    exeHints.append(exeHintMatches[len(exeHintMatches) - 1])

finalAEHints = []
for i in range(0, len(aeHints)):  # extHint in exeHints:
    aeHintList = exeHints[i].split("\n")
    aeAllHints = [x for x in aeHintList if x]   # remove all empty string
    finalAEHints.append(aeAllHints[-aeHintsLen[i] - 1:-1])   # put all exe hints in one array

print "AE hints--"
for test in finalAEHints:
    print test


# ------------get final Exercise Hints---------------------------
print "ExE hints------------"
finalExe = []
for i in range(0, len(exeHints)):  # extHint in exeHints:
    exHintList = exeHints[i].split("\n")
    exeAllHints = [x for x in exHintList if x]   # remove all empty string
    finalExe.append(exeAllHints[-exeHintsLen[i] - 1:-1])   # put all exe hints in one array

# important for Exercise Debug
for test in finalExe:
    print test


# prepare json data file

finalData = []
for i in range(0,len(finalAEHints)):
    for j in range(0,len(finalAEHints[i])):
        tempObj = {"hint_id": i+1, "row": [
            {
                "type": "mathtex_wrapper",
                "value": "", # $\\begin{array}{rl}" + finalExeLeft[i][j]  + " \\end{array}$",
                "show": False
            },
            {
                "type": "mathtex_wrapper",
                "value": finalAEHints[i][j]
            }
        ]}
        # tempObj["row"][1]["value"] = finalAE[i]
        finalData.append(tempObj)

exeIndex = len(aeHintsLen)
for i in range(0,len(finalExe)):
    for j in range(0,len(finalExe[i])):
        tempObj = {"hint_id": exeIndex+1, "row": [
            {
                "type": "mathtex_wrapper",
                "value": "", # $\\begin{array}{rl}" + finalExeLeft[i][j]  + " \\end{array}$",
                "show": False
            },
            {
                "type": "mathtex_wrapper",
                "value": finalExe[i][j]
            }
        ]}
        # tempObj["row"][1]["value"] = finalAE[i]
        finalData.append(tempObj)
        exeIndex += 1

#----------------output file-------------------------------
with open('linHints.json', 'w') as txtfile:
    json.dump(finalData,txtfile)
# for extHint in exeHints:
#     print extHint



