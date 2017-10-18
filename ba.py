import random
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

balancer, balancer_2, balancer_3 = ([] for i in range(3))

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_2.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_3.append(l)

ba_hns_students,ba_gen_students = ([] for lis in range(2))

ba_hns_gp_a = ['bengali','santhali','history','economics']
ba_hns_gp_b = ['polsc','music','english','geography','education']
ba_hns_gp_c = ['philosophy','sanskrit']
hns_subs = ba_hns_gp_a+ba_hns_gp_b+ba_hns_gp_c

ba_gen_gp_a = ['bengali','santhali','history','economics']
ba_gen_gp_b = ['polsc','music','english','geography','education']
ba_gen_gp_c = ['philosophy','sanskrit','phyedu','maths']
gen_subs = ba_gen_gp_a+ba_gen_gp_b+ba_gen_gp_c

ba_cls_room = ['vs106','vs107','vs203','vs205','vs206','vs207','vs301','vs302','vs303','vs304','vs305','vs306','vs307','vs308','vs309','vs310','vs311','vs312']

ba_cls_capa = [170,170,100,100,170,170,30,40,30,100,100,50,50,100,40,100,100,50]
'''
for k in range(3):
	print "Enter Details For Year ",k+1," Students :-"
	lis = []
	for i in range(0, len(hns_subs)):
		inp =  int(input("Enter Total in "+hns_subs[i]+" Honours Course : "))
		lis.append(inp)
	ba_hns_students.append(lis)

for k in range(3):
	print "Enter Details For Year ",k+1," Students :-"
	lis = []
	for i in range(0, len(gen_subs)):
		inp =  int(input("Enter Total in "+gen_subs[i]+" Pass Course : "))
		lis.append(inp)
	ba_gen_students.append(lis)
'''

ba_hns_students = [[70,22,42,75,16,63,49,38,67,172,85], [54,85,172,67,8,49,63,160,75,42,38], [60,22,32,65,14,53,49,48,67,100,75]]

ba_gen_students = [[64,76,82,57,9,45,16,35,29,24,33,60,52],[57,82,76,64,25,52,60,33,24,29,3,42,95],[52,60,33,24,29,35,16,45,19,57,82,76,64]]

#year_3_x_capa = 160

allotment, alloted_cls, alloted_subjects = ([] for lists in range(3))
allotment_2, alloted_cls_2, alloted_subjects_2 = ([] for lists in range(3))
allotment_3, alloted_cls_3, alloted_subjects_3 = ([] for lists in range(3))

def count_tester(lister, load):
	GPS = ['A','B','C']
	GPS_counter = []
	storer = []

	for i in range(0,len(load)):
		lsi = []
		gp = load[i]
		if gp == "A/B" or gp == "B/C" or gp == "A/C":
			lsi = gp.split('/')
			storer.append(lsi[0])
			storer.append(lsi[1])
		else:
			storer.append(gp)

	for i in range(0,3):
		count = [x for x in load if x == GPS[i]]
		GPS_counter.append(len(count))


	if GPS_counter[0] >= 2:
		if 'A' in lister:
			lister.remove('A')
		if 'A/B' in lister:
			lister.remove('A/B')
		if 'A/C' in lister:
			lister.remove('A/C')
	if GPS_counter[1] >= 2:
		if 'B' in lister:
			lister.remove('B')
		if 'A/B' in lister:
			lister.remove('A/B')
		if 'B/C' in lister:
			lister.remove('B/C')
	if GPS_counter[2] >= 2:
		if 'C' in lister:
			lister.remove('C')
		if 'A/C' in lister:
			lister.remove('A/C')
		if 'B/C' in lister:
			lister.remove('B/C')

def group_tester(row, col, lister, gp, load):
	pull = False
	copy = gp
	rem_lis = ["A/B","B/C","A/C"]
	if gp == "A/B" or gp == "B/C" or gp == "A/C":
		gp_lsi = gp.split("/")
		pull = True
	else:
		gp_lsi = gp

	lister = count_tester(lister, load[row])
	if lister:
		for k in range(0,len(gp_lsi)):
			if gp_lsi[k] in load[row]:
				index = len(load[row]) - 1 - load[row][::-1].index(gp_lsi[k])
				#index = load[row].index(gp_lsi[k])
				diffe = col - index
				if diffe > 1 and gp_lsi[k] in lister:
					if pull == True:
						lister = [x for x in rem_lis if x not in lister]
					else:
						lister.remove(gp_lsi[k])
				
				if lister:
					gp = random.choice(lister)
				else:
					gp = copy
	return gp

