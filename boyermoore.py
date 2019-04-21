# String Matching with Boyer Moore
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import sys
import json

def lastOccur(pattern):
    last = [-1]*128

    for i in range(len(pattern)):
        last[ord(pattern[i])] = i

    return last

def bm(text, pattern):
    last = lastOccur(pattern)
    n = len(text)
    m = len(pattern)

    i = 0

    while(i<=n-m) :
        j = m-1
        while(j>=0 and pattern[j] == text[i+j]):
            j = j-1

        if j<0:
            return i
        else :
            i = i+ max(1, j-last[ord(text[i+j])])

    return -1

def bm2(text, pattern):
    n = len(text)
    #m = len(pattern)
    checker = -1
    txt = text
    pat = pattern.split(" ")
    counter = 0
    percentage = 0

    for p in pat:
        checker = bm(txt,p)
        if(checker != -1):
            counter += 1
            percentage = percentage + len(p) +1
            if(len(txt)> checker):
                txt = txt[checker + 1::]

    return percentage*100/n



#MAIN
#print("BM algo")   
#print(bm("Jelaskan apa itu chatbot apa itu chatbot berdasarkan apa yang kamu baca", "apa itu chatbot"))
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
file = open("1.txt", 'r')
global answers
queries = []
answers = []

for lines in file :
	line = lines.replace('\n', '').split(" -> ")
	queries.append(line[0])
	answers.append(line[1])

#while True:
p = sys.argv[1]
inp = stopword.remove(p)

valid = 0
for i in range(len(queries)):
    kal = stopword.remove(queries[i])
    if (bm(inp.lower(), kal.lower()) != -1):
        if (valid == 0):
            #print(bm(inp.lower(), kal.lower()))
            percent  = len(inp)*100/len(kal)
            #print("Confidence1 : " + str(percent))
            if (percent > 80):
                print(json.dumps(answers[i]))
            valid = 1
    else:
        if valid == 0:
            if(bm2(inp.lower(),kal.lower()) >= 80):
                #print("Confidence2 : " + str(bm2(inp.lower(), kal.lower())))
                print(json.dumps(answers[i]))
                valid = 1

if(valid == 0) :
    print(json.dumps("no answer"))
