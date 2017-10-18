import random
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

balancer, balancer_2, balancer_3 = ([] for lis in range(3))

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_2.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_3.append(l)

com_cls_room = ["PC 301(A)","PC 302","PC 303","PC 304"]
com_cls_capa = [45,31,26,21]

subs = ["AH1","AH2","G1","G2","C1","C2","AH3","AH4","AH5","G3","G4","C3","C5","C4","AH6","AH7","G5","G6","AH8","C6"]
#'''
lis, com_students = ([] for i in range(2))

for i in range(0,len(subs)):
	inp =  int(input("Enter Total in Subject -> "+subs[i]+" : "))
	lis.append(inp)

com_students.append(lis[0:6])
com_students.append(lis[6:14])
com_students.append(lis[14:])
#print com_students
#'''
#com_students = [[30,37,28,20,25,19], [29,16,42,13,26,30,27,45], [29,19,38,23,45,45]]


def honours_selector():
	counter_AH1 = 0
	counter_AH2 = 0

	for rows in range(0,2):
		for cols in range(0,5):

			lister = ["AH1","AH2"]
			
			if counter_AH1 >= 5 and 'AH1' in lister:
					lister.remove("AH1")
			if counter_AH2 >= 5 and 'AH2' in lister:
					lister.remove("AH2")

			if lister:
				gp = random.choice(lister)
				if balancer[rows][cols-1] == gp:
					lister.remove(gp)
					if lister:
						gp = lister[0]

				if gp == "AH1":
					counter_AH1 += 1
				elif gp == "AH2":
					counter_AH2 += 1

				balancer[rows][cols] = gp
			else:
				break

def honours_selector_2():
	counter_AH3 = 0
	counter_AH4 = 0
	counter_AH5 = 0

	for rows in range(1,4):
		for cols in range(0,7):

			lister = ["AH3","AH4","AH5"]
			
			if counter_AH3 >= 6 and 'AH3' in lister:
					lister.remove("AH3")
			if counter_AH4 >= 6 and 'AH4' in lister:
					lister.remove("AH4")
			if counter_AH5 >= 6 and 'AH5' in lister:
					lister.remove("AH5")

			if lister:
				gp = random.choice(lister)
				if balancer[rows][cols-1] == gp:
					lister.remove(gp)
					if lister:
						gp = lister[0]

				if gp == "AH3":
					counter_AH3 += 1
				elif gp == "AH4":
					counter_AH4 += 1
				elif gp == "AH5":
					counter_AH5 += 1

				balancer_2[rows][cols] = gp
			else:
				break

def pass_selector():

	counter_g1 = 0
	counter_g2 = 0
	counter_c1 = 0
	counter_c2 = 0
	
	for rows in range(2,5):
		for cols in range(0,4):

			lister = ["G1","G2","C1","C2"]

			if counter_g1 >= 4 and 'G1' in lister:
				lister.remove('G1')
			if counter_g2 >= 4 and 'G2' in lister:
				lister.remove('G2')
			if counter_c1 >= 3 and 'C1' in lister:
				lister.remove('C1')
			if counter_c2 >= 3 and 'C2' in lister:
				lister.remove('C2')	

			if lister:
				gp = random.choice(lister)

				if gp == 'G1':
					counter_g1 += 1
				elif gp == 'G2':
					counter_g2 += 1
				elif gp == 'C1':
					counter_c1 += 1
				elif gp == 'C2':
					counter_c2 += 1

				balancer[rows][cols] = gp
			else:
				break


