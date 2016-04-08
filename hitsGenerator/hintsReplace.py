import re

values = ["this is hints 1 id", "this is hints 2 id", "this is hints 3 id"]
index = 0

def do(m):
    global index
    text = "\"hintIds\": [{0}]".format(values[index])
    index = index + 1
    return text


filePath = "sample.json"
data = ""

with open(filePath, 'r') as f:
    data = f.read()

# regex_hint_id = "(\"hintIds\":\s+\[)(.*?)(\])"
regex_hint_id = "\"hintIds\":\s+\[.*?\]"

# hintsMatches = re.findall(regex_hint_id, data, re.S)
# print "-- Get {0} hints ----".format(len(hintsMatches))
#
# for hint in hintsMatches:
#     print hint

# text = re.sub(regex_hint_id, lambda x: values[x.group()], data)
text = re.sub(regex_hint_id, do, data, 0, re.S)
print text
