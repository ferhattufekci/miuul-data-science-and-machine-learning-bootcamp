import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Task 1: Identify the Titanic dataset from the Seaborn library.

df = sns.load_dataset('titanic')
df.head()
# sns.get_dataset_names()

# Task 2: Find the number of male and female passengers in the Titanic dataset.

df['sex'].value_counts()

male = df['sex'].value_counts()['male'] #['male'] is used because using [0] reduces readability.
male

# Task 3: Find the number of unique values for each column.

df.nunique()

# Task 4: Find the number of unique values of the variable pclass.

# 💡 There are multiple variable selection methods. If the variable names do not contain Turkish, special, or space characters, the df.pclass method is used.
df['pclass'] # data type pandas series.
df.pclass # data type pandas series.
df[['pclass']] # data type dataframe

df['pclass'].nunique()
df.pclass.unique()

# Task 5: Find the number of unique values of pclass and parch variables.

df[['pclass', "parch"]].nunique()

# Task 6: Check the type of the embarked variable.
# Change its type to category and check again.

#💡If there is a string type variable consisting of a small number of unique values, changing the data type to category provides memory advantage and processing speed.


df['embarked'].dtype

df.info()
df.head()

df['embarked'] = df['embarked'].astype('category')


# Task 7: Show all information of those with embarked value C..

df[df['embarked'] == 'C'].head()
df.head()

# Task 8: Show all information of those whose embarked value is not S.

df[df['embarked'] != 'S']
df[~(df['embarked'] == 'S')]

# Task 9: Show all the information for female passengers younger than 30 years old.

df[(df['age'] < 30) & (df['sex'] == 'female')].head()


# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df[(df['fare'] > 500) | (df['age'] > 70)].head()

# Task 11: Find the sum of the null values in each variable.

df.isnull().sum()
df.isna().sum()

df.isnull()

int(True + True)

df.shape[0]

# Task 12: remove the who variable from the dataframe.

df.head()
df.drop('who', axis=1, inplace=True)


# Task 13: Fill the empty values in the deck variable with the most repeated value (mode) of the deck variable.

df['deck'].fillna(df['deck'].mode()[0], inplace=True)

df['deck'].value_counts().index[0]

df.isnull().sum()

# Task 14: Fill in the blank values in the age variable with the median of the age variable.

df['age'] = df['age'].fillna(df['age'].median())

# Task 15: Find the sum, count, mean values of the pclass and gender variables of the survived variable.

df.groupby(['pclass', "sex"]).agg({'survived': ['sum', 'count', 'mean']})
# df.groupby(['pclass', "sex"])['survived'].mean()

# Task 16: Write a function that returns 1 for those under 30, 0 for those above or equal to 30.
# Create a variable named age_flag in the titanic dataset using the function you wrote.
# (use apply and lambda constructs)

df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)
df.head()

df[df.embark_town.isnull()]

# Task 17: Define the Tips dataset from the Seaborn library.

df = sns.load_dataset('tips')
df.head()

# Task 18: Find the sum, min, max and average of the total_bill values according to the categories (Dinner, Lunch) of the Time variable.

df.groupby('time').agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count']})

# df.groupby("time")["total_bill"].agg(["sum","min","max","mean"])

# Task 19: Find the sum, min, max and average of total_bill values by days and time..


df.groupby(['day','time']).agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count']})

# Task 20: Find the sum, min, max and average of the total_bill and type values of the lunch time and female customers according to the day.


df_female_lunch = df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]
df_female_lunch.groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count'],
                                    'tip': ['sum', 'min', 'max', 'mean', 'count']})


# Task 21: What is the average of orders with size less than 3 and total_bill greater than 10? (use loc)

df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()


# Task 22: Create a new variable called total_bill_tip_sum.
# Give the sum of the total bill and tip paid by each customer.

df['total_bill_tip_sum'] = df['tip'] + df['total_bill']
df.head()

# Task 23: Sort by total_bill_tip_sum variable from largest to smallest
# and assign the first 30 contacts to a new dataframe

df_top30 = df.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
df_top30

# df.sort_values(by='total_bill_tip_sum', ascending=False).iloc[:30]