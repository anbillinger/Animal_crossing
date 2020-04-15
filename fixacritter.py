import openpyxl
import pandas
import sys

def _or_in_(alist,astring):
	for word in alist:
		if word.lower() in astring.lower():
			return True
	return False
def endearly(astring):
	endlist=["nvm","cancel","stop","nevermind"]
	for word in endlist:
	    if word in astring.lower(): sys.exit()
	    
def fixacritter():
        print ("\nDo you need to fix a bug entry or a fish entry? ")
        myinp=input()

        if _or_in_(["bug","insect"],myinp.lower()):
                wbkbugs = 'insectlist.xlsx'
                wbkb = openpyxl.load_workbook(wbkbugs)
                insects_xl=pandas.read_excel(wbkbugs)
                insects=insects_xl.to_dict('records')
                bugnamelist=list(map(lambda x:(x['Name']),insects))
                sheetb=wbkb.worksheets[0]
                print ("What bug? ")
                whichbug=input()
                endearly(whichbug)
                keysl=list(insects[0].keys())[1:]
                if whichbug.title() in bugnamelist:
                        bugnum=bugnamelist.index(whichbug.title())+2
                else:
                        bsc=True
                        while bsc:
                                print ("Sorry, couldn't find that bug. Try a search?")
                                searchcheck=input()
                                if "y" in searchcheck.lower():
                                        print ("Search for what term?")
                                        bugsearch=input()
                                        endearly(bugsearch)
                                        for buug in bugnamelist:
                                                if bugsearch.lower() in buug.lower():
                                                        print ("Is this your bug? "+buug)
                                                        buugcheck=input()
                                                        if "y" in buugcheck.lower():
                                                                bugnum=bugnamelist.index(buug)+2
                                                                bsc=False
                                                                break
                                else: sys.exit()
                fixwhile=True
                while fixwhile:
                        print ("Fix what part of the entry? Options: "+', '.join(keysl))
                        fixer=input().capitalize()
                        endearly(fixer)
                        if fixer in keysl:
                                fixnum=keysl.index(fixer)+2
                                fixwhile=False
                print ("This cell currently reads: "+sheetb.cell(row=bugnum,column=fixnum).value+". What should it read instead?")
                newval=input()
                endearly(newval)
                sheetb.cell(row=bugnum,column=fixnum).value=newval
                if sheetb.cell(row=bugnum,column=fixnum).value==newval:
                        print (sheetb.cell(row=bugnum,column=2).value+" "+fixer.lower()+" successfully changed to "+newval)

                wbkb.save(wbkbugs)
                wbkb.close
                
                
        if ("fish") in myinp.lower():
                wbkfish = 'Fishlist.xlsx'
                wbkf = openpyxl.load_workbook(wbkfish)
                fish_xl=pandas.read_excel(wbkfish)
                fish=fish_xl.to_dict('records')
                fishnamelist=list(map(lambda x:(x['Name']),fish))
                sheetf=wbkf.worksheets[0]
                print ("What fish? ")
                whichfish=input()
                endearly(whichfish)
                keysl=list(fish[0].keys())[1:]
                if whichfish.title() in fishnamelist:
                        fishnum=fishnamelist.index(whichfish.title())+2
                else:
                        fsc=True
                        while fsc:
                                print ("Sorry, couldn't find that fish. Try a search?")
                                searchcheck=input()
                                if "y" in searchcheck.lower():
                                        print ("Search for what term?")
                                        fishsearch=input()
                                        endearly(fishsearch)
                                        for fysh in fishnamelist:
                                                if fishsearch.lower() in fysh.lower():
                                                        print ("Is this your fish? "+fysh)
                                                        fyshcheck=input()
                                                        if "y" in fyshcheck.lower():
                                                                fishnum=fishnamelist.index(fysh)+2
                                                                fsc=False
                                                                break
                                else: sys.exit()
                fixwhile=True
                while fixwhile:
                        print ("Fix what part of the entry? Options: "+', '.join(keysl))
                        fixer=input().capitalize()
                        endearly(fixer)
                        if fixer in keysl:
                            fixnum=keysl.index(fixer)+2
                            fixwhile=False
                                
                print ("This cell currently reads: "+sheetf.cell(row=fishnum,column=fixnum).value+". What should it read instead?")
                newval=input()
                endearly(newval)
                sheetf.cell(row=fishnum,column=fixnum).value=newval
                if sheetf.cell(row=fishnum,column=fixnum).value==newval:
                        print (sheetf.cell(row=fishnum,column=2).value+" "+fixer.lower()+" successfully changed to "+newval)

                wbkf.save(wbkfish)
                wbkf.close

if __name__ == "__main__":
        fixacritter()
