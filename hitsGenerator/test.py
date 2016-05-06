__author__ = 'HeRen'
import re


class HintsGenrator(object):

    def __init__(self, sourceFile):
        self.sourceFile = sourceFile

    def getExercises(self):
        data = ""

        with open(self.sourceFile, 'r') as f:
            data= f.read()

        regex_exe = "Exercise #\d+\)[\s\S].*?\(Exercise #\d* - Solution\)"
        exeMatches = re.findall(regex_exe, data, re.S)

        print "Get {0} Exe".format(len(exeMatches))

        exeHints = []
        exeHintsLen = []
        for exe in exeMatches:
            regex_exe_hints = "\(Exercise #\d+ - Hints\).*?Tool Tip:"
            exeHintMatches = re.findall(regex_exe_hints, exe, re.S)
            exeHintsLen.append(len(exeHintMatches))
            exeHints.append(exeHintMatches[len(exeHintMatches)-1])

        return exeHints , exeHintsLen




if __name__ == '__main__':
    file = '/Users/rhe/Downloads/Grade 7_.Skill 13.10.txt'

    hg = HintsGenrator(file)

    hg.getExercises()
