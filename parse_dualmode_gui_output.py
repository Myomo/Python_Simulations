#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import re


# In[2]:


def fIsAllowedSpecificChar(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


# In[3]:


def fAdjustTime(sTimeStamp):
    x = sTimeStamp.split('.');
    fSecAdj = int(x[1]) * 10**-9;
    fReturnValue = float(x[0]) + fSecAdj;
    #print(fReturnValue)
    return(fReturnValue);


# In[9]:


inputFile = open("C:\\Users\\Nuno Alves\\Downloads\\PropVelHold_HoldPos.txt", "r")
outputFile = open("C:\\Users\\Nuno Alves\\Downloads\\PropVelHold_HoldPos_output.txt", "w")
  
sArduinoValues=["nan","nan","nan"]
count = 0;
while True:   
    # Get next line from file 
    line = inputFile.readline() 
    count=count+1;
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
     
    if ((line[0]!='$') and (line[0]!='#')):
        line = line.replace("Avg Motor Current:", "");
        line = line.replace("HBridge Thermal:", "");
        line = line.replace("Exterior Motor Thermal:", "");        
        line = line.replace("\t", "");
        line = line.replace(" ", "");
                
        splitLine = line.split(',');
        if (len(splitLine)==9):
            
            if (fIsAllowedSpecificChar(splitLine[0]) == True):
                splitLine[0] = str(fAdjustTime(splitLine[0]))
                s = ",";
                line=s.join(splitLine)
                #print(line.strip() + "," + sArduinoValues[0]+ "," + sArduinoValues[1]+ "," + sArduinoValues[2]);
                outputFile.write(line.strip() + "," + sArduinoValues[0]+ "," + sArduinoValues[1]+ "," + sArduinoValues[2] + "\n")

        if (len(splitLine)==3):
            s = ",";
            line=s.join(splitLine)
            if (splitLine[0]!="nan"): sArduinoValues[0] = str(splitLine[0]);
            if (splitLine[1]!="nan"): sArduinoValues[1] = str(splitLine[1]);
            if (splitLine[2]!="nan"): sArduinoValues[2] = str(splitLine[2].strip());        
  
inputFile.close() 
outputFile.close()


# In[ ]:




