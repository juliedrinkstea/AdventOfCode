# 2022.12.02 AOC
import os
import pandas as pd

#read the csv input, add a header
df = pd.read_csv('~/Documents/Python/aoc2022/aoc2.csv', names=['play'])

#split column on delimiter, keep original column
df[['them','me']] = df['play'].str.split(' ',expand=True)

# Replace rock, paper, scissors key with number. 
# In this case, the number can be both the point value and a unique id to identify the action
df['them'] = df['them'].replace(['A', 'B', 'C'], [1, 2, 3])
df['me'] = df['me'].replace(['X', 'Y', 'Z'], [1, 2, 3])

#Define how to score scenario 1
def outcome1(df):
    # If we play the same thing, return the value of my action plus 3 for a tie
    if (df['them'] == df['me']):
        return (df['me'] + 3)
    # Determine conditions where I win, return the value of my action plus 6 for a win
    elif (df['them'] == 1 and df['me'] == 2) or (df['them'] == 2 and df['me'] == 3) or (df['them'] == 3 and df['me'] == 1):
        return (df['me'] + 6)
    # If I lose, return the value of my action
    else:
        return df['me']

#Add the score from the outcome1 function to a new column
df['score1'] = df.apply(outcome1, axis=1)

#Print the sum of the score1 column
print("Round 1 Answer: " + str(df['score1'].sum()))


#Define how to score scenario 2
def outcome2(df):
    # If I need to draw, I can get the value of my play by copying the value of theirs plus 3 for the draw
    if (df['me'] == 2):
        return (df['them'] + 3)
    #Win; they play rock or paper. I can get the value of my play by adding 1 to their play, plus 6 for the win
    elif (df['them'] == 1 and df['me'] == 3) or (df['them'] == 2 and df['me'] == 3):
        return (df['them'] + 1 + 6) 
    #Win; they play scissors so I play rock. Simple 1 for rock plus 6 for the win for a total of 7
    elif (df['them'] == 3 and df['me'] == 3):
        return 7
    #lose, I play rock or paper. I can get the value of my play by subtracting 1 from their play. No points for a lose.
    elif (df['them'] == 2 and df['me'] == 1) or (df['them'] == 3 and df['me'] == 1):
        return (df['them'] - 1) 
    #lose, I play scissors for 3 points. No points for a lose.
    else:
        return 3

#Add the score from the outcome2 function to a new column
df['score2'] = df.apply(outcome2, axis=1)

#Print the sum of the score2 column
print("Round 2 Answer: " + str(df['score2'].cumsum().max()))
