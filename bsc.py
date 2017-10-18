import re, random
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

balancer_pure, balancer_pure_2, balancer_pure_3 = ([] for lis in range(3))
balancer_bio, balancer_bio_2, balancer_bio_3 = ([] for lis in range(3))
balancer_cs, balancer_cs_2, balancer_cs_3 = ([] for lis in range(3))
balancer_pass_pure, balancer_pass_pure_2, balancer_pass_pure_3 = ([] for lis in range(3))
balancer_pass_bio, balancer_pass_bio_2, balancer_pass_bio_3 = ([] for lis in range(3))

allotment_pure, alloted_cls_pure, alloted_subjects_pure = ([] for lists in range(3))
allotment_pure_2, alloted_cls_pure_2, alloted_subjects_pure_2 = ([] for lists in range(3))
allotment_pure_3, alloted_cls_pure_3, alloted_subjects_pure_3 = ([] for lists in range(3))

allotment_bio, alloted_cls_bio, alloted_subjects_bio = ([] for lists in range(3))
allotment_bio_2, alloted_cls_bio_2, alloted_subjects_bio_2 = ([] for lists in range(3))
allotment_bio_3, alloted_cls_bio_3, alloted_subjects_bio_3 = ([] for lists in range(3))

allotment_cs, alloted_cls_cs, alloted_subjects_cs = ([] for lists in range(3))
allotment_cs_2, alloted_cls_cs_2, alloted_subjects_cs_2 = ([] for lists in range(3))
allotment_cs_3, alloted_cls_cs_3, alloted_subjects_cs_3 = ([] for lists in range(3))

allotment_pure_pass, alloted_cls_pure_pass, alloted_subjects_pure_pass = ([] for lists in range(3))
#allotment_pure_pass_2, alloted_cls_pure_pass_2, alloted_subjects_pure_pass_2 = ([] for lists in range(3))
#allotment_pure_pass_3, alloted_cls_pure_pass_3, alloted_subjects_pure_pass_3 = ([] for lists in range(3))

allotment_bio_pass, alloted_cls_bio_pass, alloted_subjects_bio_pass = ([] for lists in range(3))
#allotment_bio_pass_2, alloted_cls_bio_pass_2, alloted_subjects_bio_pass_2 = ([] for lists in range(3))
#allotment_bio_pass_3, alloted_cls_bio_pass_3, alloted_subjects_bio_pass_3 = ([] for lists in range(3))

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_pure.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_pure_2.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_pure_3.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_bio.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_bio_2.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_bio_3.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_cs.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_cs_2.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_cs_3.append(l)

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_pass_pure.append(l)
'''
for i in range(0,6):
	l = [None for _ in range(3)]
	balancer_pass_pure_2.append(l)

for i in range(0,6):
	l = [None for _ in range(3)]
	balancer_pass_pure_3.append(l)
'''

for i in range(0,6):
	l = [None for _ in range(7)]
	balancer_pass_bio.append(l)
'''
for i in range(0,6):
	l = [None for _ in range(3)]
	balancer_pass_bio_2.append(l)

for i in range(0,6):
	l = [None for _ in range(3)]
	balancer_pass_bio_3.append(l)
'''

bsc_cls_room = ["RN 301","RN 302","RN 303","RN 304","RN 305","RN 306","RN 209","RN 210","RN 106","RN 107","JC 102","JC 103","JC 301","JC 302","JC 303"]
bsc_cls_capa = [180,120,120,110,110,190,100,100,100,100,100,100,100,100,100]
cs_cls_room = ["PC 301(B)", "PC 302(C)", "LAB X"]
cs_cls_capa = [50,50,50]

pass_pure_capa, pass_bio_capa, pure_capa, bio_capa, cs_capa = ([] for lis in range(5))

pure_subj = ["Physics","Chemistry","Maths"]
bio_subj = ["Zoology","Botany","Physiology","Micro-Biology","Bio-Technology"]
'''
print "Enter Details For Honours Course :-"
print "Enter Details For Pure Science :-"
for i in range(0,3):
	lis = []
	print "For Year ",i+1
	for k in range(0,3):
		inp = int(input("Enter Total Students In "+pure_subj[k]+ " :"))
		lis.append(inp)
	pure_capa.append(lis)

print "Enter Details For Bio Science :-"
for i in range(0,3):
	lis = []
	print "For Year ",i+1
	for k in range(0,5):
		inp = int(input("Enter Total Students In "+bio_subj[k]+ " :"))
		lis.append(inp)
	bio_capa.append(lis)

print "Enter Details For Computer Science :-"
for i in range(0,3):
	inp = int(input("Enter Total Students In Year "+str(i+1)+" :"))
	cs_capa.append(inp)
'''
	
'''
print "Enter Details For Pass Course :-"
print "Enter Details For Pure Science Pass Course :-"
for i in range(0,3):
	inp = input("Enter Total Students In Year "+str(i+1)+" :")
	pass_pure_capa.append(inp)

print "Enter Details For Bio Science Pass Course :-"
for i in range(0,3):
	inp = input("Enter Total Students In Year "+str(i+1)+" :")
	pass_bio_capa.append(inp)
'''

pure_capa = [[100,95,125],[130,110,85],[95,86,124]]

