import pandas as pd

def main():
	csv_names = ['FishList.csv','InsectList.csv']
	df_list = [pd.read_csv(csv_names[0]),pd.read_csv(csv_names[1])]
	if type(df_list[0]['Donated'][0]) != str:df_list[0]['Donated'] = df_list[0]['Donated'].astype(str)
	if type(df_list[1]['Donated'][0]) != str:df_list[1]['Donated'] = df_list[1]['Donated'].astype(str)

	to_add = input('Enter all critter names to add, separated by commas. Any unrecognized names will prompt a search.\n')
	lst_crit = list(map(lambda x: x.strip(),to_add.split(',')))
	for crit in lst_crit:
		crit_ind = "blank"
		df_ind = None
		for ind,df in enumerate(df_list):
			if crit.title() in list(df['Name']):
				crit_ind = df.loc[df['Name'] == crit.title()].index[0]
				df_ind = ind
				break
		while crit_ind == 'blank':
			
			    
			print('\nCould not find {}. Starting search. Enter "cancel" at any time to go to next critter in list.'.format(crit.title()))
			which = input('Is it a bug or a fish?\n')
			if 'cancel' in which.lower(): break
			keyword = input('Search for what keyword?\n')
			if 'cancel' in keyword.lower(): break
			if 'fish' in which.lower():
				crit_type = 'fish'
				df_ind = 0
			elif ('bug' in which.lower()) or ('insect' in which.lower()):
				df_ind = 1
				crit_type = 'bug'
			
			      
			for ind,x in enumerate(df_list[df_ind]['Name']):
				if keyword.lower() in x.lower():
					found = input('Is {} the {} you were looking for? '.format(x,crit_type))
					if 'cancel' in found.lower():
						break
					if 'y' in found.lower():
						crit_ind = ind
						break
			if not crit_ind:
				crit = keyword
				continue
			

		
		if crit_ind != 'blank':
			if (df_list[df_ind].iloc[crit_ind]['Donated']) == 'Yes':
				print('{} already listed as donated.'.format(crit.title()))
			else:
				df_list[df_ind].at[crit_ind,'Donated'] = 'Yes'
				print('Successfully added {} to donated list.'.format(crit.title()))

	for ind, df in enumerate(df_list):
	    df.to_csv(csv_names[ind],index=False)
	print("\nEnd of list, csv files updated and saved.")



if __name__ == "__main__":
	main()
