# cs50-DNA
#DNA without dictionary

from sys import argv
import re
import csv

#Total argv should be python + person + sequence = 3
if len(argv) != 3:
    print("Error: incorrect command line")
    exit(1)

#open file for sequence based on argv
#filesequence = open(argv[2], "r")

with open(argv[2], "r") as filesequence:
    AGATCmax = 0
    AGATCcurrent = 0

    TATCmax = 0
    TATCcurrent = 0

    AATGmax = 0
    AATGcurrent = 0

    sequence = filesequence.read() #copy text to sequence
    sequenceLength = len(sequence)
    for i in range(sequenceLength - 4): #keep going until last four values (min val for STR length)

        FivecharFromi = ""
        FourcharFromi = ""
        FivecharFromfive = ""
        FourcharFromfour = ""

        #get the text
        for j in range(5):
            if ((i+j) > sequenceLength): #this loop is for exiting once j has gone beyond the index; if i + j is more than the length of the sequence
                break
            else: #else if still ok
                FivecharFromi += sequence[i+j]
                if (i+5+j < sequenceLength):   #if still not out of range
                    FivecharFromfive += sequence[i+5+j]
                if j < 4:
                    FourcharFromi += sequence[i+j]
                    if (i+4+j < sequenceLength):   #if still not out of range
                        FourcharFromfour += sequence[i+4+j]

        #--------------------------------------------------------------------------------------------------------------------
        if (FivecharFromi == "AGATC"):
            AGATCcurrent += 1

            if (FivecharFromfive == "AGATC"): #Check if five char from five is AGATC
                if (AGATCcurrent > AGATCmax): #if current is more than max; if max is no longer max,
                    AGATCmax = AGATCcurrent   # current value to max(continuous) value.
            else:                             #If Fivecharfromfive is not AGATC; reach the end of the combo,
                if (AGATCcurrent > AGATCmax): #then, still check if current is more than max,
                    AGATCmax = AGATCcurrent   #but after copy the value, to max,
                AGATCcurrent = 0              #then set current value to 0

        #--------------------------------------------------------------------------------------------------------------------
        elif (FourcharFromi == "TATC"):
            TATCcurrent += 1

            if (FourcharFromfour == "TATC"): #Check if four char from four is TATC
                if (TATCcurrent > TATCmax): #if current is more than max; if max is no longer max,
                    TATCmax = TATCcurrent   # current value to max(continuous) value.
            else:                             #If Fourcharfromfour is not TATC; reach the end of the combo,
                if (TATCcurrent > TATCmax): #then, still check if current is more than max,
                    TATCmax = TATCcurrent   #but after copy the value, to max,
                TATCcurrent = 0              #then set current value to 0
        #---------------------------------------------------------------------------------------------------------------------
        elif (FourcharFromi == "AATG"):
            AATGcurrent += 1

            if (FourcharFromfour == "AATG"): #Check if four char from four is AATG
                if (AATGcurrent > AATGmax): #if current is more than max; if max is no longer max,
                    AATGmax = AATGcurrent   # current value to max(continuous) value.
            else:                             #If Fourcharfromfour is not AATG; reach the end of the combo,
                if (AATGcurrent > AATGmax): #then, still check if current is more than max,
                    AATGmax = AATGcurrent   #but after copy the value, to max,
                AATGcurrent = 0              #then set current value to 0

    print(AGATCmax, AATGmax, TATCmax)

    with open(argv[1], newline='') as filePeople:
        PersonData = csv.reader(filePeople) #read to a string file called PersonData
        Header = next(PersonData) #put first row in Header
        Person = [row for row in PersonData] #put each row into a list
        for row in Person:
            #compare and print result here
            AGATC = int(row[1])
            AATG = int(row[2])
            TATC = int(row[3])
            if ((AGATC == AGATCmax) and (AATG == AATGmax) and (TATC == TATCmax)):
                print(f"Found! It's {row[0]}")
                exit(0)
        #If a name is found, program will exit before this line
        print("Not found.")