bio_capa = [[95,76,123,140,110],[110,76,123,95,86],[54,67,69,85,72]]

cs_capa = [28,35,40]

pass_pure_capa = [140,98,130]
pass_bio_capa = [98,87,100]
#'''

def selector_pure_2():
	counter_p3 = 0
	counter_p4 = 0
	counter_p5 = 0

	counter_phy = 0
	counter_che = 0
	counter_math = 0
	
	hns_ppr = ["HNS 3","HNS 4"]
	pass_ppr = ["P2"]
	lister = ["Pass 2(Phy)","Pass 2(Che)","Pass (Math)"]

	for rows in range(0,5):
		if rows <= 3:
			for cols in range(0,2):
				balancer_pure_2[rows][cols] = "P3 Lab"+"\r\n"+"H5 Lab"

		elif rows == 4:
			for cols in range(0,2):
				balancer_pure_2[rows][cols] = "P3 Lab"


		for rows in range(0,4):
			if rows <= 2:
				balancer_pure_2[rows][2] = "H5 LAB "+"(P+C)"
			else:
				balancer_pure_2[rows][2] = "H5 LAB (P)"


	for rows in range(0,4):
		for cols in range(3,6):

			if counter_p3 >= 6 and 'HNS 3' in hns_ppr:
				hns_ppr.remove('HNS 3')
			if counter_p4 >= 6 and 'HNS 4' in hns_ppr:
				hns_ppr.remove('HNS 4')

			if hns_ppr:
				gp = random.choice(hns_ppr)
				if gp == 'HNS 3':
					counter_p3 += 1
				elif gp == 'HNS 4':
					counter_p4 += 1
				balancer_pure_2[rows][cols] = gp
			else:
				break

	for rows in range(0,5):
		for cols in range(0,7):

			if counter_phy >= 3 and 'Pass 2(Phy)' in lister:
				lister.remove('Pass 2(Phy)')
			if counter_che >= 3 and 'Pass 2(Che)' in lister:
				lister.remove('Pass 2(Che)')
			if counter_math >= 3 and 'Pass (Math)' in lister:
				lister.remove('Pass (Math)')
			
			if balancer_pure_2[rows][cols] == None:
				if lister:
					gp = random.choice(lister)

					if gp == 'Pass 2(Phy)':
						counter_phy += 1
					elif gp == 'Pass 2(Che)':
						counter_che += 1
					elif gp == 'Pass (Math)':
						counter_math += 1

					balancer_pure_2[rows][cols] = gp
				else:
					break

	for cols in range(0,3):
		balancer_pure_2[5][cols] = "Pass (Math)"


def selector_pure_3():
	counter_p6 = 0
	counter_p7 = 0

	hns_ppr = ["HNS 6","HNS 7"]

	for rows in range(0,3):
		for cols in range(0,2):
			balancer_pure_3[rows][cols] = "HNS 6"
			counter_p6 += 1
	for cols in range(0,3):
		balancer_pure_3[3][cols] = "Pass 4(Math)"
		#counter_p7 += 1

	for cols in range(0,3):
		balancer_pure_3[4][cols] = "HNS 7(Math)"
		counter_p7 += 1

	for cols in range(0,4):
		balancer_pure_3[5][cols] = "PASS 4"

	for rows in range(0,3):
		balancer_pure_3[rows][2] = "HNS 7 M/C"

	for rows in range(0,4):
		for cols in range(3,6):
			if rows == 0:
				balancer_pure_3[rows][cols] = "Phy7/8"+"\r\n"+"Che 4(L)"
			elif rows == 1:
				balancer_pure_3[rows][cols] = "PHY7/8"+"\r\n"+"Che 8"+"+"+"Phy 4(L)"
				balancer_pure_3[rows][cols+1] = "Che 8"
			elif rows == 2:
				balancer_pure_3[rows][cols] = "P7/8 +"+"\r\n"+"M8c"+" + "+"CHE 8"
				balancer_pure_3[rows][cols+1] = "M8c + Che 8"
			else:
				balancer_pure_3[rows][cols] = "PHY 7/8"

	for cols in range(3,7):
		if balancer_pure_3[rows][cols] == None:
			balancer_pure_3[3][cols] = "M8 + Che 8"
		else:
			balancer_pure_3[3][cols] = balancer_pure_3[3][cols] + "\r\n+M8 + Che 8"
	'''

	for cols in range(0,2):
		balancer_pure_3[0][cols] = "PASS 4"

	for cols in range(3,7):
		if cols > 4:
			balancer_pure_3[0][cols] = "LAB4 (Math)"
		else:
			balancer_pure_3[0][cols] = "LAB4"

	for cols in range(0,7):
		if cols >= 3:
			balancer_pure_3[1][cols] = "PHY7/Math8c"
		else:
			balancer_pure_3[1][cols] = "LAB Chem 8"


	for rows in range(2,4):
		for cols in range(0,7):

			if counter_p6 >= 6 and 'HNS 6' in hns_ppr:
				hns_ppr.remove('HNS 6')
			if counter_p7 >= 6 and 'HNS 7' in hns_ppr:
				hns_ppr.remove('HNS 7')
			if hns_ppr:
				gp = random.choice(hns_ppr)
				if gp == 'HNS 6':
					counter_p6 += 1
				if gp == 'HNS 7':
					if counter_p7 >= 3:
						gp = 'HNS 7(P/M)'
					counter_p7 += 1
				balancer_pure_3[rows][cols] = gp
			else:
				break
	
	balancer_pure_3[3][5] = balancer_pure_3[3][6] = "HNS 6(PHY)"

	for cols in range(0,4):
		balancer_pure_3[4][cols] = "PHY8/Math8"
	'''

	balancer_pure_3[4][4] = "English"
	balancer_pure_3[4][5] = "Bangla"
	balancer_pure_3[4][6] = "ENV"


