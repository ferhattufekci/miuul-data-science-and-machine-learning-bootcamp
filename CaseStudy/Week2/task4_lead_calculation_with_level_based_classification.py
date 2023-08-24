#############################################
# Lead Calculation with Level-Based Classification
#############################################

#############################################
# Business Problem
#############################################
# A game company wants to create level-based new customer definitions (persona) by using some features of its customers, and to create segments according to these new customer definitions and to estimate how much the new customers can earn on average according to these segments.

# For example: It is desired to determine how much a 25-year-old male user from Turkey who is an IOS user can earn on average.


#############################################
# Dataset Story
#############################################
# Persona.csv dataset contains the prices of the products sold by an international game company and some demographic information of the users who buy these products. The data set consists of records created in each sales transaction. This means that the table is not deduplicated. In other words, a user with certain demographic characteristics may have made more than one purchase.

# Price: Customer's spending amount
# Source: The type of device the customer is connecting to
# Sex: Gender of the client
# Country: Country of the customer
# Age: Customer's age

################# Before Application #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# After Application #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJECT TASKS
#############################################

#############################################
# TASK 1: Answer the following questions.
#############################################
import pandas as pd

# Question 1: Read the persona.csv file and show the general information about the dataset.
df = pd.read_csv('../dataset/persona.csv')

df.info()
df.head()
df.tail()
df.describe().T
df.shape
df.columns
df.index
df.isnull().values.any()

# Question 2: How many unique SOURCE are there? What are their frequencies?

df['SOURCE'].unique()
df['SOURCE'].value_counts()

# Question 3: How many unique PRICEs are there?

df.PRICE.nunique()

# Question 4: How many sales were made from which PRICE?

df.PRICE.value_counts()

# Question 5: How many sales were made from which country?

df.COUNTRY.value_counts()

# Question 6: How much was earned in total from sales by country?

df.groupby('COUNTRY').agg({'PRICE': 'sum'})
# df.groupby('COUNTRY')['PRICE'].sum()

# Question 7: What are the sales numbers by SOURCE types?

df.SOURCE.value_counts()


# Question 8: What are the PRICE averages by country?

df.groupby('COUNTRY').agg({'PRICE': 'mean'})

# Question 9: What are the PRICE averages by SOURCEs?

df.groupby(['SOURCE']).agg({'PRICE': 'mean'})

# Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?

df.groupby(['SOURCE', 'COUNTRY']).agg({'PRICE': 'mean'})


#############################################
# TASK 2: What are the average earnings in breakdown of COUNTRY, SOURCE, SEX, AGE?
#############################################

agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE']).agg({'PRICE': 'mean'})


#############################################
# TASK 3: Sort the output by PRICE.
#############################################
# Apply the sort_values method to PRICE in descending order to see the output in the previous question better.
# Save the output as agg_df.

agg_df.sort_values('PRICE', ascending=False)

len(agg_df.columns)
#############################################
# TASK 4: Convert the names in the index to variable names.
#############################################
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names.
# Hint: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()
agg_df.columns


#############################################
# TASK 5: Convert AGE variable to categorical variable and add it to agg_df.
#############################################
# Convert the numeric variable age to a categorical variable.
# Construct the intervals as you think will be persuasive.
# For example: '0_18', '19_23', '24_30', '31_40', '41_70'

# Let's specify where the AGE variable will be divided:

my_bins = [0, 18, 23, 30, 40, agg_df['AGE'].max()]

# Let's express what the nomenclature will be for the dividing points:

mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df['AGE'].max())]
# mylabels = ['0_18', '19_23', '24_30', '31_40', f'41_{agg_df["AGE"].max()}']

# divide age:
pd.cut(agg_df['AGE'], bins=my_bins, labels=mylabels)

agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=my_bins, labels=mylabels)
agg_df.head()

#############################################
# TASK 6: Identify new level based customers and add them as variables to the dataset.
#############################################
# Define a variable named customers_level_based and add this variable to the dataset.
# Attention!
# After creating customers_level_based values with list comp, these values need to be deduplicated.
# For example, more than one of the following expressions: USA_ANDROID_MALE_0_18
# It is necessary to take them to groupby and get the price average.
agg_df.drop(['AGE', 'PRICE'], axis=1).values

liste = ['A', 'B', 'C']
'-'.join(liste)

agg_df["CUSTOMERS_LEVEL_BASED"] = ["_".join(i).upper() for i in agg_df.drop(['AGE', 'PRICE'], axis=1).values]
agg_df

# ["{}_{}_{}_{}".format(x.upper(),y.upper(),z.upper(),k) for x,y,z,k in zip(agg_df["COUNTRY"],agg_df["SOURCE"],agg_df["SEX"],agg_df["AGE_CAT"])]

# agg_cols=["COUNTRY","SOURCE","SEX","AGE_CAT"]

# [col[0].upper()+"_"+col[1].upper()+"_"+col[2].upper()+"_"+col[3].upper() for col in agg_df[agg_cols].values ]

# agg_df['COUNTRY'].astype(str) + "_" + \
# agg_df['SOURCE'].astype(str) + "_" + \
# agg_df['SEX'].astype(str) + "_" + \
# agg_df['AGE_CAT'].astype(str)

# Let's remove the unnecessary variables:

agg_df.head()
agg_df = agg_df[['CUSTOMERS_LEVEL_BASED', 'PRICE']]

agg_df = agg_df.groupby('CUSTOMERS_LEVEL_BASED')['PRICE'].mean().reset_index()

###



# We are one step closer to our goal.
# There is a small problem here. There will be many identical segments.
# can be many numbers from segment USA_ANDROID_MALE_0_18, for example.
# let's check:

# For this reason, after groupby according to the segments, we should get the price averages and deduplicate the segments.


#############################################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
#############################################
# Segment by PRICE,
# add segments to agg_df with the naming "SEGMENT",
# describe the segments,

[23, 27, 34, 34, 35, 39, 41, 48]

agg_df['SEGMENT'] = pd.qcut(agg_df.PRICE, q=4, labels=['D', 'C', 'B','A'])
agg_df.head()

agg_df.groupby('SEGMENT').agg({'PRICE': 'mean'}).reset_index()

agg_df['PRICE'].corr()

#############################################
# TASK 8: Classify the new customers and estimate how much income they can bring.
#############################################
# Which segment does a 33-year-old Turkish woman using ANDROID belong to and how much income is expected to earn on average?

new_user = 'TUR_ANDROID_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user]

# In which segment and on average how much income would a 35 year old French woman using iOS expect to earn?

new_user = 'FRA_IOS_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user]
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == 'BRA_ANDROID_FEMALE_0_18']


df[['PRICE', 'AGE']].corr()