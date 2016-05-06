import re
from problemLib import generateProblem
from problemLib import getMathtex


filePath = "/Users/rhe/Downloads/Grade 8_.Skill 4.10.txt"
templatePath = "/Users/rhe/Documents/Test/LazyGang/hitsGenerator/problemTest/template2.txt"
outputPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/8th/4.10/skill_problem.json"

# open text file
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




# for final output
regex = "input\n.*?\\n"
def getInput(solutionSlide,regex):
    temp = re.findall(regex, solutionSlide, re.S)
    regex_number = "-*\d+\.?\d*"
    return re.findall(regex_number, temp[0], re.S)

def getDropDownSelection(options,answer):
    print "\n option is ",options
    print "     answer is ", answer
    print "-----------"
    return options.index(answer)

dropdown = False
dropdown = True
finalOutput = []
for solution in allSolution:
    inputAnswer = getInput(solution,regex)
    MathtexResult = getMathtex(solution)
    rowResult = MathtexResult + inputAnswer
    if dropdown:
        dropdownRes = getDropDownSelection(MathtexResult[3:7],MathtexResult[2])
        rowResult.append(dropdownRes)


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