def selector_bio_2():

	counter_p3 = 0
	counter_p4 = 0
	counter_p5 = 0

	counter_z = 0
	counter_p = 0
	counter_b = 0
	counter_m = 0


	hns_ppr = ["HNS 3","HNS 4"]
	lister = ["Pass 2(Z)","Pass 2(P)","Pass 2(B)"]

	for rows in range(0,4):
		for cols in range(0,3):
			if cols <= 1:
				balancer_bio_2[rows][cols] = "HNS 5 LAB" + "\r\n" + "LAB 3"
			else:
				balancer_bio_2[rows][cols] = "HNS 5 LAB"

	for cols in range(0,2):
		balancer_bio_2[4][cols] = "LAB 3"
	'''
	for cols in range(0,3):
		if cols <= 1:
			balancer_bio_2[0][cols] = "HNS 5 LAB" + "\r\n" + "LAB 3"
		else:
			balancer_bio_2[0][cols] = "HNS 5 LAB"
	'''
	
	for rows in range(0,3):
		for cols in range(4,6):
			gp = random.choice(hns_ppr)
			if gp == 'HNS 3':
				counter_p3 += 1
			elif gp == 'HNS 4':
				counter_p4 += 1
			balancer_bio_2[rows][cols] = gp
					
	for rows in range(3,4):
		#if rows % 2 == 0:
		for cols in range(3,6):

			if counter_p3 >= 6 and 'HNS 3' in hns_ppr:
				hns_ppr.remove('HNS 3')
			if counter_p4 >= 6 and 'HNS 4' in hns_ppr:
				hns_ppr.remove('HNS 4')

			if hns_ppr:
				gp = random.choice(hns_ppr)
				if gp == 'HNS 3':
					counter_p3 += 1
				elif gp == 'HNS 4':
					counter_p4 += 1
				balancer_bio_2[rows][cols] = gp
			else:
				break

	for rows in range(0,5):
		for cols in range(0,7):
			if balancer_pure_2[rows][cols] == "Pass 2(Che)":
				balancer_bio_2[rows][cols] = "Pass 2(che/cmp)"


	for cols in range(0,3):

		if counter_p3 >= 6 and 'HNS 3' in hns_ppr:
			hns_ppr.remove('HNS 3')
		if counter_p4 >= 6 and 'HNS 4' in hns_ppr:
			hns_ppr.remove('HNS 4')

		if hns_ppr:
			gp = random.choice(hns_ppr)
			if gp == 'HNS 3':
				counter_p3 += 1
			elif gp == 'HNS 4':
				counter_p4 += 1
			balancer_bio_2[5][cols] = gp
		else:
			break

	for rows in range(0,5):
		for cols in range(0,7):

			if counter_z >= 3 and 'Pass 2(Z)' in lister:
				lister.remove('Pass 2(Z)')
			if counter_b >= 3 and 'Pass 2(B)' in lister:
				lister.remove('Pass 2(B)')
			if counter_p >= 3 and 'Pass 2(P)' in lister:
				lister.remove('Pass 2(P)')
			
			if balancer_bio_2[rows][cols] == None:
				if lister:
					gp = random.choice(lister)

					if gp == 'Pass 2(Z)':
						counter_z += 1
					elif gp == 'Pass 2(P)':
						counter_p += 1
					elif gp == 'Pass 2(B)':
						counter_b += 1

					balancer_bio_2[rows][cols] = gp
				else:
					break

	
def selector_bio_3():
	counter_p6 = 0
	counter_lb = 0

	cmp_subs = ["English","Bangla","ENV"]

	for rows in range(0,5):
		if rows == 4:
			for cols in range(3,5):
				balancer_bio_3[rows][cols] = "Lab 4 Pass"
		else:
			for cols in range(3,6):
				if cols > 4:
					balancer_bio_3[rows][cols] = "Lab 7/8"
				else:
					balancer_bio_3[rows][cols] = "Lab 7/8\r\nLab 4 Pass"

	for rows in range(0,5):
		for cols in range(0,7):
			if balancer_bio_3[rows][cols] == None and counter_lb < 10:
				balancer_bio_3[rows][cols] = "Pass 4"
				counter_lb += 1

	for rows in range(3,5):
		for cols in range(0,6):
			if balancer_bio_3[rows][cols] == None and counter_p6 < 6:
				balancer_bio_3[rows][cols] = "HNS 6"
				counter_p6 += 1


	random.shuffle(cmp_subs)
	balancer_bio_3[5][0] = cmp_subs[0]
	balancer_bio_3[5][1] = cmp_subs[1]
	balancer_bio_3[5][2] = cmp_subs[2]

