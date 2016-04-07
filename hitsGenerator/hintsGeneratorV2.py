import re

filePath = "/Users/sma/LazyGang/Grade 7- Skill 10.7.txt"
data = ""

with open(filePath, 'r') as f:
    data= f.read()


regex_left = "\[left\].*?\[\/left\]"
regex_right = "\[right\].*?\[\/right\]"


leftMatches = re.findall(regex_left, data, re.S)
print "Get {0} left hints".format(len(leftMatches))

hints_left = []
for hint in leftMatches:
    hints_left.append(hint)



rightMatches = re.findall(regex_right, data, re.S)
print "Get {0} right hints".format(len(leftMatches))

hints_right = []
for hint in rightMatches:
    hints_left.append(hint)


