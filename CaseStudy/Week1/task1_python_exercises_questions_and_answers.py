############################################### Task 1 ##############################################################

# Examine the data structures of the given values.

#     x = 8
#     y = 3.2
#     z = 8j + 18
#     a = "Hello World"
#     c = 23 < 22
#     l = [1,2,3,4]
#     d = {"Name":"Jake","Age":27,"Adress":"Downtown"}
#     t = ("Machine Learning","Data Science")
#     s = {"Python","Machine Learning","Data Science"}
#
#     💡 Use the Type() method. Type() method: says; If you ask me for an object, it says, I will give its type information.

############################################### Task 1 Solution ###############################################

x = 8  # int
type(x)
y = 3.2  # float
type(y)
z = 8j + 18  # complex
type(z)
a = "Hello World"  # str
type(a)
c = 23 < 22  # bool
type(c)
l = [1, 2, 3, 4]  # list
type(l)
d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}  # dict
type(d)
t = ("Machine Learning", "Data Science")  # tuple
type(t)
s = {"Python", "Machine Learning", "Data Science"}  # set
type(s)

############################################### Task 2 ##############################################################

# Convert all letters of the given string to uppercase. Put space instead of commas and periods, and separate them word by word.

#     text = "The goal is to turn data into information, and information into insight."

#  Expected output:

#     ['THE','GOAL','IS','TO','TURN','DATA','INTO','INFORMATION','AND','INFORMATION','INTO','INSIGHT']

#     💡 Use string methods.
#           💡upper(): Used for large conversions. Use of: string_expression_variable.upper()
#           💡replace(): used for character replacement. string_expression_variable.replace("l", "p") This command replaces the l character with the p character.
#           💡split(): used for separation. Its default value is space. If no value is entered, it divides by spaces. string_expression_variable.split()  output: returns an array, dividing by space.


############################################### Task 2 Solution ###############################################

text = "The goal is to turn data into information, and information into insight."
uppercase_text = text.upper()
comma_free_uppercase_text = uppercase_text.replace(",", " ")
capitalized_text_without_commas = comma_free_uppercase_text.replace(".", " ")
no_comma_dot_uppercase_word_word_written_text = capitalized_text_without_commas.split()
print(no_comma_dot_uppercase_word_word_written_text)

# The solution by writing task 2 in one line: text.upper.replace(","," ").replace(".", "").split()

############################################### Task 3 ##############################################################

# Follow the steps below to the given list.

#     lst = ["D","A","T","A","A","S","C","I","E","N","C","E"]
#     Step 1: Look at the number of elements of the given list.
#            💡len(string expression/variable): It gives me the information of how many elements string expression/variable consists of.
#     Step 2: Call the elements at index zero and ten.
#     Step 3: Create a list ["D", "A", "T", "A"] from the given list.
#     Step 4: Delete the element at the eighth index.
#            💡list.pop(index) : It deletes whatever is in list 's index .
#     Step 5: Add a new element.
#            💡list.append(expression to add): adds a new element to the end of the list.
#     Step 6: Add the "N" element again to the eighth index.
#            💡list.insert(index,to be appended expression): Adds an element to index .

############################################### Task 3 Solution ###############################################