def selector_cs():
	counter_pp1 = 0
	counter_pp2 = 0

	lister = ["PAPER I","PAPER II"]
	lab_lister = ["Lab I/GEC(L)","Lab II/GEC(L)"]

	random.shuffle(lister)

	for rows in range(0,4):
		for cols in range(1,4):

			if counter_pp1 >= 5 and 'PAPER I' in lister:
				lister.remove('PAPER I')
			if counter_pp2 >= 5 and 'PAPER II' in lister:
				lister.remove('PAPER II')


			if lister:
				gp = random.choice(lister)
				if gp == 'PAPER I':
					counter_pp1 += 1
				elif gp == 'PAPER II':
					counter_pp2 += 1
				balancer_cs[rows][cols] = gp
				balancer_bio[rows][cols] = gp
				balancer_pure[rows][cols] = gp
			else:
				break


	balancer_pure[2][0] = "GEC (MATH)"
	balancer_pure[3][0] = "GEC (MATH)"
	balancer_pure[3][2] = "Paper II /Math/2"
	balancer_pure[3][3] = "Paper I /Math/2"
	


	for rows in range(0,4):
		if rows %2 == 0:
			for cols in range(5,7):
				balancer_cs[rows][cols] = lab_lister[0]
				balancer_bio[rows][cols] = lab_lister[0]
				balancer_pure[rows][cols] = lab_lister[0]
		else:
			for cols in range(5,7):
				balancer_cs[rows][cols] = lab_lister[1]
				balancer_bio[rows][cols] = lab_lister[1]
				balancer_pure[rows][cols] = lab_lister[1]

	for cols in range(0,3):
		if cols == 0:
			val = "GEC"
		else:
			val = "GEC"
		
		balancer_cs[5][cols] = val
		balancer_bio[5][cols] = val
		balancer_pure[5][cols] = val
	
	balancer_cs[4][0] = balancer_cs[4][1] = "AECC"
	balancer_cs[4][2] = "GEC"

	balancer_bio[4][0] = balancer_bio[4][1] = "AECC"
	balancer_bio[4][2] = "GEC"
	
	balancer_pure[4][0] = balancer_pure[4][1] = "AECC"
	balancer_pure[4][2] = "GEC"
	

def selector_cs_2():

	counter_p3 = 0
	counter_p4 = 0

	lister = ["III","IV"]

	balancer_cs_2[2][0] = balancer_cs_2[2][1]= "LAB V"

	for cols in range(0,2):
		balancer_cs_2[0][cols] = "LAB IIB"

	for cols in range(0,4):
		if cols < 2:
			balancer_cs_2[3][cols] = "LAB IIB"
		
	for cols in range(0,2):
		balancer_cs_2[4][cols] = "LAB III"

	for rows in range(0,4):
		for cols in range(2,4):

			if counter_p3 >= 6 and "III" in lister:
				lister.remove('III')
			if counter_p4 >= 6 and "IV" in lister:
				lister.remove('IV')

			if lister:
				if balancer_cs_2[rows][cols] is None:
					gp = random.choice(lister)
					if gp == 'III':
						counter_p3 += 1
					elif gp == "IV":
						counter_p4 += 1
					balancer_cs_2[rows][cols] = gp
			else:
				break

	for rows in range(0,4):
		if rows == 2:
			for cols in range(4,6):
				balancer_cs_2[rows][cols] = "LAB III"

		elif rows == 3:
			for cols in range(4,6):

				if counter_p3 >= 6 and "III" in lister:
					lister.remove('III')
				if counter_p4 >= 6 and "IV" in lister:
					lister.remove('IV')

				if lister:
					if balancer_cs_2[rows][cols] is None:
						gp = random.choice(lister)
						if gp == 'III':
							counter_p3 += 1
						elif gp == "IV":
							counter_p4 += 1
						balancer_cs_2[rows][cols] = gp
				else:
					break

		else:
			for cols in range(4,6):
				balancer_cs_2[rows][cols] = "LAB V"

	for cols in range(0,2):

		if counter_p3 >= 6 and "III" in lister:
			lister.remove('III')
		if counter_p4 >= 6 and "IV" in lister:
			lister.remove('IV')

		if lister:
			if balancer_cs_2[1][cols] is None:
				gp = random.choice(lister)
				if gp == 'III':
					counter_p3 += 1
				elif gp == "IV":
					counter_p4 += 1
				balancer_cs_2[1][cols] = gp
		else:
			break

	for rows in range(0,5):
		for cols in range(0,7):
			if balancer_pure_2[rows][cols] == "Pass 2(Phy)":
				balancer_cs_2[rows][cols] = "Pass 2(Phy)"
			elif balancer_pure_2[rows][cols] == "Pass 2(Che)":
				balancer_cs_2[rows][cols] = "Pass 2(Che)"
			elif balancer_pure_2[rows][cols] == "Pass (Math)":
				balancer_cs_2[rows][cols] = "Pass (Math)"

	for cols in range(0,3):
		balancer_cs_2[5][cols] = "Pass (Math)"


