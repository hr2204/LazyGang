
filePath = "/Users/rhe/Documents/Test/LazyGang/hitsGenerator/problemTest/template.txt"
outputPath = "/Users/rhe/Documents/Test/LazyGang/hitsGenerator/problemTest/output.txt"

# with open(filePath) as data_file:
#     data = json.load(data_file)
#
# for test in data[0]["answer_value"]:
#     print test

numOfProblem = 11
# print str(data[1])
replace_value = {
    # "problemId": range(1,numOfProblem+1),
    "answer_value": ["6.92","6","4.13",'8.4','6','4.91','4','3.51','4.8','2.1','7.48'],
    "question_1": ["Jane drove $7.32 \\\\times 10^8$ millimeters on a road trip in June. In August, she drove $40,000$ meters on another road trip.",
                   "The mass of an airplane is $300,000$ kilograms, and the mass of a space shuttle is $1.8 \\\\times 10^13$ grams.",
                   "Tank A holds $430$ liters of liquid. Tank B holds $3.7 \\\\times 10^6$ milliliters of liquid.",
                   "Sue lives $13,300,000$ centimeters away from the airport. She lives $4.9 \\\\times 10^4$ meters away from a museum.",
                   "An ant colony inhabits an area of $16,000$ square units of land. There are $9.6 \\\\times 10^7$ ants living in the colony. ",
                   "Jack was running sprints at his school's track. For his first sprint, he ran $340,000$ millimeters. For his second sprint, he ran $4.57 \\\\times 10^3$ meters.",
                   "A country with an area of $8.4 \\\\times 10^9$ square miles has a population of $210,000$ people. ",
                   "The mass of a motorcycle is $3.67 \\\\times 10^2$ kilograms. The mass of a young boy is $16,000$ grams. ",
                   "Adam ran $5 \\\\times 10^3$ meters on Saturday, and he biked $43$ kilometers on Sunday.",
                   "Tank X contains $30,000,000$ milliliters of water. Tank Y contains $6.3 \\\\times 10^8$ liters of water. ",
                   "Space Shuttle M traveled a distance of $840,000,000$ kilometers. Space Shuttle N traveled a distance of $9.2 \\\\times 10^{10}$ meters."
                   ],
    "question_2":["How much farther did Jane drive in June compared to August?",
                  "How many times heavier is a space shuttle compared to an airplane?",
                  "How much liquid do the tanks hold altogether?",
                  "How much farther is the airport from Sue's house compared to the museum?",
                  "How many ants are there per square unit of land?",
                  "How far did Jack sprint in total?",
                  'How many square miles are there per person in the country?',
                  'How much heavier is a motorcycle than a boy?',
                  'What was his total distance traveled over both days? ',
                  "How many times more water does Tank Y contain compared to Tank X?",
                  "How much farther did Shuttle M travel compared to Shuttle N?"],
    "answer_1":[0,0,2,0,0,1,0,0,2,0,2]
    # "value":["1","","2"],
}
# print replace_value["question_2"][7]

def generateProblem(templatePath,replaceValue,numOfProblem):
    with open(templatePath, 'r') as f:
        template = f.read()

    # text = re.sub(regex_hint_id, replaceId, data, 0, re.S)
    final_out = "["

    keys = replaceValue.keys()  #get all keywords need to replace
    print keys
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

generateProblem(filePath,replace_value,11)