import re
from problemLib import generateProblem
from problemLib import getMathtex
import os.path

skillNum = "10.18"

filePath = "/Users/rhe/Downloads/Algebra 1_. Skill " + skillNum + ".txt"
if not os.path.exists(filePath):
    filePath = "/Users/rhe/Downloads/Algebra 1_.Skill " + skillNum + ".txt"

templatePath = "/Users/rhe/Documents/Test/LazyGang/problemTest/template3.json"
outputPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/9th/" + skillNum + "/skill_problem.json"

# open text file and
with open(filePath, 'r') as f:
    text = f.read()

regex_toopTips = "Tool Tip:(.*?\.)"

toolFind = re.search(regex_toopTips, text)
toolTip = toolFind.group(1).strip()
# print toolTip


# exact solution slide
regex_solution = r"Exercise[ #\d+]*? - Solution\).*?Tool Tip:"
allSolution = re.findall(regex_solution, text, re.S)

debug = False
dropdown = False
inputBox = False
Mathtex = True
checkBox = False
getAnswerOptionIndex = False
byLocation = False
locationArr = [1,2,3,4,5,6,7,10,12,14,16,18]

images = False
# for final output
regex = "input\n.*?\\n"


def getDropDown(solutionSlide):
    regex_dropDown = " Dropdown.*?\]"
    temp = re.findall(regex_dropDown, solutionSlide, re.S)
    # print temp
    AllRes = []
    for i in range(0, len(temp)):
        temp[i] = temp[i].replace("\n", "")
        temp[i] = temp[i].replace("Dropdown", "").strip()
        temp[i] = temp[i].replace("R2C1", "").strip()

        tempResult = temp[i].split("[")
        tempResult[1] = "[" + tempResult[1]
        tempResult[1] = tempResult[1][1:-1]
        tempResult[1] = tempResult[1].split(",")
        result = {
            "type": "dropdown",
            "value": "",
            "answer": tempResult[0],
            "options":  tempResult[1]
        }
        # res = str(result)
        AllRes.append(str(result).replace( "'",'"'))
        # .replace( "'",'"')
    # print AllRes
    return AllRes


def getAnswerIndex(solutionSlide):
    solutionContent = solutionSlide.split("\n")
    solutionInfo = [x for x in solutionContent if x.strip()]
    answers = []
    for answer in solutionInfo:
        if answer == 'true' or answer == 'false':
            answers.append(answer)
    return answers.index("true") + 1

def getInput(solutionSlide, regex):
    temp = re.findall(regex, solutionSlide, re.S)
    regex_number = "-*\d+\.?\d*"
    return re.findall(regex_number, temp[0], re.S)


def getDropDownSelection(options, answer):
    if debug:
        print "\n option is ", options
        print "     answer is ", answer
        print "-----------"
    return options.index(answer)


def getByLocation(solution, index, back):
    desText = []
    solutionContent = solution.split("\n")
    solutionInfo = [x for x in solutionContent if x.strip()]
    # solutionInfo = [x for x in solutionContent if x is not " "]

    if not back:
        desText.append(solutionInfo[index])
        return desText
    else:
        desText.append(solutionInfo[-index])
        return desText


def getCheckBoxOption(solution):
    options = []
    answers = []
    solutionContent = solution.split("\n")
    solutionInfo = [x for x in solutionContent if x]

    for answer in solutionInfo:
        if answer == 'true' or answer == 'false':
            answers.append(answer)
    options = solutionInfo[2:6]
    if debug:
        print options
        print answers
    return options, answers


finalOutput = []
for solution in allSolution:
    rowResult = []
    if byLocation:
        for i in range(0, len(locationArr)):
            rowResult = rowResult + getByLocation(solution, locationArr[i], False)

            # tempText = getByLocation(solution, locationArr[i], False)
            # tempArray = tempText[0].split('.')
            # rowResult.append(tempArray[0]+".")
            # rowResult.append(tempArray[1]+".")

    if Mathtex:
        rowResult = rowResult + getMathtex(solution)
    if inputBox:
        inputAnswer = getInput(solution, regex)
        rowResult = rowResult + inputAnswer
    if dropdown:
        # MathtexResult = getMathtex(solution)
        # dropdownRes = getDropDownSelection(MathtexResult[3:7], MathtexResult[2])
        print allSolution.index(solution) + 1
        rowResult = rowResult + getDropDown(solution)
    if checkBox:
        options, answers = getCheckBoxOption(solution)
        rowResult = rowResult + options + answers

    if images:
        skillNumber = skillNum.split(".")
        numOfAE = len(allSolution) - 10
        if allSolution.index(solution) < numOfAE :
            imagePath = str(skillNum)+"/"+"math-g9-c"+str(skillNumber[0])+"-s"+str(skillNumber[0])+"-"+str(skillNumber[1])+"-ap"+ str(allSolution.index(solution)+1) + "-img1.png"
        else :
            imagePath = str(skillNum)+"/"+"math-g9-c"+str(skillNumber[0])+"-s"+str(skillNumber[0])+"-"+str(skillNumber[1])+"-p"+ str(allSolution.index(solution)+1) + "-img1.png"
        rowResult.append(imagePath)
    if getAnswerOptionIndex:
        rowResult.append(getAnswerIndex(solution))
    # getDropDown(solution)
    # temp = []
    # rowResult = rowResult + temp.append(getDropDown(solution))
    # rowResult.append( getDropDown(solution))
    finalOutput.append(rowResult)

finalOutput = map(list, zip(*finalOutput))
# [list(i) for i in zip(*finalOutput)]

# for x in finalOutput:
#     print x

finalObj = {}
for i in range(0, len(finalOutput)):
    if i < 9:
        key = "tobereplace" + "0" + str(i + 1)
    else:
        key = "tobereplace" + str(i + 1)

    finalObj[key] = finalOutput[i]

print "===================================="

for skill in finalObj:
    print skill, finalObj[skill]
print "===================================="

print "Number of Skill: ", len(finalOutput[0])
generateProblem(templatePath, outputPath, finalObj, len(finalOutput[0]), skillNum, toolTip)