def selector_cs_3():
	counter_p6 = 0
	cmp_subs = ["English","Bangla","Env"]

	balancer_cs_3[0][0] = balancer_cs_3[0][1] = "Theory IV"

	balancer_cs_3[0][3] = balancer_cs_3[0][4]  = "LAB IV"

	balancer_cs_3[0][5] = balancer_cs_3[0][6]  = "LAB VII"


	for rows in range(1, 5):
		for cols in range(0,2):

			if counter_p6 < 6:
				balancer_cs_3[rows][cols] = "Theory VI"
				counter_p6 += 1
			else:
				break
	for rows in range(1,4):
		for cols in range(3,5):
			balancer_cs_3[rows][cols] = "LAB VIII"

	for cols in range(0,4):
		balancer_cs_3[4][cols] = "LAB VII"

	random.shuffle(cmp_subs)
	balancer_cs_3[5][0] = cmp_subs[0]
	balancer_cs_3[5][1] = cmp_subs[1]
	balancer_cs_3[5][2] = cmp_subs[2]

#argha

def pass_pure_selector():
	lister_counter = 0
	lister = ["Physics (PC)","Chemistry (PC)","Maths (PC)"]

	for rows in range(0,4):
		random.shuffle(lister)
		for cols in range(0,2):
			if lister_counter > 2:
				lister_counter = 0

			balancer_pass_pure[rows][cols] = lister[lister_counter]
			lister_counter += 1

		balancer_pass_pure[rows][4] = lister[lister_counter]
		lister_counter += 1
'''
def pass_pure_selector():
	counter_p1 = 0
	counter_p2 = 0
	counter_p3 = 0

	for rows in range(0,6):
		for cols in range(0,3):

			lister = ["Physics","Chem","Maths"]

			if counter_p1 >= 4 and 'Physics' in lister:
				lister.remove('Physics')
			if counter_p2 >= 4 and 'Chem/Comp' in lister:
				lister.remove('Chem')
			if counter_p3 >= 4 and 'Maths' in lister:
				lister.remove('Maths')

			if lister:
				gp = random.choice(lister)
				if gp == 'Physics':
					counter_p1 += 1
				elif gp == 'Chem':
					counter_p2 += 1
				elif gp == 'Maths':
					counter_p3 += 1
				balancer_pass_pure[rows][cols] = gp
			else:
				break
'''
'''
def pass_pure_selector_2_3():

	for i in range(0,6):
		balancer_pass_pure_2[i] = balancer_pass_pure[i][:]
		balancer_pass_pure_3[i] = balancer_pass_pure[i][:]
		random.shuffle(balancer_pass_pure_2[i])
		random.shuffle(balancer_pass_pure_3[i])
'''
def pass_bio_selector():
	lister_counter = 0
	lister = ["Zoology (PC)","Botany (PC)","Physiology (PC)"]

	for rows in range(0,4):
		random.shuffle(lister)
		for cols in range(0,2):
			if lister_counter > 2:
				lister_counter = 0

			balancer_pass_bio[rows][cols] = lister[lister_counter]
			lister_counter += 1
		
		balancer_pass_bio[rows][4] = lister[lister_counter]
		lister_counter += 1
'''
def pass_bio_selector():
	counter_p1 = 0
	counter_p2 = 0
	counter_p3 = 0
	counter_p4 = 0

	for rows in range(0,6):
		for cols in range(0,3):

			lister = ["Zoology","Botany","Physiology"]

			if counter_p1 >= 4 and 'Zoology' in lister:
				lister.remove('Zoology')
			if counter_p3 >= 4 and 'Botany' in lister:
				lister.remove('Botany')
			if counter_p4 >= 4 and 'Physiology' in lister:
				lister.remove('Physiology')

			if lister:
				gp = random.choice(lister)
				if gp == 'Zoology':
					counter_p1 += 1
				elif gp == 'Botany':
					counter_p3 += 1
				elif gp == 'Physiology':
					counter_p4 += 1
				balancer_pass_bio[rows][cols] = gp
			else:
				break
'''
'''
def pass_bio_selector_2_3():
	for i in range(0,6):
		balancer_pass_bio_2[i] = balancer_pass_bio[i][:]
		balancer_pass_bio_3[i] = balancer_pass_bio[i][:]
		random.shuffle(balancer_pass_bio_2[i])
		random.shuffle(balancer_pass_bio_3[i])
'''


#argha

selector_pure_2()
selector_pure_3()

selector_bio_2()
selector_bio_3()

selector_cs()
selector_cs_2()
selector_cs_3()

pass_pure_selector()
pass_bio_selector()
'''
pass_pure_selector_2_3()
pass_bio_selector_2_3()
'''

al_3 = ["HNS 3","HNS 4","HNS 6","HNS 7","PASS 2","PASS 4","PAPER I","PAPER II","AECC","GEC"]
al_2 = ["HNS 7(P/M)","HNS 7 M/C"]
al_1 = ["HNS 6(PHY)","HNS 7(Maths)","PASS 3(CHE)","Paper II /Math/2","GEC (MATH)","H5 Lab","Pass (Math)","Pass 2(Che)","Pass 2(Phy)","M8 + Che 8","Physics (PC)","Chemistry (PC)","Maths (PC)"]

