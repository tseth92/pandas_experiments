# pandas_experiments
this repository contains pandas experiment where different pandas apis are checked for speed, performance or just functionality
#### pandas_iterator.py
1) Just run as python3 pandas_iterator.py. 
2) It shows the runtimes for 5000000 elements dataframe . 
3) A simple code was run in which for all the rows, if multiple of 5 is found , it is doubled
4) Result: You should never use normal for loop over dataframe or iterrows(not mentioned in this but is similar to itertuples)
5) itertuples is way much faster than for loop as it takes around 14-15 secs. 

**Important**: But you should almost always consider apply or list comprehensions as they are the fastest.
