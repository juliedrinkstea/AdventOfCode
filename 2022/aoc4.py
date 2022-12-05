# 2022.12.04 AOC
import os
import pandas as pd

#read the csv input
input = pd.read_csv('~/Documents/Python/aoc2022/aoc4.csv', names=['pairs'])

#split column on delimiter, keep original column. Split areas into high and low values to set up for range()
input[['area1','area2']] = input['pairs'].str.split(',',expand=True)
input[['low1','high1']] = input['area1'].str.split('-',expand=True)
input[['low2','high2']] = input['area2'].str.split('-',expand=True)

#cast to numbers
input['low1']= pd.to_numeric(input['low1'])
input['high1']= pd.to_numeric(input['high1'])
input['low2']= pd.to_numeric(input['low2'])
input['high2']= pd.to_numeric(input['high2'])

#method to see if ranges contain eachother. Add +1 to high number since .range() doesn't include stop number
def in_range(input):
    if set(range(input['low1'],input['high1']+1)).issubset(range(input['low2'],input['high2']+1)):
        return 1
    elif set(range(input['low2'],input['high2']+1)).issubset(range(input['low1'],input['high1']+1)):
        return 1
    else:
        return 0
#apply to df
input['contains'] = input.apply(in_range, axis=1)

#sum and print answer to part 1
print("Round 1 Answer: " + str(input['contains'].sum()))

#method for overlap
def overlap(input):
    if (input['high1'] >= input['low2']) and (input['high2'] >= input['low1']):
        return 1
        
#apply to df
input['overlap'] = input.apply(overlap, axis=1)

#sum and print answer to part 2
print("Round 2 Answer: " + str(input['overlap'].sum()))
