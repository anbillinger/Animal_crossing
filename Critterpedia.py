import pandas
import datetime
from datetime import time
import math

allmonths=["January","February","March","April","May","June","July","August","September","October","November","December"]

def monthscheck(txtstring):
	if "-" in txtstring:
		endcaps=txtstring.split("-")
	else: return [txtstring]
	startindex=allmonths.index(endcaps[0])
	endindex=allmonths.index(endcaps[1])
	if startindex<endindex:
		return allmonths[startindex:endindex+1]
	else: 
		firsthalf=allmonths[:endindex+1]
		secondhalf=allmonths[startindex:]
		return firsthalf+secondhalf
		
def timecheck(txtstring):
	now=datetime.datetime.now()
	if txtstring=="All day":
		return True
	else: 
		endcaps=txtstring.split(" - ")
		endcapsmil=[]
		for thing in endcaps:
			thing2=int(thing.split(" ")[0])
			if "p" in thing:
				endcapsmil.append(thing2+12)
			else:
				endcapsmil.append(thing2)
		if endcapsmil[0]<endcapsmil[1]:
			if endcapsmil[0]<=now.hour<endcapsmil[1]:
				return True
			else: return False
		else:
			if now.hour>endcapsmil[0] or now.hour<=endcapsmil[1]:
				return True
			else: return False

def _or_in_(alist,astring):
	for word in alist:
		if word.lower() in astring.lower():
			return True
	return False
			
