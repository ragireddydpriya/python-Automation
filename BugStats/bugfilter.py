import csv
import os
from os.path import isfile
from csvreader import csvreader
import utils as utils

def createGraphBasedOnAssignee(list):
    utils.createPieChart(list.getassigneNames())
            
def createGraphBasedOnPriority(list):
    utils.createPieChart(list.getpriority())

def createGraphBasedOnStatus(list):
    utils.createPieChart(list.getstatus())


if __name__=="__main__":
    if os.path.isfile('Bug-filter.csv'):
        parser = utils.getArgParserObj()
        args = parser.parse_args()
        list = csvreader('Bug-filter.csv')
        if args.assignee:
            createGraphBasedOnAssignee(list)
        elif args.priority:
            createGraphBasedOnPriority(list)
        elif args.status:
            createGraphBasedOnStatus(list)
        else:
            print('No Option Given,please give either -a or -p or -s to see the trends')

    else:
        print (" CSV File not exist,please add the file and rename it to Bug-filter.csv")