#usage python distributerandom.py inputfile outputfile
#inputfile is a two column file wth specimen id and clusterid separated by tab
import sys,random

o=open(sys.argv[2],'w')
k={}

with open(sys.argv[1]) as infile:
	l=infile.readlines()
	for each in l:
		m=each.strip().split('\t')
		k[m[0]]=m[1]

n=0
while n<=100:
	sublist1=random.sample(list(k.keys()),1456)
	sublist2=[x for x in list(k.keys()) if x not in sublist1]
	print(len(sublist1),len(sublist2))
	clustlist1,clustlist2,clustlist2uniq=[],[],[]
	for each in sublist1:
		if k[each] not in clustlist1:
			clustlist1.append(k[each])
	for each in sublist2:
		if k[each] not in clustlist2:
			clustlist2.append(k[each])
	speccovered=0
	specnotcovered=0
	for each in sublist2:
		if k[each] in clustlist1:
			speccovered+=1
		else:
			specnotcovered+=1
	clustlist2uniq=list(set(clustlist2)-set(clustlist1))

	clustlist2overlap=list(set(clustlist2)&set(clustlist1))
	o.write(str(len(clustlist1))+'\t'+str(len(clustlist2))+'\t'+str(len(clustlist2uniq))+'\t'+str(len(clustlist2overlap))+'\t'+str(speccovered)+'\t'+str(specnotcovered)+'\n')

	n+=1

o.close()

