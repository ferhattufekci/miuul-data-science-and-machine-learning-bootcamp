############################################### Task 1 ##############################################################

# Using the List Comprehension structure, capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.

#     df = sns.load_dataset("car_crashes")
#     df.columns = [col.upper() for col in df.columns]
#     df.columns

#     Expected Output:

#     ['NUM_TOTAL',
#     'NUM_SPEEDING',
#     'NUM_ALCOHOL',
#     'NUM_NOT_DISTRACTED',
#     'NUM_NO_PREVIOUS',
#     'NUM_INS_PREMIUM',
#     'NUM_INS_LOSSES',
#     'ABBREV']

#     💡 The names of non-numeric variables should also grow.
#     💡 A single list comprehension structure should be used.

############################################### Task 1 Solution ###############################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
print(["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns])

############################################### Task 2 ##############################################################

# Using the List Comprehension structure, write "FLAG" at the end of the names of the variables that do not contain "number" in the car_crashes data.

#     Expected Output:

#     ['TOTAL_FLAG',
#     'SPEEDING_FLAG',
#     'ALCOHOL_FLAG',
#     'NOT_DISTRACTED',
#     'NO_PREVIOUS',
#     'INS_PREMIUM_FLAG',
#     'INS_LOSSES_FLAG',
#     'ABBREV_FLAG']

#     💡All variable names must be uppercase.
#     💡It should be done with a single list comprehension structure.

############################################### Task 2 Solution ###############################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
print([col.upper() + "_FLAG" if "NO" not in col.upper() else col.upper() for col in df.columns])

############################################### Task 3 ##############################################################

# Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.

#     og_list = ["abbrev","no_previous"]

#     Expected Output:

#     total  speeding  alcohol  not_distracted  ins_premium  ins_losses
#     18.8     7.332    5.640          18.048       784.55      145.08
#     18.1     7.421    4.525          16.290      1053.48      133.93
#     18.6     6.510    5.208          15.624       899.47      110.35
#     22.4     4.032    5.824          21.056       827.34      142.39
#     12.0     4.200    3.360          10.920       878.41      165.63

#     💡First, create a new list named new_cols using list comprehension according to the given list.
#     💡Then create a new df by selecting these variables with df[new_cols] and name it new_df.

############################################### Task 3 Solution ###############################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df.head())
#####################################################################################################################