bl_5 = ["HNS 3","HNS 4","HNS 6","HNS 7","PAPER I","PAPER II","AECC","GEC"]
bl_3 = ["Pass 4"]
bl_1 = ["Pass 2(P)","Pass 2(Z)","Pass 2(B)","Zoology (PC)","Botany (PC)","Physiology (PC)"]
 
def group_tester(obj, mode):
	val = 0
	new_lis = []
	if re.search('\r\n',obj):
		obj = obj.replace('\r\n', '/')
		obj = obj.replace(' ', '')
		new_lis = obj.split('/')
	#print new_lis

	if new_lis:
		if 'H5Lab' in new_lis:
			obj = 'H5 Lab'
		elif '+M8+Che8':
			obj = 'M8 + Che 8'

	if mode == 0:
		if obj in al_3:
			val = 3
		elif obj in al_2:
			val = 2
		elif obj in al_1:
			val = 1
	
	elif mode == 1:
		if obj in bl_5:
			val = 5
		elif obj in bl_3:
			val = 3
		elif obj in bl_1:
			val = 1

	return val

def alloter(i,j,room,capa,n,students,year,mode):

	if mode == 0:
		if year == 1:
			alcls = alloted_cls_pure
			almnt = allotment_pure
		elif year == 2:
			alcls = alloted_cls_pure_2
			almnt = allotment_pure_2
		elif year == 3:
			alcls = alloted_cls_pure_3
			almnt = allotment_pure_3
	elif mode == 1:
		if year == 1:
			alcls = alloted_cls_bio
			almnt = allotment_bio
		elif year == 2:
			alcls = alloted_cls_bio_2
			almnt = allotment_bio_2
		elif year == 3:
			alcls = alloted_cls_bio_3
			almnt = allotment_bio_3
	elif mode == 2:
		if year == 1:
			alcls = alloted_cls_cs
			almnt = allotment_cs
		elif year == 2:
			alcls = alloted_cls_cs_2
			almnt = allotment_cs_2
		elif year == 3:
			alcls = alloted_cls_cs_3
			almnt = allotment_cs_3
	elif mode == 3:
		if year == 1:
			alcls = alloted_cls_pure_pass
			almnt = allotment_pure_pass
		elif year == 2:
			alcls = alloted_cls_pure_pass_2
			almnt = allotment_pure_pass_2
		elif year == 3:
			alcls = alloted_cls_pure_pass_3
			almnt = allotment_pure_pass_3
	elif mode == 4:
		if year == 1:
			alcls = alloted_cls_bio_pass
			almnt = allotment_bio_pass
		elif year == 2:
			alcls = alloted_cls_bio_pass_2
			almnt = allotment_bio_pass_2
		elif year == 3:
			alcls = alloted_cls_bio_pass_3
			almnt = allotment_bio_pass_3

	for no in range(0,n):
		try:
			alloted = min(capa, key = lambda z:abs(students[no] - z))
		except:
			alloted = None
		if alloted is not None:
			index = capa.index(alloted)
			alcls.append(room[index])
			almnt.extend([[i,j]])
			del room[index]
			del capa[index]

	return room,capa

def class_alloter():

	compl = ["English","Bangla","ENV"]

	for cols in range(0,7):
		for rows in range(0,6):

			class_room = bsc_cls_room[:]
			class_capa = bsc_cls_capa[:]

			if balancer_pass_pure[rows][cols] is not None:
				val = group_tester(balancer_pass_pure[rows][cols], 0)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_pure_capa,1,3)

			if balancer_pass_bio[rows][cols] is not None:
				val = group_tester(balancer_pass_bio[rows][cols], 1)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_bio_capa,1,4)

			if balancer_pure[rows][cols] is not None:
				val = group_tester(balancer_pure[rows][cols], 0)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,val,pure_capa[0],1,0)

			if balancer_pure_2[rows][cols] is not None:
				val = group_tester(balancer_pure_2[rows][cols], 0)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,val,pure_capa[1],2,0)

			
			if balancer_pure_3[rows][cols] is not None:
				if balancer_pure_3[rows][cols] in compl:
					val = 3
				else:
					val = group_tester(balancer_pure_3[rows][cols], 0)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,val,pure_capa[2],3,0)

			if balancer_bio[rows][cols] is not None:
				val = group_tester(balancer_bio[rows][cols], 1)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,val,bio_capa[0],1,1)

			if balancer_bio_2[rows][cols] is not None:
				val = group_tester(balancer_bio_2[rows][cols], 1)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,val,bio_capa[1],2,1)

			if balancer_bio_3[rows][cols] is not None:
				if balancer_bio_3[rows][cols] in compl:
					val = 5
				else:
					val = group_tester(balancer_bio_3[rows][cols], 1)
				if val is not 0 and class_room:
					class_room, class_capa = alloter(rows,cols,class_room,class_capa,val,bio_capa[2],3,1)

def cs_class_alloter():

	subjs = ['II A','III','IV','Theory IV','Theory VI',"PAPER I","PAPER II","AECC","GEC","GEC (MATH)"]

	for cols in range(0,7):
		for rows in range(0,6):

			class_room = cs_cls_room[:]
			class_capa = cs_cls_capa[:]

			if balancer_cs[rows][cols] in subjs:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,cs_capa,1,2)

			if balancer_cs_2[rows][cols] in subjs:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,cs_capa,2,2)

			if balancer_cs_3[rows][cols] in subjs:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,cs_capa,3,2)

