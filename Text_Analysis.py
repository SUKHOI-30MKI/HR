import io
import nltk
import xlwt				#
import urllib2 				#url data fetch fromthe 
import xlrd 				#excel reading package 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textstat.textstat import textstat
j=0
workbook_write=xlwt.Workbook(encoding="utf-8")
sheet1=workbook_write.add_sheet("sheets1")
for i in range(1,4): # change the value of loop acoording to the analysis of the url in c_l.xlsx
	f=open('/home/shantanu/Desktop/intermediate.txt','w')
	file_location="c_l.xlsx"
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	ur=sheet.cell_value(i,5) 
    	response=urllib2.urlopen(ur)
    	data=response.read()
	print(data)
    	f.write(data)
	#initialize values of variable
	sumneg=0		
	sumpos=0
	sum1=0
	sum2=0
	j=0
	wordneg = set(stopwords.words('neg'))  #put the negative words dictionary in stopword directory
	wordpos = set(stopwords.words('pos'))	#put the negative words dictionary in stopword directory
	f1=open('intermediate.txt')		# file opening
	# finding the number of sentences using tokenization
	word=nltk.word_tokenize(f1.read())
	#line = f.read()
	#word=line.split()
	for s in word:
		ns=s.lower()
		sum1 = sum1 + 1		#sum of number of words
		if ns in wordneg:		
			sumneg = sumneg - 1
		if ns in wordpos:
			sumpos = sumpos + 1	
	sumneg = (sumneg*-1)			# make number of negative words (multiply by -1)

	ss=(sumpos+sumneg)/((sum1) + 0.000001)	#canculation of subjective score

	ps=(sumpos-sumneg)/((sumpos+sumneg) + 0.000001)		#calculation of polarity score

	sheet1.write(i,j,sumneg)
	workbook_write.save("output.xlsx")
	j = j+1
	sheet1.write(i,j,sumpos)
	workbook_write.save("output.xlsx")
	j = j+1
	sheet1.write(i,j,ps)
	workbook_write.save("output.xlsx")
	j = j+1
	sheet1.write(i,j,ss)
	workbook_write.save("output.xlsx")	
	j = j+1

	# Counting the number of complex words 
	if __name__ == '__main__':
		words=nltk.word_tokenize(f1.read())
		for s in words:
			ns=s.lower()
			if textstat.syllable_count(s)>2:   		#if syllable count is greater then 2 then count that word
					sum2 = sum2 + 1
	sheet1.write(i,j,sum2)
	workbook_write.save("output.xlsx")
	j= j+1	
	#print('number of complex words',sum2)
	#number of sentences in a text
	f2 = open('intermediate.txt','rb')
	sentence = nltk.sent_tokenize(f2.read())
	l=len(sentence)
	sheet1.write(i,j,l)
	workbook_write.save("output.xlsx")
	j = j+1
        #number of sentences
	#print('number of sentences ',l)

	avgl=(sum1/l)                            #average sentence length
	per_c_word=(sum2/sum1)                   #percentage of complex words 
	fog_index=(0.4*(avgl+per_c_word))        #calculation of fog index
	avgnumberofword=((sum1)/l)               #average number of words per sentence

	sheet1.write(i,j,avgl)
	workbook_write.save("output.xlsx")
	j=j+1
	sheet1.write(i,j,per_c_word)
	workbook_write.save("output.xlsx")
	j=j+1
	sheet1.write(i,j,fog_index)
	workbook_write.save("output.xlsx")
	j = j+1
	sheet1.write(i,j,avgnumberofword)
	workbook_write.save("output.xlsx")
	j = j+1
	#print('average sentence length',avgl)
	#print('percentage of complex words',per_c_word)
	#print('claculation of fog index',fog_index)
	#print('average number of words per sentence',avgnumberofword)                                         







