# 2022.12.05 AOC
import os
import pandas as pd

# #read the csv input

# I eventually gave up on crates and hard coded them.
# #crates = pd.read_csv('~/Documents/Python/aoc2022/aoc5.1.csv')

moves = pd.read_csv('~/Documents/Python/aoc2022/aoc5.2.csv', names = ['moves'] )

crates = [['b', 's', 'j', 'z', 'v', 'd', 'g'],
['p', 'v', 'g', 'm', 's', 'z'],
['f', 'q', 't', 'w', 's', 'b', 'l', 'c'],
['q', 'v', 'r', 'm', 'w', 'g', 'j', 'h'],
['d', 'm', 'f', 'n', 's', 'l', 'c'],
['d', 'c', 'g', 'r'],
['q', 's', 'd', 'j', 'r','t','g','h'],
['v', 'f', 'p'],
['j', 't', 's','r','d']]


#For loop; extract integers by splitting on delimiter and returning index reference 
#shuffle list values around the array accordingly, print first val in each
for m in moves['moves']:
    m = m.split(' ')
    amt = int(m[1])
    start = int(m[3])-1
    finish = int(m[5])-1
    move = crates[start][:amt]
    crates[start] = crates[start][amt:]
    crates[finish] = move + crates[finish]
print("Part 1:" + "".join([i[0] for i in crates]).upper())
#Input is apparently case sensitive. Added upper()

#Same thing, but reverse the order of insert into the shuffled list
for m in moves['moves']:
    m = m.split(' ')
    amt = int(m[1])
    start = int(m[3])-1
    finish = int(m[5])-1
    move = crates[start][:amt]
    crates[start] = crates[start][amt:]
    move.reverse()
    crates[finish] = move + crates[finish]
print("Part 2:" + "".join([i[0] for i in crates]).upper())