def pass_class_alloter():

	for cols in range(0,5,2):
		for rows in range(0,4):

			class_room = bsc_cls_room[:]
			class_capa = bsc_cls_capa[:]

			if balancer_pass_pure[rows][cols] is not None:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_pure_capa,1,3)
			'''
			if balancer_pass_pure_2[rows][cols] is not None:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_pure_capa,2,3)

			if balancer_pass_pure_3[rows][cols] is not None:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_pure_capa,3,3)
			'''			

			if balancer_pass_bio[rows][cols] is not None:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_bio_capa,1,4)

			'''
			if balancer_pass_bio_2[rows][cols] is not None:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_bio_capa,2,4)

			if balancer_pass_bio_3[rows][cols] is not None:
				class_room, class_capa = alloter(rows,cols,class_room,class_capa,1,pass_bio_capa,3,4)
			'''

#pass_class_alloter()
class_alloter()
cs_class_alloter()

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
slots = ['Days/Slots','10:00 - 11:00','11:00 - 12:00','12:00 - 1:00','1:00 - 2:00','2:00 - 3:00','3:00 - 4:00','4:00 - 5:00']

for i in range(0,6):
	balancer_pure[i].insert(0,days[i])
	balancer_pure_2[i].insert(0,days[i])
	balancer_pure_3[i].insert(0,days[i])
	balancer_bio[i].insert(0,days[i])
	balancer_bio_2[i].insert(0,days[i])
	balancer_bio_3[i].insert(0,days[i])
	balancer_cs[i].insert(0,days[i])
	balancer_cs_2[i].insert(0,days[i])
	balancer_cs_3[i].insert(0,days[i])
	balancer_pass_pure[i].insert(0,days[i])
	balancer_pass_bio[i].insert(0,days[i])

balancer_pure.insert(0,slots)
balancer_pure_2.insert(0,slots)
balancer_pure_3.insert(0,slots)
balancer_bio.insert(0,slots)
balancer_bio_2.insert(0,slots)
balancer_bio_3.insert(0,slots)
balancer_cs.insert(0,slots)
balancer_cs_2.insert(0,slots)
balancer_cs_3.insert(0,slots)
balancer_pass_pure.insert(0,slots)
balancer_pass_bio.insert(0,slots)

doc1 = SimpleDocTemplate("Pure_1.pdf", pagesize=letter)
doc2 = SimpleDocTemplate("Pure_2.pdf", pagesize=letter)
doc3 = SimpleDocTemplate("Pure_3.pdf", pagesize=letter)

doc4 = SimpleDocTemplate("Bio_1.pdf", pagesize=letter)
doc5 = SimpleDocTemplate("Bio_2.pdf", pagesize=letter)
doc6 = SimpleDocTemplate("Bio_3.pdf", pagesize=letter)

doc7 = SimpleDocTemplate("CS_1.pdf", pagesize=letter)
doc8 = SimpleDocTemplate("CS_2.pdf", pagesize=letter)
doc9 = SimpleDocTemplate("CS_3.pdf", pagesize=letter)

doc10 = SimpleDocTemplate("Pass_Pure_1.pdf", pagesize=letter)
doc11 = SimpleDocTemplate("Pass_Bio_1.pdf", pagesize=letter)


elements = []
p1 = Table(balancer_pure,8*[1.0*inch], 7*[0.4*inch])
p2 = Table(balancer_pure_2,8*[1.0*inch], 7*[0.4*inch])
p3 = Table(balancer_pure_3,8*[1.0*inch], 7*[0.4*inch])

b1 = Table(balancer_bio,8*[1.0*inch], 7*[0.4*inch])
b2 = Table(balancer_bio_2,8*[1.0*inch], 7*[0.4*inch])
b3 = Table(balancer_bio_3,8*[1.0*inch], 7*[0.4*inch])

c1 = Table(balancer_cs,8*[1.0*inch], 7*[0.4*inch])
c2 = Table(balancer_cs_2,8*[1.0*inch], 7*[0.4*inch])
c3 = Table(balancer_cs_3,8*[1.0*inch], 7*[0.4*inch])

pp1 = Table(balancer_pass_pure,8*[1.0*inch], 7*[0.4*inch])
pb1 = Table(balancer_pass_bio,8*[1.0*inch], 7*[0.4*inch])

tabs = [p1,p2,p3,b1,b2,b3,c1,c2,c3,pp1,pb1]
docs = [doc1,doc2,doc3,doc4,doc5,doc6,doc7,doc8,doc9,doc10,doc11]

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

allots = [allotment_pure,allotment_pure_2,allotment_pure_3,allotment_bio,allotment_bio_2,allotment_bio_3,allotment_pure_pass,allotment_bio_pass]
allots_cls = [alloted_cls_pure,alloted_cls_pure_2,alloted_cls_pure_3,alloted_cls_bio,alloted_cls_bio_2,alloted_cls_bio_3,alloted_cls_pure_pass,alloted_cls_bio_pass]

