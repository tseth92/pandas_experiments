'''
The below code creates a dataframe with two columns A and B with 5000000
entries in the dataframe.
Then a comparison of different iterators is done in different methods. 
Each code checks for the multiple of 5 in B column and doubles it if it 
is found
'''
import pandas as pd
import time

df_test = pd.DataFrame()
tlist = []
tlist2 = []

################ this code creates a dataframe df_test ##################
###############with two columns and 5000000 entries #####################
for i in range (0,5000000):
  tlist.append(i)
  tlist2.append(i+5)
df_test['A'] = tlist
df_test['B'] = tlist2
#########################################################################
######################### Done creating DF ##############################


#########################################################################
################## Using itertuples around 15 secs#######################
'''
check if multiple of 5 in column B and doubles it using itertuples
iterrows is very slow and hence we are not considering it and it is similar
to itertuples but very very slow
'''
def dtst_itertuples():
    startTime = time.time()
    for row in df_test.itertuples():
        x = row.B
        if x%5==0:
            df_test.at[row.Index,'B'] = x*2
    print("--Itertuples-- time of completion: ", (time.time()-startTime))
######################### end itertuples  ##############################
########################################################################




########################################################################
################### Using normal for loop ##############################
'''
check if multiple of 5 in column B and doubles it using normal for loop
'''
def dtst_for_normal():
    startTime = time.time()
    for i in range (0,5000000):
        x = df_test.loc[i,'B']
        if x%5==0:
          df_test.loc[i,'B'] = x*2
    print("--Normal for-- time of completion: ", (time.time()-startTime))
######################## takes minutes. Never use ######################
####################***************************#########################



########################################################################
######################## Using apply ###################################
'''
check if multiple of 5 in column B and doubles it using apply
'''
def dtst_apply():
    startTime = time.time()
    df_test['B'] = df_test['B'].apply(lambda x: x*2 if x%5==0 else x)
    print("--Apply--time of completion: ", (time.time()-startTime))
#################### takes around 1-2 seconds ########################
#################***********************************##################




#######################################################################
######################## List Comprehension ###########################
'''
check if multiple of 5 in column B and doubles it using list 
comprehensions
'''
def dtst_list_comprehension():
    startTime = time.time()
    df_test['B'] = [ x*2 if x%5==0 else x for x in df_test['B']]
    print("--ListComp--time of completion: ", (time.time()-startTime))
###################### Done List Comprehension #########################
#########****************** 1-2 seconds ************####################




if __name__ == "__main__":
    #dtst() # don't use it . its very slow, will complete in minutes
    dtst_itertuples() # relatively faster than for loop and itertuples , still very slow
    dtst_apply() # relatively very fast
    dtst_list_comprehension() # relatively very fast , comparable to apply
    print(df_test.head(5))
