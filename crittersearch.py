import pandas
import math

def crittersearch():
        searchterm1=input("Search for bug or fish? ")
        for word in ["insect","bug"]:
                if word in searchterm1.lower():
                        insects_xl=pandas.read_excel('insectlist.xlsx')
                        insects=insects_xl.to_dict('records')
                        searchterm2=input("Search for what bug? ")
                        print ("\n")
                        for bug in insects:
                                if searchterm2.lower() in bug['Name'].lower():
                                        if not math.isnan(bug['Value']):
                                                bug['Value']=math.trunc(bug['Value'])
                                        print (bug['Name']+"\t"+str(bug['How to catch'])+"\t"+str(bug['Time'])+"\t"+str(bug['Value']))
                                        
        if "fish" in searchterm1.lower():
                fishes_xl=pandas.read_excel('Fishlist.xlsx')
                fishes=fishes_xl.to_dict('records')
                searchterm3=input("Search for which fish? ")
                print ("\n")
                for fish in fishes:
                        if searchterm3.lower() in fish['Name'].lower():
                                print (fish['Name']+"\t"+fish['Location']+"\t"+fish['Size']+"\t\t"+fish['Time']+"\t\t"+str(fish['Value']))

if __name__ == "__main__":
        crittersearch()
