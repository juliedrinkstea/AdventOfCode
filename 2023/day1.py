import pandas as pd 
import regex as re


# Read the input CSV file
df = pd.read_csv(r'~/Documents/Python/aoc2023/i1.1.csv')

def get_first(input_col):
    for each in input_col:
        if each.isdigit():
            return int(each)
    return None

def get_last(input_col):
    for each in reversed(input_col):
        if each.isdigit():
            return int(each)
    return None

# Apply the functions to create new columns
df['first'] = df['input'].apply(get_first)
df['last'] = df['input'].apply(get_last)
df['coord1'] = df['first'].astype(str) + df['last'].astype(str)


#Part 2: Strings

word_map = {
    'eightwo': '8',
    'nineight': '9',
    'twone': '2',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

reversed_word_map = {

    'thgieerht': '8',
    'thgievif': '8',
    'enineves' : '9',
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9'
}


# Function to replace all possible matches of word_map values in a string using regex
#note -- this still went in dictionary order, so I ended up throwing in the towel 
#        and hardcoding the variables that overlap in spelling where order matters
def replace_all_occurrences(input_string):
    pattern = '|'.join(re.escape(word) for word in word_map.keys())
    repl_func = lambda match: word_map[match.group(0)]
    return re.sub(pattern, repl_func, input_string)

# Function to replace all possible matches of word_map values in a string using regex
#note -- this still went in dictionary order, so I ended up throwing in the towel 
#        and hardcoding the variables that overlap in spelling where order matters
def rev_replace_all_occurrences(input_string):
    pattern = '|'.join(re.escape(word) for word in reversed_word_map.keys())
    repl_func = lambda match: reversed_word_map[match.group(0)]
    return re.sub(pattern, repl_func, input_string)

df['find_first_2'] = df['input'].apply(replace_all_occurrences)
df['find_last_2'] = df.loc[:,'input'].apply(lambda x: x[::-1])
df['find_last_2'] = df['find_last_2'].apply(rev_replace_all_occurrences)
df['first2'] = df['find_first_2'].apply(get_first)
df['last2'] = df['find_last_2'].apply(get_first)
df['coord2'] = df['first2'].astype(str) + df['last2'].astype(str)


print(df.head())
print(df['coord1'].astype(int).sum())
print(df['coord2'].astype(int).sum())

