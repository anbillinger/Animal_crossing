from datetime import datetime
import numpy as np
import pandas as pd
from IPython.display import display

def monthscheck(txtstring):
	if "Year" in txtstring: return list(range(1,13))
	if ',' in txtstring:
		txt1 = txtstring.split(", ")[0].split(' ')[0]
		txt2 = txtstring.split(", ")[1].split(' ')[0]
		return monthscheck(txt1)+monthscheck(txt2)
	else: txtstring = txtstring.split(" ")[0]
	if "-" in txtstring:
		endcapstxt = txtstring.split("-")
	else: return [datetime.strptime(txtstring,'%B').month]

	endcaps = [datetime.strptime(x,'%B').month for x in endcapstxt]

	if endcaps[0] < endcaps[1]:
		return list(range(endcaps[0],endcaps[1]+1))
	return list(range(1,endcaps[1]+1))+list(range(endcaps[0],13))

def time_check(txtstring):
	now = datetime.now()
	if txtstring == "All day":
		return True 

	endcaps = txtstring.split(" - ")
	endcapsmilitary = [(int(x.split(" ")[0])+12*("p" in x)) for x in endcaps]
	if endcapsmilitary[0] < endcapsmilitary[1]:
	    if endcapsmilitary[0] <= now.hour < endcapsmilitary[1]: return True
	    else: return False

	if now.hour > endcapsmilitary[0] or now.hour <= endcapsmilitary[1]: return True
	return False

def main():
	
	typecheck = 'fishbug'
	monthcheck = datetime.now().month
	endcheck = False
	exclude_donated = False
	timecheck = False
	min_value = False
	locationcheck = False
	sizecheck = False
	get_names = False
	whatchecks = input("Which questions to specify? Enter 'help' to list options and their defaults.\n")
	if 'help' in whatchecks.lower():
		print ('''\nOptions for what can be specified are:\nBugs, fish, or both\t(default Both, enter "type" to change)\nWhat month\t\t(default current month, enter "month" to change)\nEnding this month\t(default no, enter "end" to change)\nExclude donated\t\t(default no, enter "donate" or "exclude" to change)\nTime of day\t\t(default any time, enter "time" or "now" to change\nMinimum value\t\t(default no minimum, enter "value" to change)\nLocation of fish\t(default any, enter "location" to change)\nSize of fish\t\t(default any, enter "size" to change)\nShow names for critterupdate\t(default no, enter "names" to change)''')
		whatchecks = input('\nWhich questions to specify? Enter all at once\n')

	if 'type' in whatchecks.lower():
		typecheck = input('Which list do you want to see, fish or bugs?\n')
		while (('fish' not in typecheck) and ('bug' not in typecheck) and ('insect' not in typecheck)):
			typecheck = input('Not a valid response, please try again.\n')
	if 'month' in whatchecks.lower():
		monthtxt = input("Which month to see? Enter name, number, or 'next'. If entered incorrectly, will default to current month.\n")
		if 'next' in monthtxt.lower():
			if monthcheck == 12: monthcheck = 1
			else: monthcheck+=1
		elif monthtxt.isnumeric():
			if 1 <= int(monthtxt) <=12: monthcheck = int(monthtxt)
		else:
			try: datetime.strptime(monthtxt,'%B')
			except ValueError: print('Defaulting to current month\n')
			else: monthcheck = datetime.strptime(monthtxt,'%B').month

	if 'end' in whatchecks.lower():
		endcheck = True
		print('Will only display critters going away at the end of the month\n')

	if ('exclude' in whatchecks.lower()) or ('donate' in whatchecks.lower()):
		exclude_donated = True
		print('Already donated critters will not be show\n')
	if ('now' in whatchecks.lower()) or ('time' in whatchecks.lower()):
		timecheck = True
		print('Will only display currently available critters\n')
	if ('val' in whatchecks.lower()):
		min_value = input("What's the minimum value?\n")
		if min_value.isnumeric():min_value = int(min_value)
		while not (type(min_value) == int):
			min_value = input("Can only accept integer values. Please enter an integer value.\n")
			if min_value.isnumeric():min_value = int(min_value)
	if 'names' in whatchecks.lower():get_names = True

	#size and location
	if ('loc' in whatchecks.lower()):
		locationcheck = input('Where to search? Sea (can specify pier), river (can specify clifftop), or pond.\n')
	if 'size' in whatchecks.lower():
		sizecheck = input('What size? Smallest, small, medium, large, x large, or largest, or it will return an empty list\n')


	type_check = [('fish' in typecheck.lower()),(('insect' in typecheck.lower()) or ('bug' in typecheck.lower()))]
	csv_names = ['FishList.csv','InsectList.csv']
	df_list = []
	for num, val in enumerate(type_check):
		if val: df_list.append(pd.read_csv(csv_names[num]))
	for ind,df in enumerate(df_list):
		df['Month_List'] = df['Months'].apply(lambda x:monthscheck(x))
		df = df.loc[df['Month_List'].apply(lambda x:monthcheck in x)]
		df = df.drop('Month_List',axis=1)
		if exclude_donated: df.query('Donated != "Yes"',inplace=True)
		df = df.drop('Donated',axis=1)
		if timecheck: df = df.loc[df['Time'].apply(lambda x:time_check(x))]
		if min_value:
			valstr = 'Value >= {}'.format(min_value)
			df.query(valstr,inplace=True)


		
		df_list[ind] = df

	for df in df_list:
		
		display(df)
		if get_names: print((', ').join(df['Name']),'\n')


	#potential checks: size, location		
	    
	


if __name__ == "__main__":
	main()
