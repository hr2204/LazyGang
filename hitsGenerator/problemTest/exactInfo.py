import re
from problemLib import generateProblem
from problemLib import getMathtex

skillNum = "3.13"
filePath = "/Users/rhe/Downloads/Grade 8_.Skill "+ skillNum+".txt"
templatePath = "/Users/rhe/Documents/Test/LazyGang/hitsGenerator/problemTest/template3.txt"
outputPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/8th/" + skillNum +"/skill_problem.json"

# open text file and
with open(filePath, 'r') as f:
    text = f.read()



#exact solution slide
regex_solution = "Exercise #\d+ - Solution\).*?Tool Tip:"
allSolution = re.findall(regex_solution, text, re.S)




# get dropdown answer
# dropdownAnswer = []
# for x in allSolution:
#     temp = []
#     solutionInfo = x.split("\n")
#     print solutionInfo


# for test in allSolution:
#     print test

# print len(allSolution)

debug = False
dropdown = False
inputBox = False
Mathtex = True
checkBox = False
descritionTxt = False
# for final output
regex = "input\n.*?\\n"
def getInput(solutionSlide,regex):
    temp = re.findall(regex, solutionSlide, re.S)
    regex_number = "-*\d+\.?\d*"
    return re.findall(regex_number, temp[0], re.S)

def getDropDownSelection(options,answer):
    if debug:
        print "\n option is ",options
        print "     answer is ", answer
        print "-----------"
    return options.index(answer)

def getDescrition(solution,index):
    desText = []
    solutionContent = solution.split("\n")
    solutionInfo = [x for x in solutionContent if x]
    desText.append(solutionInfo[index])
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



# dropdown = True
finalOutput = []
for solution in allSolution:
    rowResult = []
    if Mathtex:
        rowResult = rowResult + getMathtex(solution)
    if inputBox:
        inputAnswer = getInput(solution,regex)
        rowResult = rowResult + inputAnswer
    if dropdown:
        MathtexResult = getMathtex(solution)
        dropdownRes = getDropDownSelection(MathtexResult[3:7],MathtexResult[2])
        rowResult.append(dropdownRes)
    if checkBox:
        options, answers = getCheckBoxOption(solution)
        rowResult = rowResult + options + answers

    if descritionTxt:
        rowResult = rowResult + getDescrition(solution,1)

    finalOutput.append(rowResult)



finalOutput = map(list, zip(*finalOutput))
# [list(i) for i in zip(*finalOutput)]

for x in finalOutput:
    print x

finalObj = {}
for i in range(0,len(finalOutput)):
    key = "tobereplace" + str(i+1)
    finalObj[key] = finalOutput[i]

print "===================================="

for skill in finalObj:
    print skill,finalObj[skill]


generateProblem(templatePath,outputPath,finalObj,len(finalOutput[0]))