def balancer_tester(val,load):
	emp_lis,gps = ([] for lis in range(2))
	tester = ['A/B','A/C','B/C']
	l = len(load)
	try:
		for i in range(0,l):
			if load[i] in tester:
				gps = load[i].split('/')
			else:
				gps = load[i]
			if val in gps:
				emp_lis.append(load[i])
				del load[i]
	except:
		pass

	#emp_lis = list(set().union(emp_lis,load))
	emp_lis = emp_lis + load
	return emp_lis

def balancer_check():
	lister = ['A','B','C','A/B','A/C','B/C']
	opts = ['a','b','c']

	for rows in range(0,6):
		count_m = len([x for x in balancer[rows] if x in lister])
		count_o = len([x for x in balancer[rows] if x in opts])
		if count_m > count_o:
			if count_o == 1:
				val = [x for x in balancer[rows] if x in opts]
				index = balancer[rows].index(val[0])
				del balancer[rows][index]
				balancer[rows] = balancer_tester(val[0].upper(),balancer[rows])
				balancer[rows].append(val[0])
			else:
				pass
		else:
			pass

def honours_selector(gp_a, gp_b, gp_c):
	counter_A = 0
	counter_B = 0
	counter_C = 0

	for rows in range(0,5):
		for cols in range(0,6):

			lister = ['A','B','C','A/C','B/C','A/B']
			random.shuffle(lister)
			if counter_A >= 10 or counter_C >= 10 and 'A/C' in lister:
				lister.remove('A/C')
			if counter_A >= 10 or counter_B >= 10 and 'A/B' in lister:
				lister.remove('A/B')
			if counter_B >= 10 or counter_C >= 10 and 'B/C' in lister:
				lister.remove('B/C')
			
			if counter_A >= 10 and 'A' in lister:
					lister.remove('A')
			if counter_B >= 10 and 'B' in lister:
					lister.remove('B')
			if counter_C >= 10 and 'C' in lister:
				lister.remove('C')

			if lister:
				gp = random.choice(lister)
				gp = group_tester(rows, cols, lister, gp, balancer)

				if gp == "A":
					counter_A += 1
				elif gp == "B":
					counter_B += 1
				elif gp == "C":
					counter_C += 1
				if gp == "A/C":
					counter_A += 1
					counter_C += 1
				elif gp == "B/C":
					counter_B += 1
					counter_C += 1
				elif gp == "A/B":
					counter_A += 1
					counter_B += 1
				balancer[rows][cols] = gp

			else:
				break

def pass_selector():
	counter_a = 0
	counter_b = 0
	counter_c = 0

	lister = ['a','b','c']
	random.shuffle(lister)

	balancer[0][6] = lister[0]
	balancer[1][6] = lister[1]
	balancer[2][6] = lister[2]
	
	counter_a += 1
	counter_b += 1
	counter_c += 1

	for rows in range(3,5):
		for cols in range(0,7):
			
			lister = ['a','b','c']

			if counter_a >= 3 and 'a' in lister:
				lister.remove('a')
			if counter_b >= 3 and 'b' in lister:
				lister.remove('b')
			if counter_c >= 3 and 'c' in lister:
				lister.remove('c')

			if balancer[rows][cols] == None:
				if lister:
					gp = random.choice(lister)
					if gp == 'a':
						counter_a += 1
					elif gp == 'b':
						counter_b += 1
					elif gp == 'c':
						counter_c += 1
					balancer[rows][cols] = gp
				else:
					pass

def pass_selector_2():
	counter_a = 0
	counter_b = 0
	counter_c = 0

	for cols in range(0,7):
		if balancer_2[4][cols] == None:
			balancer_2[4][cols] = 'a/b/c'
			counter_a += 1
			counter_b += 1
			counter_c += 1

	for cols in range(0,4):
		if counter_a < 6 or counter_b < 6 or counter_c < 6:
			balancer_2[5][cols] = 'a/b/c'
			counter_a += 1
			counter_b += 1
			counter_c += 1


