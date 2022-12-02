import os
import pandas as pd

#create df from csv. Add header. Make sure not to skip the blank rows.
input = pd.read_csv('~/Documents/Python/aoc2022/aoc1.csv', names=['calories'],skip_blank_lines=False)

#change NaN in blank rows to 0
input.fillna(0,inplace=True)

# Add a column to group by. Increment group by 1 each time calories is <1
input['elf_num'] = (input['calories'] < 1).cumsum()+1

#create a df that groups by assigned elf number. Sum the other column (calories) per group.
sum_df = input.groupby(['elf_num']).sum()


#part 1 answer
print(sum_df['calories'].max())
#part 2 answer
print(sum_df['calories'].nlargest(3).sum())
