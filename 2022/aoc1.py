import os
import pandas as pd

#create df from csv. Add header. Make sure not to skip the blank rows.
input = pd.read_csv('~/Documents/Python/aoc2022/aoc1.csv', names=['calories'],skip_blank_lines=False)

#change NaN in blank rows to 0
input.fillna(0,inplace=True)

# If calorie value is <1, we know it was one of the blank rows, so add a column we can group by. Increment group by 1 each time calories is <1
input['elf_num'] = (input['calories'] < 1).cumsum()+1

#create a df that groups by assigned elf number. Sum the other column (calories) per group.
sum_df = input.groupby(['elf_num']).sum()

#Sometimes I'll print things double check what is going on
#print(input_df.head(10))
#print(sum_df.head(10))
#print(sum_df[sum_df['calories']==sum_df['calories'].max()])


#part 1 answer
print(sum_df['calories'].max())
#part 2 answer
print(sum_df['calories'].nlargest(3).sum())