def honours_selector_2(gp_a, gp_b, gp_c):
	counter_A = 0
	counter_B = 0
	counter_C = 0

	for rows in range(0,5):
		for cols in range(0,7):

			lister = ['A','B','C','A/C','B/C','A/B']
			if counter_A >= 15 or counter_C >= 15 and 'A/C' in lister:
				lister.remove('A/C')
			if counter_A >= 15 or counter_B >= 15 and 'A/B' in lister:
				lister.remove('A/B')
			if counter_B >= 15 or counter_C >= 15 and 'B/C' in lister:
				lister.remove('B/C')
			
			if counter_A >= 15 and 'A' in lister:
					lister.remove('A')
			if counter_B >= 15 and 'B' in lister:
					lister.remove('B')
			if counter_C >= 15 and 'C' in lister:
				lister.remove('C')

			if lister:
				gp = random.choice(lister)
				tmp = balancer[rows][cols]
				if tmp == 'A/C' or tmp == 'A/B' or tmp == "B/C":
					temp_lis = lister
					if 'A/C' in lister:
						lister.remove('A/C')
					if 'A/B' in lister:
						lister.remove('A/B')
					if 'B/C' in lister:
						lister.remove('B/C')
					if temp_lis:
						gp = group_tester(rows, cols, temp_lis, gp, balancer_2)
					else:
						gp = group_tester(rows, cols, lister, gp, balancer_2)

				if gp == "A":
					counter_A += 1
				elif gp == "B":
					counter_B += 1
				elif gp == "C":
					counter_C += 1
				if gp == "A/C":
					counter_A += 1
					counter_C += 1
				elif gp == "B/C":
					counter_B += 1
					counter_C += 1
				elif gp == "A/B":
					counter_A += 1
					counter_B += 1
				elif gp == 'A/B/C':
					counter_A += 1
					counter_B += 1
					counter_C += 1
				balancer_2[rows][cols] = gp
			else:
				break

def honours_selector_3(gp_a, gp_b, gp_c):
	counter_A = 0
	counter_B = 0
	counter_C = 0

	lister = ['A','B','A','B']
	random.shuffle(lister)
	balancer_3[0][0] = lister[0]
	balancer_3[0][1] = lister[1]
	balancer_3[0][2] = lister[2]
	balancer_3[0][3] = lister[3]
	balancer_3[0][4] = "C"
	balancer_3[0][5] = "C"
	balancer_3[0][6] = "C"

	counter_A += 2
	counter_B += 2
	counter_C += 3	

	for rows in range(1,6):
		for cols in range(0,7):

			lister = ['A','B','C','A/C','B/C','A/B']
			if counter_A >= 13 or counter_C >= 12 and 'A/C' in lister:
				lister.remove('A/C')
			if counter_A >= 13 or counter_B >= 13 and 'A/B' in lister:
				lister.remove('A/B')
			if counter_B >= 13 or counter_C >= 12 and 'B/C' in lister:
				lister.remove('B/C')
			
			if counter_A >= 13 and 'A' in lister:
					lister.remove('A')
			if counter_B >= 13 and 'B' in lister:
					lister.remove('B')
			if counter_C >= 12 and 'C' in lister:
				lister.remove('C')

			if lister:
				gp = random.choice(lister)
				tmp = balancer[rows][cols]
				tmp1 = balancer_2[rows][cols]
				temp_lis = lister
				if tmp == 'A/C' or tmp == 'A/B' or tmp == 'B/C':
					temp_lis.remove('A/C')
					temp_lis.remove('A/B')
					temp_lis.remove('B/C')
				if (tmp and tmp1) == ('A' or 'B' or 'C') and tmp in temp_lis and tmp1 in temp_lis:
					temp_lis.remove('A')
					temp_lis.remove('B')
					temp_lis.remove('C')
				if temp_lis:
					gp = group_tester(rows, cols, temp_lis, gp, balancer_3)
				else:
					gp = group_tester(rows, cols, lister, gp, balancer_3)

				if gp == "A":
					counter_A += 1
				elif gp == "B":
					counter_B += 1
				elif gp == "C":
					counter_C += 1
				if gp == "A/C":
					counter_A += 1
					counter_C += 1
				elif gp == "B/C":
					counter_B += 1
					counter_C += 1
				elif gp == "A/B":
					counter_A += 1
					counter_B += 1
				elif gp == 'A/B/C':
					counter_A += 1
					counter_B += 1
					counter_C += 1
				if gp:
					balancer_3[rows][cols] = gp
			else:
				break

