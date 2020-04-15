import pandas
import math

def crittersearch():
        print ("Search for bug or fish?")
        searchterm1=input()
        for word in ["insect","bug"]:
                if word in searchterm1.lower():
                        insects_xl=pandas.read_excel('insectlist.xlsx')
                        insects=insects_xl.to_dict('records')
                        print ("Search for what bug?")
                        searchterm2=input()
                        print ("\n")
                        for bug in insects:
                                if searchterm2.lower() in bug['Name'].lower():
                                        if not math.isnan(bug['Value']):
                                                bug['Value']=math.trunc(bug['Value'])
                                        print (bug['Name']+"\t"+str(bug['How to catch'])+"\t"+str(bug['Time'])+"\t"+str(bug['Value']))
                                        
        if "fish" in searchterm1.lower():
                fishes_xl=pandas.read_excel('Fishlist.xlsx')
                fishes=fishes_xl.to_dict('records')
                print ("Search for which fish?")
                searchterm3=input()
                print ("\n")
                for fish in fishes:
                        if searchterm3.lower() in fish['Name'].lower():
                                print (fish['Name']+"\t"+fish['Location']+"\t"+fish['Size']+"\t\t"+fish['Time']+"\t\t"+str(fish['Value']))

if __name__ == "__main__":
        crittersearch()
