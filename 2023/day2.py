import pandas as pd 
import re

# Read the input CSV file
df = pd.read_csv(r'~/Documents/Python/aoc2023/i2.csv')

#define method to get game number; split 'Game #:' from the game play, call with 0 index
def get_game_num(input):
    for each in input:
        game_columns = input.split(":")
        for each in game_columns[0]:
                return re.sub(r'Game ','', game_columns[0])

#list of colors for below method
colors = ['green', 'blue', 'red']

# Define a function to extract the maximum number for a given color
def extract_max_number(input_string, color):
    pattern = r'\d+ ' + color
    matches = re.findall(pattern, input_string)
    if matches:
        numbers = [int(match.split()[0]) for match in matches]
        return max(numbers)
    else:
        return None

#apply the function to get the game number
df['game_num'] = df['input'].apply(get_game_num)

#make a column with the max value for each color
for each in colors:
    df[each + '_max'] = df['input'].apply(lambda x: extract_max_number(x, each))


#print(df.head())
print(df.loc[(df['red_max'] <= 12) & (df['green_max'] <= 13) & (df['blue_max'] <= 14), 'game_num'].astype(int).sum())            

####Part 2
#easy peasy. Just multiply the color max columns and sum the result
print(sum(df['green_max'] * df['red_max'] * df['blue_max']))