def pass_selector_2():
	counter_c3 = 0
	counter_c5 = 0
	counter_g3 = 0
	counter_g4 = 0

	for cols in range(0,7):
		lister = ["C3","C5"]

		if counter_c3 >= 3 and 'C3' in lister:
			lister.remove('C3')
		if counter_c5 >= 3 and 'C5' in lister:
			lister.remove('C5')

		if lister:
			gp = random.choice(lister)
			if gp == 'C3':
				counter_c3 += 1
			elif gp == 'C5':
				counter_c5 += 1
			balancer_2[0][cols] = gp
		else:
			break

	lister = ['G3','G4']
	gp = random.choice(lister)
	if gp == 'G3':
		counter_g3 += 1
	elif gp == 'G4':
		counter_g4 += 1
	balancer_2[0][6] = gp


	for rows in range(3,5):
		for cols in range(0,7):
			if balancer_2[rows][cols] == None:
				lister = ['G3','G4']

				if counter_g4 >= 4 and 'G4' in lister:
					lister.remove('G4')
				if counter_g3 >= 4 and 'G3' in lister:
					lister.remove('G3')

				if lister:
					gp = random.choice(lister)
					if gp == 'G3':
						counter_g3 += 1
					elif gp == 'G4':
						counter_g4 += 1
					balancer_2[rows][cols] = gp
				else:
					break

	for cols in range(0,4):
		balancer_2[5][cols] = "C4"

def selector_3():
	counter_AH6 = 0
	counter_AH7 = 0
	counter_AH8 = 0
	counter_g5 = 0
	counter_g6 = 0
	counter_c6 = 0
	

	for rows in range(0,2):
		for cols in range(0,6):

			lister = ["AH6","AH7"]

			if counter_AH6 >= 6 and 'AH6' in lister:
				lister.remove('AH6')
			if counter_AH7 >= 6 and 'AH7' in lister:
				lister.remove('AH7')

			if lister:
				gp = random.choice(lister)
				if gp == "AH6":
					counter_AH6 += 1
				elif gp == "AH7":
					counter_AH7 += 1
				balancer_3[rows][cols] = gp
			else:
				break

	for rows in range(2,6):
		for cols in range(0,7):

			lister = ["G5","G6","C6"]
			if counter_g5 >= 4 and 'G5' in lister:
				lister.remove('G5')
			if counter_g6 >= 4 and 'G6' in lister:
				lister.remove('G6')
			if counter_c6 >= 3 and 'C6' in lister:
				lister.remove('C6')

			if lister:
				gp = random.choice(lister)
				if gp == "G5":
					counter_g5 += 1
				elif gp == "G6":
					counter_g6 += 1
				elif gp == "C6":
					counter_c6 += 1
				balancer_3[rows][cols] = gp
			else:
				break
	
	balancer_3[3][4] = balancer_3[3][5] = "C6(LAB)"
	counter_c6 += 2

	for cols in range(0,6):
		if balancer_3[4][cols] == None and counter_AH8 < 5:
			balancer_3[4][cols] = "AH8"
			counter_AH8 += 1

	lister = ["Env","English","Bangla"]
	random.shuffle(lister)
	balancer_3[5][0] = lister[0]
	balancer_3[5][1] = lister[1]
	balancer_3[5][2] = lister[2]

honours_selector()
honours_selector_2()
pass_selector()
pass_selector_2()
selector_3()
temp_allocate = {}

first_year,first_year_day,first_year_cls = ([] for lis in range(3))
second_year,second_year_day,second_year_cls = ([] for lis in range(3))
third_year,third_year_day,third_year_cls = ([] for lis in range(3))

