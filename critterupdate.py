import openpyxl
import pandas

def _or_in_(alist,astring):
	for word in alist:
		if word.lower() in astring.lower():
			return True
	return False
fishinit=False
buginit=False
print ("\nDid you catch a bug or a fish? ")
myinp=input()

if _or_in_(["bug","insect"],myinp.lower()):
	wbkbugs = 'insectlist.xlsx'
	wbkb = openpyxl.load_workbook(wbkbugs)
	insects_xl=pandas.read_excel(wbkbugs)
	insects=insects_xl.to_dict('records')
	bugnamelist=list(map(lambda x:(x['Name']),insects))
	buginit=True
	sheetb=wbkb.worksheets[0]
	print ("What bug? ")
	whichbug=input()
	bsc=True
	while bsc:
		if whichbug.title() in bugnamelist:
			bugnum=bugnamelist.index(whichbug.title())+2
			sheetb.cell(row=bugnum,column=7).value="Yes"
			if sheetb.cell(row=bugnum,column=7).value=="Yes":
				print ("Successfully added")
			bsc=False
		else: 
			print ("Sorry, couldn't find that bug. Try a search?")
			searchcheck=input()
			if "y" in searchcheck.lower():
				print ("Search for what term?")
				bugsearch=input()
				for buug in bugnamelist:
					if bugsearch.lower() in buug.lower():
						print ("Is this your bug? "+buug)
						buugcheck=input()
						if "y" in buugcheck.lower():
							bugnum=bugnamelist.index(buug)+2
							sheetb.cell(row=bugnum,column=7).value="Yes"
							if sheetb.cell(row=bugnum,column=7).value=="Yes":
								print ("Successfully added")
							bsc=False
							break
			else: bsc=False
	
if ("fish") in myinp.lower():
	wbkfish = 'Fishlist.xlsx'
	wbkf = openpyxl.load_workbook(wbkfish)
	fish_xl=pandas.read_excel(wbkfish)
	fish=fish_xl.to_dict('records')
	fishnamelist=list(map(lambda x:(x['Name']),fish))
	fishinit=True
	sheetf=wbkf.worksheets[0]
	print ("Which fish? ")
	whichfish=input()
	fsc=True
	while fsc:
		if whichfish.title() in fishnamelist:
			fishnum=fishnamelist.index(whichfish.title())+2
			sheetf.cell(row=fishnum,column=8).value="Yes"
			if sheetf.cell(row=fishnum,column=8).value=="Yes":
				print ("Successfully added")
			fsc=False
		else:
			print ("Sorry, couldn't find that fish. Try a search?")
			searchcheck=input()
			if "y" in searchcheck.lower():
				print ("Search for what term?")
				fishsearch=input()
				for fysh in fishnamelist:
					if fishsearch.lower() in fysh.lower():
						print ("Is this your fish? "+fysh)
						fyshcheck=input()
						if "y" in fyshcheck.lower():
							fishnum=fishnamelist.index(fysh)+2
							sheetf.cell(row=fishnum,column=8).value="Yes"
							if sheetf.cell(row=fishnum,column=8).value=="Yes":
								print ("Successfully added")
			else: fsc=False
		

if buginit:
	wbkb.save(wbkbugs)
	wbkb.close
if fishinit:
	wbkf.save(wbkfish)
	wbkf.close

