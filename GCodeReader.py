import time
StartTime = time.time()
import os
import sys
import glob

os.chdir('C:\Alsayyad\CNC\CNC Codes\CNC1')
#print(os.listdir(os.getcwd()))

ListOfFiles = glob.glob('P*')


print(ListOfFiles)

'''
for i in ListOfFiles:
    GCode = []
    with open(i,'r') as f:
        GCode = f.readlines()
    
    #EditedFiles
'''
for i in ListOfFiles:
    GCode = []
    CleanGCode = []
    FName = os.path.join('ForPrinting', i+'.txt')
    with open(i ,'r') as F:
        #Original Code
        GCode = F.readlines()
        print(GCode)
    #Process The Text
    for Line in GCode:
        TMP = [[]]
        for Char in Line:
            #Check For Uppercase and not 'N'
            if Char.isupper() and Char != 'N':
                TMP.append([])
            TMP[-1].append(Char)
        
        CleanGCode.append(' '.join(''.join(Line) for Line in TMP))

    with open(FName,'w') as F:
        OpeningTXT = i + '\n'
        F.write(OpeningTXT)
        F.writelines(CleanGCode)
        print('DONE')



#To Calculate Time Taken!
print("--- %s Seconds ---" % (time.time() - StartTime))