def compulsary_setter():
	i = 0
	p = 4
	cset = ['ENV','ENG','B1','B2']
	random.shuffle(cset)  
	for cols in range(0,p):
		if balancer_3[5][cols] == None:
			balancer_3[5][cols] = cset[i]
			i += 1 
		else:
			p = 5

honours_selector(ba_hns_gp_a, ba_hns_gp_b, ba_hns_gp_c)
pass_selector()
honours_selector_2(ba_hns_gp_a, ba_hns_gp_b, ba_hns_gp_c)
pass_selector_2()
honours_selector_3(ba_hns_gp_a, ba_hns_gp_b, ba_hns_gp_c)
compulsary_setter()

def selector(i, j, year, students):
	if year == 1:
		load = balancer
	elif year == 2:
		load  = balancer_2
	elif year == 3:
		load = balancer_3

	if load[i][j] == 'A':
		subjects = ba_hns_gp_a
		capacity = students[0:4]
	elif load[i][j] == 'B':
		subjects = ba_hns_gp_b
		capacity = students[4:9]
	elif load[i][j] == 'C':
		subjects = ba_hns_gp_c
		capacity = students[9:]
	elif load[i][j] == 'A/B':
		subjects = ba_hns_gp_a + ba_hns_gp_b
		capacity = students[0:9]
	elif load[i][j] == 'B/C':
		subjects = ba_hns_gp_b + ba_hns_gp_c
		capacity = students[4:]
	elif load[i][j] == 'A/C':
		subjects = ba_hns_gp_a + ba_hns_gp_c
		capacity = students[0:4] + students[9:]
	'''
	elif load[i][j] == 'E' or load[i][j] == 'B1' or load[i][j] == 'B2':
		subjects = [load[i][j]]
		capacity = [year_3_x_capa]
	'''

	return subjects, capacity

def allotment_tester(i, j, capacity, subjects, rooms, classes, year):
	if capacity != None and subjects != None:
		
		if year == 1:
			alcls = alloted_cls
			almnt = allotment
			alsub = alloted_subjects
		elif year == 2:
			alcls = alloted_cls_2
			almnt = allotment_2
			alsub = alloted_subjects_2
		elif year == 3:
			alcls = alloted_cls_3
			almnt = allotment_3
			alsub = alloted_subjects_3

		rooms = list(rooms)
		classes = list(classes)
		
		zippd = zip(capacity, subjects)
		zippd.sort()
		capacity, subjects = zip(*zippd)
		for k in range(0,len(capacity)):
			try:
				alloted = min(rooms, key=lambda z:abs(capacity[k] - z))
			except:
				alloted = None
			if alloted is not None:
				index = rooms.index(alloted)
				alcls.append(classes[index])
				almnt.extend([[i,j]])
				alsub.append(subjects[k])
				del rooms[index]
				del classes[index]
			else:
				break
	return rooms,classes

