import datetime
import calendar
import csv
import sys
from decimal import Decimal

def row_as_dict(data, columns):
    result = []
    for row in data:
        i=0
        items={}
        for col in row:
            if (i > -1):
                column_name = columns[i]
                items[column_name] = str(col)
            i=i+1
        result.append(items)
    return result

def waitKeyPress(waitMessage):
    waitForKeyPress = input(waitMessage + " (Press a key to continue).")

def dateStringToObject(stringDate):
    if stringDate is None:
        return None
    return datetime.datetime.strptime(stringDate, '%Y-%m-%d')

def dateObjectToString(objectDate):
    if objectDate is None:
        return None
    return objectDate.strftime('%Y-%m-%d')

def dateStringCompare(stringDate1, comparisonStr, stringDate2):
    objDate1 = dateStringToObject(stringDate1)
    objDate2 = dateStringToObject(stringDate2)
    switcher = {
        "==": objDate1 == objDate2,
        "<": objDate1 < objDate2,
        "<=": objDate1 <= objDate2,
        ">": objDate1 > objDate2,
        ">=": objDate1 >= objDate2,
        "!=": objDate1 != objDate2
    }
    return switcher[comparisonStr] #the comparisonStr will be looked up in switcher dict to get true/false value

#This helper function is used to check if a string date is between 2 string dates
def dateStringInDateRange(theStringDate, stringDateStart, stringDateEnd):
    return dateStringCompare(theStringDate, ">=", stringDateStart) and dateStringCompare(theStringDate,"<=", stringDateEnd)

#used to pretty print a dictionary
def printDictData(dictData):
    print()
    for keys, values in dictData.items():
        print(keys, ':', values)

#used to print a dictionary in CSV form, so you can cut/paste to view it in Excel as a table
# keyFieldTuples are the field names used in the dictionary's keys (usually just 1 field)
# valueFieldTuples are the field names used in dictionary's values (usually many fields)
#Example Call: printDictInCSVFormat(holidays.dict, ('date',), ('holidayName', 'numberDaysOff'))
def printDictInCSVFormat(dictData, keyFieldTuples, valueFieldTuples ):
    print()
    if keyFieldTuples is not None:
        for i in range(len(keyFieldTuples)):
            if (i==0):
                print(keyFieldTuples[i], end='')
            else:
                print(",", keyFieldTuples[i], end = '')

    for i in range(len(valueFieldTuples)):
        if keyFieldTuples is None and (i == len(valueFieldTuples)-1 and i == 0):
            print(valueFieldTuples[i])
        elif keyFieldTuples is None and i == 0:
            print(valueFieldTuples[i], end='')
        else:
            if (i == len(valueFieldTuples)-1):
                print(",", valueFieldTuples[i])
            else:
                print(",", valueFieldTuples[i], end='')

    for keys, values in dictData.items():
        if keyFieldTuples is not None:
            keyLength = len(keyFieldTuples)
        else:
            keyLength = 0
        if (keyLength == 1):
            print(keys, end='')
        else:
            for i in range(keyLength):
                if (i == 0):
                    print(keys[i], end='')
                else:
                    print(",", keys[i], end='')
        for i in range(len(valueFieldTuples)):
            if keyFieldTuples is None and (i == len(valueFieldTuples) - 1 and i == 0):
                print(values[valueFieldTuples[i]])
            elif keyFieldTuples is None and i == 0:
                print(values[valueFieldTuples[i]], end='')
            elif (i == len(valueFieldTuples) - 1):
                print(",", values[valueFieldTuples[i]])
            else:
                print(",", values[valueFieldTuples[i]], end='')
                
def printCSVLineItem(datas, columns):
    for col in columns:
        if col != columns[-1]:
            print("{}, ".format(col),end="")
        else:
            print("{}".format(col))
    for data in datas:
        for value_indx in range(len(data)):
            if value_indx != len(data)-1:
                print("{}, ".format(data[value_indx]),end="")
            else:
                print("{}".format(data[value_indx]))

def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' , '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))
