import re


def getMathtex(solutionSlide):
    regex = "\$.*?\$"
    return re.findall(regex, solutionSlide, re.S)

def generateProblem(templatePath,outputPath,replaceValue,numOfProblem):
    with open(templatePath, 'r') as f:
        template = f.read()

    # text = re.sub(regex_hint_id, replaceId, data, 0, re.S)
    final_out = "["

    keys = replaceValue.keys()  #get all keywords need to replace
    print "===================================="
    print "keys:",keys
    # keys: ['answer_value', 'question_1', 'value', 'problemId']

    for i in range(0,numOfProblem):
        # for x in replace_value["answer_value"]:
        text = template.replace("problemID",str(i+1))
        for key in replaceValue.keys():
            text = text.replace(key,str(replaceValue[key][i]))

        final_out = final_out + '\n' + text + ','

    final_out = final_out[:-1]
    final_out = final_out + '\n' + ']'

    # print replace_value["problemId"]


    with open(outputPath, 'w') as txtfile:
        txtfile.write(final_out)
