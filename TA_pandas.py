# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:37:09 2019

@author: Charlemagne Jones

===================================================
Data Manipulation via Pandas - Testing

--Parts & Options
1. prompting for which particular csv or excel files which are to be used...
    a. needs to differentiate what kind of file is being used...
    b. must be able to either find the file path involved, or copy the file into the same folder as the script
2. once read, gives user a list of the columns / rows involved...basically a small sneak peak of the file involved
3. Give user several options for specific columns: ADD, SUBTRACT, AVERAGE, MULTIPLY, DIVIDE, MERGE, EXTRACT, etc...
    a. Will probably have to make classes for this...
    b. will probably need a TOC for better presentation...
4. Provide a way to check work or accuracy of new numbers...
5. provide way to export new file and way to rename said file...


"""
#TEST! 
#print("HELLOOWWWWW UWU")

import pandas as pd

# found formatting solution for floating numbers online: < https://stackoverflow.com/questions/38689125/how-to-get-rid-of-pandas-converting-large-numbers-in-excel-sheet-to-exponential >
pd.options.display.float_format = '{:.3f}'.format

#***************************  1  ************************************

#dataname1 = input("What is the name of the file?\n") + ".xlsx"
#df = pd.read_excel(dataname1)
#print(df)

#********************************************************************

# FUNCTIONS

#def add():
    # function to add
    
#def subt():
    # function to subtract
   
#def sum():
    #function to sum


    




df = pd.read_excel("TA_data1.xlsx")
print(df)

for col in df.columns:
    print(col)

print("============================================================")

df2 = df.groupby("Client")["Net Revenue"].sum() 
print(df2)

#df2.to_excel("test.xlsx",sheet_name = 'Client Net Revenue')

print("============================================================")

df3 = df.groupby("Client Type")["Net Revenue"].sum() 
print(df3)

print("============================================================")

df4 = df.groupby("Accrual Account")["Net Revenue"].sum() 
print(df4)

print("============================================================")

new_file_name = input("What would you like to name this file? Include .xlsx\n")

with pd.ExcelWriter(new_file_name) as writer:
    df2.to_excel(writer, sheet_name='Client_NetRevenue')
    df3.to_excel(writer, sheet_name='ClientType_NetRevenue')
    df4.to_excel(writer, sheet_name='AccrualAccount_NetRevenue')



















