'''
Created on Mar 12, 2018

@author: dz

'''
import csv
from operator import itemgetter

def typeone(midi):
    list = []
    for observation in midi:
        if observation[2] == "Note_on_c":
            observation.remove(observation[2])
            int(observation[0])
            int(observation[1])
            int(observation[2])
            int(observation[3])
            int(observation[4])
            print(observation)
            list.append(observation)
    list=list.sort(key=lambda elem:elem[4])
    with open('AfterYou.csv','w',newline='') as f:
        midifile = csv.writer(f)
        for row in list:
                midifile.writerow(row)
        

def typezero(midi):
    with open('hello.csv', 'w',newline='') as f:
        midifile = csv.writer(f)
        for observation in midi:
            if observation[2] == "Note_on_c":
                observation.remove(observation[2])
                observation.remove(observation[0])
                int(observation[0])
                int(observation[1])
                int(observation[2])
                int(observation[3])
                midifile.writerow(observation)

def sort(filename):
    list = []
    with open(filename) as csvfile:
        midi = csv.reader(csvfile,delimiter=',')
        for row in midi:
            newrow = []
            for element in row:
                element = str(element).strip()
                newrow.append(element)
            list.append(newrow)
    if list[0][3]== "0":
        typezero(list)
    if list[0][3]== "1":
        typeone(list)
    
        
if __name__ == '__main__':
    sort("data/AfterYou.csv")