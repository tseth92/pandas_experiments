# pandas_experiments
this repository contains pandas experiment where different pandas apis are checked for speed, performance or just functionality
#### pandas_iterator.py
1) Just run as python3 pandas_iterator.py. 
2) It shows the runtimes for 5000000 elements dataframe . 
3) A simple code was run in which for all the rows, if multiple of 5 is found , it is doubled
4) Result: You should never use normal for loop over dataframe or iterrows(not mentioned in this but is similar to itertuples)
5) itertuples is way much faster than for loop as it takes around 14-15 secs. 

**Important**: But you should almost always consider apply or list comprehensions as they are the fastest.

#### pandas_loc_iloc.py
1) Just run python3 pandas_loc_iloc.py
2) It shows the difference between loc and iloc functionality in pandas
3) While iloc requires the column in terms of numbers, loc requires the column actual labels. Moreover, iloc ignores slice last index included, loc includes ie. [2:4] : iloc ignores 3rd row/column(4 means third row) whereas loc doesn't
4) In terms of rows, the difference is seen when there is different index than the usual . To show that, I change the index numbers and we observe that while iloc considers the actual count of rows as the rows specified, whereas the loc considers the labels of index. eg. in iloc, [:3] means first three rows where as in loc, it means whenever 3 is found in index , it can be in any place instead of being at 3rd place
