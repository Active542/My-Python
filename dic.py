#Write a Python script to add a key to a dictionary.

a =  {0: 10, 1: 20}
a.update({2:30})

print(a)


#Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

new_dic = {}
for d in (dic1, dic2, dic3): new_dic.update(d)

print(new_dic)



#Write a Python script to check whether a given key already exists in a dictionary.

z = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check(a):
    x = 15
    if x in a:
        print("present")
    else:
        print("not present")

check(z)



#Write a Python program to iterate over dictionaries using for loops.

z = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for key, value in z.items():
    
    print(key,":", value)
    
    
#Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d3 = d1.copy()
d3.update(d2)

print(d3)

newd = {}
for d in (d1, d2):
    newd.update(d)
    
print(newd)



#Write a Python program to sum all the items in a dictionary.

print(sum(d3.values()))



#Write a Python program to multiply all the items in a dictionary. 

result = 1
for a in d3:
    result = result*d3[a]
    
print(result)

result = 1
for key, value in d3.items():
    result *= value
    
print(result)



#Write a Python program to remove a key from a dictionary

myDict = {'a':1,'b':2,'c':3,'d':4}

print(myDict)

if 'a' in myDict: 
    del myDict['a']
    
print(myDict)



#Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))


print(color_dictionary)



#Write a Python program to sort a given dictionary by key. 

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key, value in sorted(color_dict.items()):
    
    print(f"{key}:{value}")

  

#Write a Python program to get the maximum and minimum value in a dictionary.

my_dict = {'x':500, 'y':5874, 'z': 560}

maxv = max(my_dict.values())

print(f"Maximum Value:  {maxv}")

minv = min(my_dict.values())

print(f"Minimum Value:  {minv}")



#Write a Python program to remove duplicates from Dictionary.

student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)


#Write a Python program to check a dictionary is empty or not

my_dict = {}

if not bool(my_dict):
    
    print("Dictionary is empty")
    
    
    
#Write a Python program to print all unique values in a dictionary

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

u_value = set( val for dic in L for val in dic.values())

print("Unique Values: ",u_value)



#Write a Python program to count the values associated with key in a dictionary

student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

sum = 0
inpt = 'id'

for d in student:
    for a, b in d.items():
        if a == inpt:
            sum += b
            
print(sum)



#Write a Python program to convert a list into a nested dictionary of keys

num_list = [1, 2, 3, 4]
new_dict = current = {}

for name in num_list:
    current[name] = {}
    current = current[name]
    
print(new_dict)



#num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

for k, v in num.items():
    a = sorted(v)
    
    print(f"{k}:{a}")
    
    

#Write a Python program to remove spaces from dictionary keys

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

for x, y in student_list.items():
    new = x.translate({32: None})
    
    print(new)
    


#Write a Python program to get the key, value and item in a dictionary.

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("key  value  count")

for count, (key, value) in enumerate(dict_num.items(), 1):
    
    print(key,'   ',value,'    ', count)
    


# Write a Python program to print a dictionary line by line

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for a in students:
    print(a)
    for b, a in students[a].items():
        print(f"{b}:{a}")
        
        

#Write a Python program to check multiple keys exists in a dictionary.

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})



#Write a Python program to count number of items in a dictionary value that is a list.

dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

ctr = 0
for k, v in dic.items():
    ctr += len(v)
print(ctr)



#Write a Python program to sort Counter by value

data = {'Math':81, 'Physics':83, 'Chemistry':87}

for key, value in data.items():
    print(tuple((key, value)))



#Write a Python program to replace dictionary values with their average.

def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts 
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(sum_math_v_vi_average(student_details))



#Write a Python program to match key values in two dictionaries.

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for (key, value) in set(x.items()) & set(y.items()):
    print(f"{(key, value)} appears in both dictionary")



#Write a Python program to filter a dictionary based on values.

info = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

ctr = {}
for (k, v) in info.items():
    if v >= 170:
        ctr = {k : v}
        print(ctr)



#Write a Python program to filter the height and width of students, which are stored in a dictionary.

students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}


def filter_data(students):
    result = {}
    for k, s in students.items():
        if s[0] >= 6.0 and s[1] >= 70:
            result = {k : s}
    return result
 

print(filter_data(students))



#Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.

colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result


print(grouping_dictionary(colors))



#Write a Python program to remove a specified dictionary from a given list.

color = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, 
         {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

del color[0]
print(color)



#Write a Python program to convert string values of a given dictionary, into integer/float datatypes.

x = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

for y in x:
    for w, z in y.items():
        print({w, int(z)})
        


#A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary.

dictionary = { 'C1' : [10,20,30], 'C2' : [20,30,40],'C3' : [12,34]}

for key, value in dictionary.items():
        value.clear()
print(dictionary)



#Write a Python program to extract a list of values from a given list of dictionaries.

lst = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

result = []

for i in lst:
    for k, v in i.items():
        if k == 'Science':
            result.append(v)

print(result)



#Write a Python program to find the length of a given dictionary values.

dic = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

new = {}

for k, v in dic.items():
    length = len(v)
    new = {v : length}
    
    print(new)



#Write a Python program to access dictionary key's element by index.

num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])



#Write a Python program to convert a given dictionary into a list of lists.

dic = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

lst = []

for k, v in dic.items():
    lst.append([k, v])
print(lst)



#Write a Python program to find the specified number of maximum values in a given dictionary

dic = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

maxv = 0

for key, value in dic.items():
    if value > maxv:
        maxv = value
print(key, maxv)



#Write a Python program to find shortest list of values with the keys in a given dictionary.

x = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

new = {}

minlen = 1

for k, v in x.items():
    length = len(v)
    if length <= minlen:
        minlen = length
        new = {k}
        print(new)



#Write a Python program to extract values from a given dictionaries and create a list of lists from those values.

lst = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
       {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, 
       {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
       {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
       {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

new_lst = []

for i in lst:
    for k, v in i.items():
        new_lst.append((v))
print(new_lst)



#Write a Python program to convert a given list of lists to a dictionary.

ll = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], 
      [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

result = {}

for i in ll:
    result = {i[0] : i[1:]}
    print(result)



# Write a Python program to get the total length of all values of a given dictionary with string values

rgb = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

length = 0

for k, v in rgb.items():
    length += len(v)
print(length)



#Write a Python program to invert a dictionary with unique hashable values

students = {
  'Theodore': 10,
  'Mathew': 11,
  'Roxanne': 9,
}

for key, value in students.items():
    print(f"{value} : {key}")
    
    

#Write a Python program to convert given a dictionary to a list of tuples.

dic = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

lst = []

for k, v in dic.items():
    lst.append((k, v))
print(lst)



#Write a Python program to create a flat list of all the keys in a flat dictionary

info = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}#

flat_list = []

for key, value in info.items():
    flat_list.append(key)
print(flat_list)



#Write a Python program to create a flat list of all the values in a flat dictionary.

info = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}#

flat_list = []

for key, value in info.items():
    flat_list.append(value)
print(flat_list)



#

info = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

maxv = 0
minv = 9999

for key, value in info.items():
    if value > maxv:
        maxv = value

        print(key, maxv)
        

for key, value in info.items():
    if value < minv:
        minv = value

        print(key, minv)