import argparse
import matplotlib.pyplot as plt
import numpy as np

def getArgParserObj():
    parser = argparse.ArgumentParser(description="Sample Command::python bugfilter.py --priority High --assigne Priya --status TODO")

    # can use the args precisely for assinee/priority/status search
    
    # parser.add_argument('--priority', '-p',type=str,choices=["Highest","High","Medium","Low","Lowest"], help="please give one among these {Highest/High/Medium/Low/Lowest} to get the data based on Priority")
    # parser.add_argument('--assignee', '-a', type=str, help='Graph Based On Assignee')
    # parser.add_argument('--status', '-s', type=str,choices=["TODO","InProgress"], help='please give one among these {TODO/In Progress} to get the data based on Status')

    parser.add_argument('--assignee','-a',action='store_true')
    parser.add_argument('--priority','-p',action='store_true')
    parser.add_argument('--status','-s',action='store_true')
    return parser

def createPieChart(dictvalue):
    xaxis=[]
    yaxis=[]
    for key,value in dictvalue.items():
        xaxis.append(key)
        yaxis.append(len(value))
    x = np.char.array(xaxis)
    y = np.array(yaxis)
    porcent = 100.*y/y.sum()

    patches, texts = plt.pie(y,startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

    sort_legend = True
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

    plt.legend(patches, labels, bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
    plt.show()

    # plot can also save in png
    #plt.savefig('piechart.png', bbox_inches='tight')