def critterpedia():
	
	
	fishcheck=False
	bugcheck=False
	while not (fishcheck or bugcheck):
		which=input("Fish, Insects, or Both? ")
		if _or_in_(['fish','both'],which.lower()):fishcheck=True
		if _or_in_(['insect','bug','but','both'],which.lower()):bugcheck=True

	incdonated=False
	whilecheck=True
	while whilecheck:
		donatecheck=input("Show already donated critters? ")
		if 'y' in donatecheck.lower():
			incdonated=True
			whilecheck=False
		elif 'n' in donatecheck.lower():
			whilecheck=False
		
	monthcheck=''
	neworend=""
	while monthcheck not in allmonths:
		monthcheck=input("What month? Specify new or ending critters? ")
		if "end" in monthcheck.lower():
			neworend="end"
		elif "new" in monthcheck.lower():
			neworend="new"
		for months in allmonths:
			if months.lower() in monthcheck.lower():
				monthcheck=months
		

	whilecheck2=True
	while whilecheck2:
		timein=input("Available now or any time of day? ")
		if ("any" or "all") in timein.lower():
			whilecheck2=False
			checktime=False
		if ("now" or "this") in timein.lower():
			checktime=True
			whilecheck2=False
			
	loccheck=False
	sizecheck=False
	valcheck=False
	if incdonated:
		ffinput=input("Any further restrictions? Please list all now ")
		if "value" in ffinput.lower():
			valcheck=True
			print ("What's the cutoff?")
			minval=int(input())
		if "location" in ffinput.lower():
			loccheck=True
			print ("What location? Enter river, sea, pond, or pier, or it will return an empty list")
			loca=input()
		if "size" in ffinput.lower():
			sizecheck=True
			print ("What size? Enter smallest, small, medium, large, x large, or largest, or it will return an empty list")
			sizein=input()
				
			
		
		
	if bugcheck:
		insects_xl=pandas.read_excel('insectlist.xlsx')
		insects=insects_xl.to_dict('records')
		print ("\n")
		titles=["Name","How to catch","Time"]
		for insect in insects:
			if "Year" in insect['Months']: insect['Simple Months']=allmonths
			else: 
				if "," in insect['Months']:
					txtstrings=insect['Months'].split(", ")
					txtstring1=txtstrings[0].split(" ")[0]
					txtstring2=txtstrings[1].split(" ")[0]
					insect['Simple Months']=monthscheck(txtstring1)+monthscheck(txtstring2)
				else:
					txtstring=insect['Months'].split(" ")[0]
					insect['Simple Months']=monthscheck(txtstring)
		shortlisti=list(filter(lambda x:(monthcheck in x['Simple Months']),insects))
		if not incdonated:
			shortlisti=list(filter(lambda x:(x["Donated"]!="Yes"),shortlisti))
		if neworend=="end":
			indcheck=allmonths.index(monthcheck)
			shortlisti=list(filter(lambda x:(allmonths[indcheck+1] not in x['Simple Months']),shortlisti))
		if neworend=="new":
			indcheck=allmonths.index(monthcheck)
			shortlisti=list(filter(lambda x:(allmonths[indcheck-1] not in x['Simple Months']),shortlisti))
		if checktime:
			shortlisti=list(filter(lambda x:(timecheck(x["Time"])),shortlisti))
		if valcheck:
			shortlisti=list(filter(lambda x:(not math.isnan(x['Value'])),shortlisti))
			shortlisti=list(filter(lambda x:(x['Value']>=minval),shortlisti))
		print ("Insects:")
		if shortlisti==[]:print ("None")
		else:
			maxn=max(list(map(lambda x:(len(x["Name"])),shortlisti)))
			listh=list(map(lambda x:(len(x['How to catch'])),shortlisti))
			listh.append(12)
			maxh=max(listh)
			maxt=max(list(map(lambda x:(len(x["Time"])),shortlisti)))
			print ("Name"+" "*(maxn-4)+"\t"+'How to catch'+" "*(maxh-12)+"\t"+'Time'+" "*(maxt-4)+"\t\t"+"Value")
			for insect in shortlisti:
				insect['Name']=insect['Name']+" "*(maxn-len(insect['Name']))
				insect['How to catch']=insect['How to catch']+" "*(maxh-len(insect['How to catch']))
				insect['Time']=insect['Time']+" "*(maxt-len(insect['Time']))
				if not math.isnan(insect['Value']):
					insect['Value']=math.trunc(insect['Value'])
				print (insect['Name']+"\t"+insect['How to catch']+"\t"+insect['Time']+"\t\t"+str(insect['Value']))
		
	if fishcheck:	
		fishes_xl=pandas.read_excel('Fishlist.xlsx')
		fishes=fishes_xl.to_dict('records')
		print ("\n")
		for fish in fishes:
			if "Year" in fish['Months']: fish['Simple Months']=allmonths
			else: 
				if "," in fish['Months']:
					txtstrings=fish['Months'].split(", ")
					txtstring1=txtstrings[0].split(" ")[0]
					txtstring2=txtstrings[1].split(" ")[0]
					fish['Simple Months']=monthscheck(txtstring1)+monthscheck(txtstring2)
				else:
					txtstring=fish['Months'].split(" ")[0]
					fish['Simple Months']=monthscheck(txtstring)
				
		print ('Fish:')
		shortlistf=list(filter(lambda x:(monthcheck in x['Simple Months']),fishes))
		if not incdonated:
			shortlistf=list(filter(lambda x:(x["Donated"]!="Yes"),shortlistf))
		if neworend=="end":
			indcheck=allmonths.index(monthcheck)
			shortlistf=list(filter(lambda x:(allmonths[indcheck+1] not in x['Simple Months']),shortlistf))
		if neworend=="new":
			indcheck=allmonths.index(monthcheck)
			shortlistf=list(filter(lambda x:(allmonths[indcheck-1] not in x['Simple Months']),shortlistf))
		if checktime:
			shortlistf=list(filter(lambda x:(timecheck(x["Time"])),shortlistf))
		if valcheck:
			shortlistf=list(filter(lambda x:(not math.isnan(x['Value'])),shortlistf))
			shortlistf=list(filter(lambda x:(x['Value']>=minval),shortlistf))
		if loccheck:
			if "sea" in loca.lower():
				shortlistf=list(filter(lambda x:(_or_in_(["sea","pier"],x['Location'].lower())),shortlistf))
			else:shortlistf=list(filter(lambda x:(loca.lower() in x['Location'].lower()),shortlistf))
		if sizecheck:
			if "largest" in sizein.lower():
				shortlistf=list(filter(lambda x:(sizein.lower() in x['Size'].lower()),shortlistf))
			else: shortlistf=list(filter(lambda x:(sizein.lower()==x['Size'].lower()),shortlistf))
		if shortlistf==[]:print ("None")
		else:
			maxn=max(list(map(lambda x:(len(x["Name"])),shortlistf)))
			listl=list(map(lambda x:(len(x['Location'])),shortlistf))
			listl.append(8)
			maxl=max(listl)
			maxs=max(list(map(lambda x:(len(x["Size"])),shortlistf)))
			maxt=max(list(map(lambda x:(len(x["Time"])),shortlistf)))
			print ("Name"+" "*(maxn-4)+"\t"+'Location'+" "*(maxl-8)+"\t"+"Size"+" "*(maxs-4)+"\t"+'Time'+" "*(maxt-4)+"\t"+"Value")
			for fish in shortlistf:
				fish['Name']=fish['Name']+" "*(maxn-len(fish['Name']))
				fish['Location']=fish['Location']+" "*(maxl-len(fish['Location']))
				fish['Size']=fish['Size']+" "*(maxs-len(fish['Size']))
				fish['Time']=fish['Time']+" "*(maxt-len(fish['Time']))
				print (fish['Name']+"\t"+fish['Location']+"\t"+fish['Size']+"\t"+fish['Time']+"\t"+str(fish['Value']))


if __name__ == "__main__":
	critterpedia()
