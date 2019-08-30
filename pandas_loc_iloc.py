'''
This code compares the loc and iloc in pandas dataframe
'''
import pandas as pd
import timeit
df_test = pd.DataFrame()
tlist = []
tlist2 = []


################ this code creates a dataframe df_test ##################
###############with two columns and 5000000 entries #####################
for i in range (0,50):
  tlist.append(i)
  tlist2.append(i+5)
df_test['A'] = tlist
df_test['B'] = tlist2

print('Original Dataframe:')
print(df_test.head(5))
print("-----------------")
######################### Done creating DF ##############################



############################ iloc #######################################
print('iloc dataframe: 3rd row and 1st to 2nd column:')
# since iloc ignores the last part of slice 
# iloc works with only numbers for columns
print(df_test.iloc[2:3,0:2])
print("-----------------")
print('loc dataframe: 3rd row and 1st to 2nd column:')
# since loc includes the last part of slice
# loc works with only column names
print(df_test.loc[2:3,['A','B']])
print("-----------------")
######################### Done iloc ####################################



##########*******************************************####################
  # ***** Observing loc and iloc when index is different ********** #
##########*******************************************####################

'''
Now the index is altered for dataframe which gives the actual difference
between what loc and iloc varies with in terms of rows. while iloc works 
by checking index number and counting from start, loc works by checking 
where the index label comes. eg. index: (4,5,6,1,2), iloc considers 2 
index at 2nd position whereas loc considers it at  5th position
'''

############################### changing index ##########################
as_list = df_test.index.tolist()
print(as_list[3:7])
as_list[0:5] = [63,64,65,66,67]
for i in range(5,len(as_list)):
    as_list[i] = as_list[i]-5 
df_test.index = as_list
########################################################################
print('-----------------Dataframe after index updated -------------- ')
print(df_test.head(10))
print('-------------- iloc dataframe with updated index-------------')
print(df_test.iloc[:7]) # iloc watches for 7 index counts from start
print('-------------- loc dataframe with updated index-------------')
print(df_test.loc[:7]) # loc watches for index=7 where it appears
