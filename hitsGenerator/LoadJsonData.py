__author__ = 'georgehu'

# import jsonpickle
import re
import json
from collections import namedtuple

import demjson
import os.path
import os.path
# skillDao=skillDAO.SkillDAO()

class LoadJson(object):
    def __init__(self):
        pass

    def getFileRows(self,filename):
        index = 0
        try:
            if(os.path.exists(filename)):


                with open(filename) as f:
                    for line in f:
                        index = index + 1
                        # print '---line---: ',line
        except:
            print "files does not exist: ",filename
        return index + 1


    def dict_generator(self,indict, pre=None):
        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    for d in self.dict_generator(value, [key] + pre):
                        yield d
                elif isinstance(value, list) or isinstance(value, tuple):
                    for v in value:
                        for d in self.dict_generator(v, [key] + pre):
                            yield d
                else:
                    yield pre + [key, value]
        else:
            yield indict

        print ':::generator done'
    def decodeSkillwighGrade(self,jsondata,grade=2):#, skill):
        start = jsondata.find("[", 0, len(jsondata))
        end = jsondata.rfind("]", 0, len(jsondata))

        jsonPre = jsondata[start + 1: end]

        print jsonPre

  # "program_type": "Math",
  # "program_id":"1",
  # "level": "Grade 2",
  # "grade_id":"2",
  # "chapters":[
  #   {
  #     "chapter_id":1,
  #     "chapter_name":" Counting through 100",
  #     "skills":[
  #       {
  #         "skill_id": 1,



        term = "chapter_id"
        #term = "skill_id"

        headlist = re.finditer(term, jsonPre)
        pointlist = []
        for head in headlist:
            print "==by Search skill chapter=", head.start()
            pointlist.append(head.start())

        print "====", len(pointlist)
        print pointlist

        pointlist.append(end)

        print pointlist

        demoCollection = []

        for i in range(len(pointlist) - 1):
            print i, pointlist[i]
            a = pointlist[i]
            b = pointlist[i + 1]
            print "[a,b]: ", "[", a, " ", b, "]"
            print '--------------------------'

            preDemo = jsonPre[a:b].strip()


            if preDemo.endswith("}"):
                print "ends with , ", i

            else:

                print "not end with ,", i
                b = preDemo.rfind("}")
                preDemo = preDemo[0:b + 1]

            demoCollection.append(preDemo)
            print "========i=====", i


            if preDemo.startswith("{"):
                pass
            else:
                preDemo = "{" + preDemo

            print "====final preChapter==="
            print preDemo

            response = json.loads(preDemo)
            for doc in response['skills']:
                print(doc['skill_id'], doc['weigth'])

            #problem = jsonpickle.decode(preproblem)
            #self.saveSkill(preDemo)#,skill)
            skillDao.add_chapter_skill_json(preDemo,grade)

        return demoCollection

    def decodeDemo(self,jsondata, skill):
        start = jsondata.find("[", 0, len(jsondata))
        end = jsondata.rfind("]", 0, len(jsondata))

        jsonPre = jsondata[start + 1: end]

        print jsonPre
        term = "demo_id"

        headlist = re.finditer(term, jsonPre)
        pointlist = []
        for head in headlist:
            print "==by Search=", head.start()
            pointlist.append(head.start())

        print "====", len(pointlist)
        print pointlist

        pointlist.append(end)

        print pointlist

        demoCollection = []

        for i in range(len(pointlist) - 1):
            print i, pointlist[i]
            a = pointlist[i]
            b = pointlist[i + 1]
            print "[a,b]: ", "[", a, " ", b, "]"
            print '--------------------------'

            preDemo = jsonPre[a:b].strip()


            if preDemo.endswith("}"):
                print "ends with , ", i

            else:

                print "not end with ,", i
                b = preDemo.rfind("}")
                preDemo = preDemo[0:b + 1]

            demoCollection.append(preDemo)
            print "========i=====", i


            if preDemo.startswith("{"):
                pass
            else:
                preDemo = "{" + preDemo

            print "====final predemo==="
            print preDemo

            #problem = jsonpickle.decode(preproblem)
            self.saveDemo(preDemo,skill)
        return demoCollection


    def saveDemo(self,demojson,skill):
        demodao = demoDAO.DemoDAO()
        demoobj = demo.Demo()
        demoobj.setExplanationText(demojson)
        demoobj.setskillid(skill)

        try:

            rtId = demodao.add_demo(demoobj)
            print "===insert demo id: ", rtId
        except Exception as e:
            print e.message()
            print '!!!!!!!!insert failed.'


    def decodeProblem(self,jsondata,skill):
        start = jsondata.find("[", 0, len(jsondata))
        end = jsondata.rfind("]", 0, len(jsondata))

        jsonPre = jsondata[start + 1: end]

        print jsonPre
        term = "skill_id"  # "problem_id"

        headlist = re.finditer(term, jsonPre)
        pointlist = []
        for head in headlist:
            print "==by Search=", head.start()
            pointlist.append(head.start())
        print "====", len(pointlist)
        print pointlist

        pointlist.append(end)

        print pointlist

        problemCollection = []

        for i in range(len(pointlist) - 1):
            print i, pointlist[i]

            a = pointlist[i]
            b = pointlist[i + 1]
            print "[a,b]: ", "[", a, " ", b, "]"
            print '--------------------------'

            preproblem = jsonPre[a:b].strip()
            # print "before:===",preproblem

            if preproblem.endswith("}"):
                print "ends with , ", i

            else:

                print "not end with ,", i
                b = preproblem.rfind("}")
                preproblem = preproblem[0:b + 1]

            problemCollection.append(preproblem)
            print "========i=====", i
            #print "after====",preproblem

            if preproblem.startswith("{"):
                pass
            else:
                preproblem = "{" + preproblem

            print "====final"
            print preproblem

            #problem = jsonpickle.decode(preproblem)

            print "===problem ==   [ " + str(id) + "   ]====inserted="

        for problemjson in problemCollection:
            problem_object = self.createProblemEntity(problemjson,skill)
            # id=problemdao.add_problemJson(preproblem)

        print "=====final===="
        # print problemCollection


    def createProblemEntity(self,problemjson,skill):
        # 'skill_id': object.skill_id,
        # 'problem_id': object.problem_id,
        # 'template_type': object.template_type,
        # 'description': object.description,
        # 'user_input_grp_description': object.user_input_grp_description,
        # 'meta_data': object.meta_data,
        # 'demo_id': object.demo_id,
        # 'hintIds': object.hintIds,
        # 'specified_time': object.specified_time,
        # 'weight':object.weight,
        # 'id':object.id,
        # 'images':object.images,
        # 'problemItems':object.problemItems,
        # 'assisted_exercise':object.assisted_exercise

        print '==stat decode problem json===='

        print problemjson
        problemdao = problemDAO.ProblemDAO()
        problem_obj = problem.Problem()

        problem_obj.setdescription(problemjson)
        problem_obj.setSkillId(skill)

        id = problemdao.add_problem(problem_obj)
        print "==problem id  : ", id

        return problem_obj


        #print problem["skill_id"],problem["problem_id"],problem["template_type"],problem["description"],problem["user_input_grp_description"],


    def decodeHints(self,jsondata, skill):
        hintdao = hintDAO.HintDAO()
        hint = hints.Hint()

        start = jsondata.find("[", 0, len(jsondata))
        end = jsondata.rfind("]", 0, len(jsondata))

        jsonPre = jsondata[start + 1: end].strip()

        hintslist = jsonPre.split("},")


        # print jsonPre
        print hintslist[0], hintslist[1], hintslist[len(hintslist) - 1]

        newHintList = []

        for hinttmp in hintslist:


            if not hinttmp.strip().endswith("}"):
                #print hint
                hinttmp = hinttmp + "}"
                #print hint
                newHintList.append(hinttmp)

        print "=======after==="

        #print newHintList[0],newHintList[1],newHintList[len(newHintList)-1]

        hintslist = []
        for hintStr in newHintList:
            #hintdao.add_hint_json(hintStr)

            obj = jsonpickle.decode(hintStr)

            print obj
            #print "====",obj["hint_id"],\
            print obj["description"], obj["hinticon"], obj["hintimgs"]
            #hint.settitle()
            hint.setdescription(obj["description"])
            #hint.setHint_id(obj["hint_id"])
            hint.sethinticon(obj["hinticon"])
            hint.setHintImages(obj["hintimgs"])
            hint.setSkillId(skill)


            hintdao.add_hint(hint)

            hintslist.append(hint)
            # self.uuid = None
            # self.hint_id =0
            # self.description = ""
            # self.title = ""
            # self.hinticon = ""
            # self.hintimgs = []

        return hintslist





    def readJson(self,filename):
            data = [None] * (self.getFileRows(filename)-1)
            json_data=''
            print " !!!!file name: ",filename
            if(os.path.exists(filename)):
                with open(filename) as f:
                    index = 0
                    for line in f:

                        data[index] = line.rstrip('\n')
                        index = index + 1
                        #'test string \n'.rstrip('\n')
                        #print '---line---: ',line

                json_data = ''.join(str(e) for e in data)


            # print '\n'
            # print '\n'
            # print json_data

            # return json_data
            obj=demjson.decode(json_data)# '["one",42,true,null]' )  # From JSON to Python
            return obj

    def generaateJson(self,obj):

            json=demjson.encode(obj)# ['one',42,True,None] )    # From Python to JSON
            # '["one",42,true,null]'
            return json

    def loadJsonFile(self,filename, type=None, skill="1.1"):
        data = [None] * self.getFileRows(filename)
        with open(filename) as f:
            index = 0
            for line in f:
                index = index + 1

                data[index] = line.rstrip('\n')
                #'test string \n'.rstrip('\n')
                print '---line---: ',line

        json_data = ''.join(str(e) for e in data)


        hintList=[]

        if (type == "DEMO"):
            demoList = self.decodeDemo(json_data, skill)
            # pass
        elif (type == "PROBLEM"):

            problemList=self.decodeProblem(json_data,skill)
        elif (type =="SKILL"):
             print "===========start decode skill......"
             skilllist= self.decodeSkillwighGrade(json_data)#, skill)
        elif (type=="HINT"):
            print "start pint hint-------"
            hintList = self.decodeHints(json_data, skill)
        else:
            # pass
            print "Nothing to load"

        hintdao = hintDAO.HintDAO()
        for hintobj in hintList:
            pass

            #hintdao.add_hint(hintobj)

        # print json_hints
        return json_data