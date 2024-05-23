import csv
from collections import defaultdict

def returndictvalues(list1,list2):
    d = defaultdict(list)
    for key, value in zip(list1,list2):
        d[key].append(value)
    return d

    
class csvreader:
    def __init__(self,csvfile):
        self.csvfile = csvfile
        self.IssueType=[]
        self.IssueKey=[]
        self.summary=[]
        self.Assignee=[]
        self.Reporter=[]
        self.Priority=[]
        self.status=[]
        self.created=[]
        self.updated=[]
        self.FixVersions=[]

        with open(self.csvfile,'r') as cfile:
            records = csv.reader(cfile, delimiter = ',')
            next(records)
            for record in records:
                self.IssueType.append(record[0])
                self.IssueKey.append(record[1])
                self.summary.append(record[2])
                self.Assignee.append(record[3])
                self.Reporter.append(record[4])
                self.Priority.append(record[5])
                self.status.append(record[6])
                self.created.append(record[7])
                self.updated.append(record[8])
                self.FixVersions.append(record[9])
            


    def getassigneNames(self):
        return returndictvalues(self.Assignee,self.IssueKey)     
        
    def getstatus(self):
        return returndictvalues(self.status,self.IssueKey) 

    def getpriority(self):
        return returndictvalues(self.Priority,self.IssueKey)