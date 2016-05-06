import re

#----------------Usage-----------------------------------
#  1) Ipnut txtPath from slides
#  2) Choose number of AE
#  3) Run and check your result
#----------------input--Here---------------------------------


# txtPath = "/Users/rhe/Downloads/Grade 7_ Skill 13.4.txt"

skillNumber = "2.6"

totalLen = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3]
#######
print sum(totalLen)
hintIds = []
start = 1
for i in totalLen:
    temp = range(start,start+i)
    start += i
    hintIds.append(temp)

print hintIds

def do(m):
    global index
    text = "\"hintIds\": {0}".format(hintIds[index])
    index = index + 1
    return text

#------------------init path-----------------------------------------

regex_txtPath = "\d+\.\d+"
# fileName = re.search(regex_txtPath, txtPath, re.S)
# skillNumber = fileName.group(0)
# fileName = txtPath.split()
# skillNumber = fileName[-1].strip(".txt")
# print "----------", skillNumber
# print "----------"+fileName.group(0)

projectPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/8th/"
skillPath = projectPath + skillNumber + "/skill_problem.json"
print skillPath
#----------------get IDs from .txt-----------------------------------

index = 0
# def replaceId():
#     global index
#     text = "\"hintIds\": {0}".format(values[index])
#     index = index + 1
#     return text

print hintIds

# filePath = "sample.json"
data = ""
with open(skillPath, 'r') as f:
    data = f.read()



regex_hint_id = "\"hintIds\":\s+\[.*?\]"
# text = re.sub(regex_hint_id, replaceId, data, 0, re.S)

text = re.sub(regex_hint_id, do, data, 0, re.S)


with open(skillPath, 'w') as txtfile:
    txtfile.write(text)



