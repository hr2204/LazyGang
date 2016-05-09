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
hintIds = []

index = 0
def replaceID(skillNumber,totalLen,templateType):
    print sum(totalLen)
    global hintIds
    start = 1
    for i in totalLen:
        temp = range(start,start+i)
        start += i
        hintIds.append(temp)

    print hintIds

    projectPath = "/Users/rhe/Documents/git/mathjoy-dev/app/static/src/data/math/8th/"
    skillPath = projectPath + skillNumber + "/skill_problem.json"
    print skillPath
    data = ""
    with open(skillPath, 'r') as f:
        data = f.read()


    regex_hint_id = "\"hintIds\":\s+\[.*?\]"
    text = re.sub(regex_hint_id, do, data, 0, re.S)
    regex_template_type = "hint_template_type\":\s+\".*\","
    if templateType == "singleColumn":
        text = re.sub(regex_template_type, "hint_template_type\": \"singlecolumn\",", text)
    if templateType == "twoColumn":
        text = re.sub(regex_template_type, "hint_template_type\": \"two_columns_hint_b\",", text)

    with open(skillPath, 'w') as txtfile:
        txtfile.write(text)

def do(m):
    global index
    text = "\"hintIds\": {0}".format(hintIds[index])
    index = index + 1
    return text

#------------------init path-----------------------------------------

#----------------get IDs from .txt-----------------------------------





# replaceID(skillNumber,totalLen)