lst = ["D", "A", "T", "A", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1 Solution
print(len(lst))

# Step 2 Solution
lst[0]
lst[10]
# Step 2 One Line Solution
lst[0::10]

# Step 3 Solution
lst2 = lst[0:4]
print(lst2)

# Step 4 Solution
lst.pop(8)
print(lst)

# Step 5 Solution
lst.append("F")
print(lst)

# Step 6 Solution
lst.insert(8, "N")
print(list)

############################################### Task 4 ##############################################################

 # Apply the following steps to the given dictionary structure.

 #    dict = {'Christian':["America",18],
 #            'Daisy':["England",12],
 #            'Antonio':["Spain",22],
 #            'Dante':["Italy",25]}

 #    Step 1: Access the key values.
 #         💡dictioanary.keys(): It is used to access all keys of dictionary.
 #    Step 2: Access the values.
 #         💡dictionary.values(): It is used to access all the values of the dictionary.
 #    Step 3: Update the value 12 of the Daisy key to 13.
 #         💡dictionary.update():It is used to update the key and value or add a new value. If there is no value, it creates it. update if any.
 #    Step 4: Add a new value whose key is Ahmet and the value is [Turkey,24].
 #         💡dictionary.update():It is used to update the key and value or add a new value. If there is no value, it creates it. update if any.
 #    Step 5: Delete Antonio from dictionary.

############################################### Task 4 Solution ###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Step 1 Solution
print(dict.keys())

# Step 2 Solution
print(dict.values())

# Step 3 Solution
dict["Daisy"][1] = 13  # dict.update({"Daisy": ["England",13]})
print(dict)

# Step 4 Solution
dict2 = {"Ahmet": ["Turkey", 24]}
dict.update(dict2)
print(dict)

# Step 5 Solution
dict.pop("Antonio")  # del dict["Antonio"]
print(dict)

############################################### Task 5 ##############################################################

# Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns those lists.

#     l = [2,13,18,93,22]
#     def func(..):
#         ...
#         ...
#         return ..

#     even_list, odd_list = func(l)

#     💡 You need to access list elements one by one.
#     💡 You can use the %  to check if each element is even or odd.

############################################### Task 5 Solution ###############################################

l = [2, 13, 18, 93, 22]

def func(list):
    """
    A function that takes a list as an argument, assigns odd and even numbers in a list to separate lists and returns these lists.
    Args:
        list: list of numbers

    Returns: even_list and odd_list
    """
    even_list = []
    odd_list = []
    for element_of_list in list:
        if element_of_list % 2 == 0:
            even_list.append(element_of_list)
        else:
            odd_list.append(element_of_list)
    return even_list, odd_list

even_list, odd_list = func(l)

############################################### Task 6 ##############################################################

# In the list given below are the names of the students who received degrees in engineering and medicine faculties.
# Respectively, the first three students represent the success order of the engineering faculty, while the last three students belong to the medical faculty student rank.
# Print the student's degrees specific to the faculty using Enumerate.

#     students = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

#     Expected Output:

#     Engineering Faculty 1 . student: Ali
#     Engineering Faculty 2 . student: Veli
#     Engineering Faculty 3 . student: Ayşe
#     Medicine Faculty 1 . student: Talat
#     Medicine Faculty 2 . student: Zeynep
#     Medicine Faculty 3 . student: Ece

############################################### Task 6 Solution ###############################################

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(students, start=1):
    if index <= 3:
        print("Engineering Faculty {}. student: {}".format(index, student))
    else:
        print("Medicine Faculty {}. student: {}".format(index - 3, student))

############################################### Task 7 ##############################################################

# Three lists are given below. In the lists, there is a course code, credit, and quota information, respectively. Print course information using zip.

#     lesson_codes  = ["CMP1005","PSY1001","HUK1005","SEN2204"]
#     credits = [3,4,2,4]
#     quotas = [30,75,150,25]

#     Expected Output:

#     The quota of the CMP1005 course with 3 credits is 30 people.
#     The quota of the PSY1001 course with 4 credits is 75 people.
#     The quota of the HUK1005 course with 2 credits is 150 people.
#     The quota of the SEN2204 course with 4 credits is 25 people.

###############################################  Task 7 Solution ###############################################

lesson_codes = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credits = [3, 4, 2, 4]
quotas = [30, 75, 150, 25]

course_informations = zip(credits, lesson_codes, quotas)

for credit, lesson_code, quota in course_informations:
    print("The quota of the {} course with {} credits is {} people.".format(lesson_code, credit, quota))

############################################### Task 8 ##############################################################

# Below are 2 sets.
# if the first set includes the second set, it will print their common elements. If not, define the function to print the elements of the second set that are different from the first set.

#     set1 = set(["data","python"])
#     set2 =  set(["data","function","qcut","lambda","python","miuul"])

#     Expexted Output:

#     {'function', 'qcut', 'miuul', 'lamda'}

#     💡You can use the issuperset() method to check if it is covered.
#     💡For different and environment elements, you can use intersection and difference methods.

############################################### Task 8 Solution ###############################################

set1 = set(["data", "python"])
set2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def compare_set(set1, set2):
    if set1.issuperset(set2):
        common_elements = set1.intersection(set2)
        print(common_elements)
    else:
        different_elements = set2.difference(set1)
        print(different_elements)


print(compare_set(set1, set2))
#######################################################################################################################