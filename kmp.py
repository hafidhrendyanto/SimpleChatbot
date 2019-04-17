#bikin tabel2an itu
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def kmpPreprocess(pattern):
	patternLength = len(pattern)
	borderTable = []
	for x in range(patternLength):
		borderTable.append(0)

	j = 0
	i = 1

	while (i < patternLength):
		if (pattern[j] == pattern[i]):
			borderTable[i] = j + 1
			i = i + 1
			j = j + 1
		elif (j > 0):
			j = borderTable[j-1]
		else:
			borderTable[i] = 0
			i = i +1

	return borderTable
#kmp super precise
def kmp(text, pattern):
	textLength = len(text)
	patternLength = len(pattern)

	borderTable = kmpPreprocess(pattern)
	i = 0
	j = 0

	while (i < textLength):

		if (pattern[j] == text[i]):
			if (j == (patternLength - 1)):
				return i - patternLength + 1
			i = i + 1
			j = j + 1
		elif (j > 0):
			j = borderTable[j-1]
		else:
			i = i + 1

	return -1

#kmp neko neko
def kmpv2(text, pattern, i):
	global answers
	textLength = len(text)
	patternLength = len(pattern)
	lastidx  = -1
	t = text
	p = pattern.split(" ")
	percent = 0
	counter = 0

	for f in p:
		lastidx = kmp(text, f)
		if (lastidx != -1):
			counter = counter + 1
			percent = percent + len(f) + 1
			if len(t) > lastidx :
				t = t[0: 0:] + t[lastidx + 1::]
	if (counter > len(p)*0.8):
		print("Jawaban: " + answers[i])
	print("Confidence = " + str(percent*100/textLength))


#main prog
#filenya blom keisi bgt

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
 
# Kalimat
#kalimat = 'Dengan Menggunakan Python dan Library Sastrawi saya dapat melakukan proses Stopword Removal'
#stop = stopword.remove(kalimat)

file = open("1.txt", 'r')
global answers
queries = []
answers = []

for lines in file :
	line = lines.replace('\n', '').split(" -> ")
	queries.append(line[0])
	answers.append(line[1])

while 1:
	p = input('your question pls: ')
	print()
	pattern = stopword.remove(p)
	valid = 0
	for i in range(len(queries)):
		kal = stopword.remove(queries[i])
		if (kmp(kal.lower(),pattern.lower()) != -1):
			if (valid == 0):
				percent  = len(pattern)*100/len(kal)
				print(percent)
				if (percent > 80):
					print("Jawaban: "+ answers[i])
				valid = 1
		else:
			if (valid == 0):
				kmpv2(kal.lower(), pattern.lower(), i)


#kmp buat cek pertama, kalo ketemu lansgung 100 percent
#kalo ga ketemu, pake kmp v 2
