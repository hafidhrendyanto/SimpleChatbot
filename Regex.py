import re
import heapq

file = open("RegexLib.txt", 'r')

queries = []
answers = []

for lines in file :
    line = lines.replace('\n', '').split(" -> ")
    queries.append(line[0])
    answers.append(line[1])

inp = ""
while re.match("exit", inp) == None :
    matchedAnswers = []
    inp = input()
    for i in range(len(queries)) :
        print("apasi", i)
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
    
    while (True) :
        ans = heapq.heappop(matchedAnswers)
        if ((-1)*(ans[0])) >= 80 :
            print("Matched ", (-1)*(ans[0]), "% :", ans[1])
        else :
            break
        if (len(matchedAnswers) == 0):
            break