files = ["Year_1_Pure_Sc","Year_2_Pure_Sc","Year_3_Pure_Sc","Year_1_Bio_Sc","Year_2_Bio_Sc","Year_3_Bio_Sc","Pass_Year_1_Pure","Pass_Year_1_Bio"]

def texter(allots, allots_cls):
	text = days[allots[0]] + " --> " +str(allots[1]+1) + " --> " +str(allots_cls) + "\r\n"
	return text
length = len(files)
for i in range(0,length):
	file_name = str(files[i]) +".txt"
	fi = open(file_name,"w")
	text = "DAY --> PERIOD --> CLASS\r\n"
	fi.write(text)
	for k in range(0,len(allots[i])):
		text = texter(allots[i][k],allots_cls[i][k])
		#text = str(allots[i][k]) + " --> " + str(allots_cls[i][k]) + "\r\n"
		fi.write(text)
	fi.close()

allots = [allotment_cs,allotment_cs_2,allotment_cs_3]
allots_cls = [alloted_cls_cs,alloted_cls_cs_2,alloted_cls_cs_3]

files = ["Year_1_CS","Year_2_CS","Year_3_CS"]
for i in range(0,3):
	file_name = str(files[i]) + ".txt"
	fi = open(file_name,"w")
	text = "DAY --> PERIOD --> CLASS\r\n"
	fi.write(text)
	for k in range(0,len(allots[i])):
		text = texter(allots[i][k],allots_cls[i][k])
		#text = str(allots[i][k]) + " --> " + str(allots_cls[i][k]) + "\r\n"
		fi.write(text)
	fi.close()


#argha
'''
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
slots = ['Days/Slots','07:00 - 08:00','08:00 - 09:00','09:00 - 10:00']

for i in range(0,6):
	balancer_pass_pure[i].insert(0,days[i])
	balancer_pass_pure_2[i].insert(0,days[i])
	balancer_pass_pure_3[i].insert(0,days[i])
	balancer_pass_bio[i].insert(0,days[i])
	balancer_pass_bio_2[i].insert(0,days[i])
	balancer_pass_bio_3[i].insert(0,days[i])

balancer_pass_pure.insert(0,slots)
balancer_pass_pure_2.insert(0,slots)
balancer_pass_pure_3.insert(0,slots)
balancer_pass_bio.insert(0,slots)
balancer_pass_bio_2.insert(0,slots)
balancer_pass_bio_3.insert(0,slots)


doc1 = SimpleDocTemplate("Pass_Pure_1.pdf", pagesize=letter)
doc2 = SimpleDocTemplate("Pass_Pure_2.pdf", pagesize=letter)
doc3 = SimpleDocTemplate("Pass_Pure_3.pdf", pagesize=letter)

doc4 = SimpleDocTemplate("Pass_Bio_1.pdf", pagesize=letter)
doc5 = SimpleDocTemplate("Pass_Bio_2.pdf", pagesize=letter)
doc6 = SimpleDocTemplate("Pass_Bio_3.pdf", pagesize=letter)

elements = []
p1 = Table(balancer_pass_pure,8*[1.25*inch], 7*[0.4*inch])
p2 = Table(balancer_pass_pure_2,8*[1.25*inch], 7*[0.4*inch])
p3 = Table(balancer_pass_pure_3,8*[1.25*inch], 7*[0.4*inch])

b1 = Table(balancer_pass_bio,8*[1.0*inch], 7*[0.4*inch])
b2 = Table(balancer_pass_bio_2,8*[1.0*inch], 7*[0.4*inch])
b3 = Table(balancer_pass_bio_3,8*[1.0*inch], 7*[0.4*inch])

tabs = [p1,p2,p3,b1,b2,b3]
docs = [doc1,doc2,doc3,doc4,doc5,doc6]

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

allots = [allotment_pure_pass,allotment_pure_pass_2,allotment_pure_pass_3]
allots_cls = [alloted_cls_pure_pass,alloted_cls_pure_pass_2,alloted_cls_pure_pass_3]

files = ["Year_1_PURE_PASS","Year_2_PURE_PASS","Year_3_PURE_PASS"]
for i in range(0,3):
	file_name = str(files[i]) + ".txt"
	fi = open(file_name,"w")
	text = "DAY --> PERIOD --> CLASS\r\n"
	fi.write(text)
	for k in range(0,len(allots[i])):
		text = texter(allots[i][k],allots_cls[i][k])
		fi.write(text)
	fi.close()

allots = [allotment_bio_pass,allotment_bio_pass_2,allotment_bio_pass_3]
allots_cls = [alloted_cls_bio_pass,alloted_cls_bio_pass_2,alloted_cls_bio_pass_3]

files = ["Year_1_BIO_PASS","Year_2_BIO_PASS","Year_3_BIO_PASS"]
for i in range(0,3):
	file_name = str(files[i]) + ".txt"
	fi = open(file_name,"w")
	text = "DAY --> PERIOD --> CLASS\r\n"
	fi.write(text)
	for k in range(0,len(allots[i])):
		text = texter(allots[i][k],allots_cls[i][k])
		fi.write(text)
	fi.close()
'''
#argha