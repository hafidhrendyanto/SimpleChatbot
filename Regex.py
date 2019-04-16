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
        matchCount = 0
        query = queries[i].split(' ')
        for sentence in query :
            if (re.search(sentence, inp) != None) :
                matchCount += len(re.search(sentence, inp).group())
        percentage = ((matchCount + inp.count(" "))/len(inp))*100
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


