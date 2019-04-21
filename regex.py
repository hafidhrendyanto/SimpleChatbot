import re
import heapq
import sys
import json

file = open("RegexLib.txt", 'r')

queries = []
answers = []

for lines in file :
    line = lines.replace('\n', '').split(" -> ")
    queries.append(line[0])
    answers.append(line[1])

inp = ""

matchedAnswers = []
inp = sys.argv[1]
for i in range(len(queries)) :
    matchCount = 0
    lastidx = 0
    spacecount = -1
    query = queries[i].split(' ')
    for sentence in query.copy() :
        matchobj = re.search(sentence, inp)
        if (matchobj != None) :
            if (matchobj.group() == '') :
                doublecek = re.findall(sentence, inp)
                for cek in doublecek :
                    if len(cek) != 0 :
                        matchCount += len(cek)
                        spacecount += 1
                        lastidx = re.search(cek, inp).start()
                        break
            elif (matchobj.start() >= lastidx) :
                matchCount += matchobj.end() - matchobj.start()
                spacecount += 1
                lastidx = matchobj.end() - 1
            query.remove(sentence)

    querylen = matchCount + spacecount
    for sentence in query :
        querylen += (len(sentence) - (sentence.count("[")*4 + sentence.count("(")*3))
    if len(inp) > querylen : 
        percentage = ((matchCount + spacecount)/len(inp))*100
    else :
        percentage = ((matchCount + spacecount)/(querylen))*100
    #print((matchCount + inp.count(" ")), len(inp), percentage)
    heapq.heappush(matchedAnswers, ((-1)*percentage, answers[i]))

ans = heapq.heappop(matchedAnswers)
if ((-1)*(ans[0])) >= 80 :
    print(json.dumps(ans[1]))
else : 
    print(json.dumps("Answer not found, please rearange your query!"))