def class_alloter():
	subjects = [["AH1","AH2","G1","G2","C1","C2"],["AH3","AH4","AH5","G3","G4","C3","C5","C4"],["AH6","AH7","G5","G6","AH8","C6"]]
	sub_lst = ["Env","English","Bangla"]
	
	for i in range(0,6):
		for j in range(0,7):
			count = 0

			if(balancer[i][j] is not None) and (balancer[i][j] in subjects[0]):
				cap_index = subjects[0].index(balancer[i][j])
				temp_allocate.update({balancer[i][j]:com_students[0][cap_index]})
			else:
				pass

			if(balancer_2[i][j] is not None) and (balancer_2[i][j] in subjects[1]):
				cap_index = subjects[1].index(balancer_2[i][j])
				temp_allocate.update({balancer_2[i][j]:com_students[1][cap_index]})
			else:
				pass

			if(balancer_3[i][j] is not None) and (balancer_3[i][j] not in sub_lst) and (balancer_3[i][j] in subjects[2]):
				cap_index = subjects[2].index(balancer_3[i][j])
				temp_allocate.update({balancer_3[i][j]:com_students[2][cap_index]})
			else:
				pass

			if(balancer_3[i][j] is not None) and (balancer_3[i][j] in sub_lst):
				cap_index = sub_lst.index(balancer_3[i][j])
				temp_allocate.update({balancer_3[i][j]:com_students[2][cap_index]})
			else:
				pass

			b = sorted(temp_allocate, key=temp_allocate.__getitem__,reverse=True)
		
			for k in b:
				if k in subjects[0]:
					first_year.append(k)
					first_year_day.extend([[i,j]])
					first_year_cls.append(com_cls_room[count])
				elif k in subjects[1]:
					second_year.append(k)
					second_year_day.extend([[i,j]])
					second_year_cls.append(com_cls_room[count])
				elif k in subjects[2]:
					third_year.append(k)
					third_year_day.extend([[i,j]])
					third_year_cls.append(com_cls_room[count])
				elif k in sub_lst:
					third_year.append(k)
					third_year_day.extend([[i,j]])
					third_year_cls.append(com_cls_room[count])
				count+=1

			temp_allocate.clear()
			
			del b[:]

class_alloter()

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
slots = ['Days/Slots','12:00 - 01:00','01:00 - 02:00','02:00 - 03:00','03:00 - 04:00','04:00 - 05:00','05:00 - 06:00','06:00 - 07:00']

for i in range(0,6):
	balancer[i].insert(0,days[i])
	balancer_2[i].insert(0,days[i])
	balancer_3[i].insert(0,days[i])

balancer.insert(0,slots)
balancer_2.insert(0,slots)
balancer_3.insert(0,slots)

allots = [first_year_day,second_year_day,third_year_day]
allots_cls = [first_year_cls,second_year_cls,third_year_cls]
allots_subj = [first_year,second_year,third_year]

def texter(allots, allots_cls,allots_subj):
	text = days[allots[0]] + " --> " +str(allots[1]+1) + " --> " +str(allots_cls) + " -- > "+ str(allots_subj) +"\r\n"
	return text

files = ["Year_1_Commerce","Year_2_Commerce","Year_3_Commerce"]
for i in range(0,3):
	file_name = str(files[i]) + ".txt"
	fi = open(file_name,"w")
	text = "DAY --> PERIOD --> CLASS --> Subjet\r\n"
	fi.write(text)
	for k in range(0,len(allots[i])):
		text = texter(allots[i][k],allots_cls[i][k],allots_subj[i][k])
		fi.write(text)
	fi.close()

doc1 = SimpleDocTemplate("Commerce_Year_1.pdf", pagesize=letter)
doc2 = SimpleDocTemplate("Commerce_Year_2.pdf", pagesize=letter)
doc3 = SimpleDocTemplate("Commerce_Year_3.pdf", pagesize=letter)

elements = []
p1 = Table(balancer,8*[1.0*inch], 7*[0.4*inch])
p2 = Table(balancer_2,8*[1.0*inch], 7*[0.4*inch])
p3 = Table(balancer_3,8*[1.0*inch], 7*[0.4*inch])

tabs = [p1,p2,p3]
docs = [doc1,doc2,doc3]

for i in range(0,len(tabs)):

	tabs[i].setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),
                       ('TEXTCOLOR',(1,1),(-1,-1),colors.red),
                       ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('TEXTCOLOR',(0,0),(0,0),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
	elements.append(tabs[i])
	docs[i].build(elements)