def class_alloter(ba_cls_room, ba_cls_capa, students_hns, students_gen):
	optes_1 = ['a','b','c']
	hnses_1 = ['A','B','C','A/B','B/C','A/C']
	
	optes_2 = ['a/b/c']
	hnses_2 = ['A','B','C','A/C','B/C','A/B']

	hnses_3 = ['A','B','C','A/C','B/C','A/B']
	comp_3 = ['ENV','B1','B2']

	classes, rooms = ([] for lists in range(2))

	for j in range(0,7):
		for i in range(0,6):

			rooms = ba_cls_capa[:]
			classes = ba_cls_room[:]
			
			if balancer[i][j] in optes_1:
				if balancer[i][j] == 'a':
					subjects = ba_gen_gp_a
					capacity = students_gen[0][0:4]
				elif balancer[i][j] == 'b':
					subjects = ba_gen_gp_b
					capacity = students_gen[0][4:9]
				elif balancer[i][j] == 'c':
					subjects = ba_gen_gp_c
					capacity = students_gen[0][9:]
			
			elif balancer[i][j] in hnses_1:
				subjects, capacity = selector(i, j, 1, students_hns[0])
			
			elif balancer[i][j] == None:
				subjects = None
				capacity = None

			rooms, classes = allotment_tester(i, j, capacity, subjects, rooms, classes, 1)

			if balancer_2[i][j] in optes_2:
				if balancer_2[i][j] == 'a/b/c':
					subjects = ba_gen_gp_a + ba_gen_gp_b + ba_gen_gp_c
					capacity = students_gen[1][0:]
			
			elif balancer_2[i][j] in hnses_2:
				subjects, capacity = selector(i, j, 2, students_hns[1])
			
			elif balancer_2[i][j] == None:
				subjects = None
				capacity = None

			rooms, classes = allotment_tester(i, j, capacity, subjects, rooms, classes, 2)
			
			if balancer_3[i][j] in comp_3:
				alloted_cls_3.append("ALL")
				allotment_3.extend([[i,j]])
				alloted_subjects_3.append(balancer_3[i][j])
			else:
				if balancer_3[i][j] in hnses_3:
					subjects, capacity = selector(i, j, 3, students_hns[2])
			
				elif balancer_3[i][j] == None:
					subjects = None
					capacity = None

				rooms, classes = allotment_tester(i, j, capacity, subjects, rooms, classes, 3)


balancer_check()	
class_alloter(ba_cls_room, ba_cls_capa, ba_hns_students, ba_gen_students)
'''
for i in range(0,6):
	print i," -> ",balancer[i]
print "--"*70
for i in range(0,6):
	print i," -> ",balancer_2[i]
print "--"*70
for i in range(0,6):
	print i," -> ",balancer_2[i]
'''

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
slots = ['Days/Slots','10:00 - 11:00','11:00 - 12:00','12:00 - 1:00','1:00 - 2:00','2:00 - 3:00','3:00 - 4:00','4:00 - 5:00']


for i in range(0,6):
	balancer[i].insert(0,days[i])
	balancer_2[i].insert(0,days[i])
	balancer_3[i].insert(0,days[i])

balancer.insert(0,slots)
balancer_2.insert(0,slots)
balancer_3.insert(0,slots)

doc1 = SimpleDocTemplate("ba_1.pdf", pagesize=letter)
doc2 = SimpleDocTemplate("ba_2.pdf", pagesize=letter)
doc3 = SimpleDocTemplate("ba_3.pdf", pagesize=letter)

elements = []
t1 = Table(balancer,8*[1.0*inch], 7*[0.4*inch])
t2 = Table(balancer_2,8*[1.0*inch], 7*[0.4*inch])
t3 = Table(balancer_3,8*[1.0*inch], 7*[0.4*inch])

tabs = [t1,t2,t3]
docs = [doc1,doc2,doc3]

for i in range(3):

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

def texter(allots, allots_cls,allots_subj):
	text = days[allots[0]] + " --> " +str(allots[1]+1) + " --> " +str(allots_cls) + " -- > "+ str(allots_subj) +"\r\n"
	return text

allots = [allotment,allotment_2,allotment_3,]
allots_cls = [alloted_cls,alloted_cls_2,alloted_cls_3]
allots_subj = [alloted_subjects,alloted_subjects_2,alloted_subjects_3]

files = ["Year_1_Arts","Year_2_Arts","Year_3_Arts"]
for i in range(0,3):
	file_name = str(files[i]) + ".txt"
	fi = open(file_name,"w")
	text = "DAY --> PERIOD --> CLASS --> Subjet\r\n"
	fi.write(text)
	for k in range(0,len(allots[i])):
		text = texter(allots[i][k],allots_cls[i][k],allots_subj[i][k])
		fi.write(text)
	fi.close()
#'''