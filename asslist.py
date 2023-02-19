#Write a Python program to sum all the items in a list.

l1 = [34, 52, 22, 12, 101]

def sumlist(a):
    sum = 0
    for a in l1:
        sum += a
    return sum

print(sumlist(l1))



#Write a Python program to multiply all the items in a list

l2 = [1, 2, 4, 5, 10]
 
def mut(b):
    multi = 1
    for b in l2:
        multi *= b
    return multi

print(mut(l2))



#Write a Python program to get the largest number from a list.


l3 = [1, 2, 4, 5, 10]

def large(c):
    largest = 0
    for c in l3:
        if c > largest:
            largest = c
    return largest

print(large(l3))



#Write a Python program to get the smallest number from a list.

def small(c):
    smallest = 9999
    for c in l3:
        if c < smallest:
            smallest = c
    return smallest

print(small(l3))



#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given 
#list of strings

Li = ['abc', 'xyz', 'aba', '1221']

def word(a):
    diff = 0
    for words in a:
        if len(words) > 1 and words[0] == words[-1]:
            diff += 1
    return diff

print(word(Li))



#Write a Python program to get a list, sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.

cord = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last(cord))



#Write a Python program to remove duplicates from a list.

s = [1, 2, 4, 1, 5, 10]

new_s = []
for x in s:
    if x not in new_s:
        new_s.append(x)
        
print(new_s)



#Write a Python program to check a list is empty or not

s = []

if not s:
    print("list is empty")
    
    
    
#Write a Python program to clone or copy a list.

s = [1, 2, 4, 1, 5, 10]
s2 = s

print(s)
print(s2)




#Write a Python program to find the list of words that are longer than n from a given list of words.

w = (4, "The quick brown fox jumps over the lazy dog")
def long_words(a):
    words = []
    text = a[1].split(" ")
    for x in text:
        if len(x) > a[0]:
            words.append(x)
    return words

print(long_words(w))



#Write a Python function that takes two lists and returns True if they have at least one common member

s = [1, 2, 4, 1, 5, 10]
n = [3, 8, 9, 15, 20, 4]

def has_common(a, b):
    same = []
    for x in a:
        if x in b:
            same.append(x)
            return same

print(has_common(s, n))




#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del color[0]
del color[-2]
del color[-1]

print(color)


 
#Write a Python program to print the numbers of a specified list after removing even numbers from it.

s = [1, 2, 4, 1, 5, 10]

def new_list(a):
    odd = []
    for x in a:
        if x % 2 != 0:
            odd.append(x)
    return odd

print(new_list(s))



#Write a Python program to shuffle and print a specified list

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new = color[3:] + color[:3]

print(new)



#Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
           25, 26, 27, 28, 29, 30,]

def sqr(a):
    square_of_number = []
    for num in a:
        square_of_number.append(num * num)
    print(square_of_number[:5])
    print(square_of_number[-5:])
    
sqr(numbers)



#Write a Python program to generate and print a list except for the first 5 elements, 
# where the values are square of numbers between 1 and 30 (both included).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
           25, 26, 27, 28, 29, 30,]

def sqr(a):
    square_of_number = []
    for num in a:
        square_of_number.append(num * num)
    print(square_of_number[5 : 30])
    
sqr(numbers)



#Write a Python program to get the difference between the two lists.

list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1

print(total_diff)



#Write a Python program access the index of a list.

nums = [5, 15, 35, 8, 98]
for num_index, num_val in enumerate(nums):
    
    print(num_index, num_val)




#Write a Python program to convert a list of characters into a string

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)

print(str1)



#Write a Python program to find the index of an item in a specified list

num =[10, 30, 4, -6]

print(num.index(4))



#Write a Python program to append a list to the second list.

s = ['a', 'b', 'c', 'd']
color = ["blue", "green", "yellow",]
new = s + color

print(new)

def new_list(a):
    l2 = []
    for i in s:
        l2.append(i)
    return l2

print(new_list(s))



#Write a Python program to find the second smallest number in a list

nums = [5, 15, 35, 8, 98]

nums.sort()

print(nums[1])



#Write a Python program to find the second largest number in a list.

nums = [5, 15, 35, 8, 98]

nums.sort()

print(nums[-2])



#Write a Python program to get unique values from a list.

my_list = [10, 20, 30, 40, 20, 50, 60, 40]


def uniq(z):
    uniq_list = []
    for i in z:
        if i not in uniq_list:
            uniq_list.append(i)
    return uniq_list

print(uniq(my_list))



#Write a Python program to count the number of elements in a list within a specified range.

my_list = [10, 20, 30, 40, 20, 50, 60, 40]

def count(y):
    counter = []
    for w in range(len(y)):
        if w not in counter:
            counter.append(w)
    return counter

print(count(my_list))



#Write a Python program to find common items from two lists.

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]

def same(c, d):
    common = []
    for i in c:
        if i in d:
            common.append(i)
    return common

print(same(color1, color2))



#Write a Python program to convert a list of multiple integers into a single integer.

z = [11, 33, 50]
for c in z:
    
    print(c, end="")
    
    
    
#Write a Python program to select the odd items of a list.

numb = [1, 3, 5, 7, 9, 10, 54, 66, 55]

def odd(v):
    odd = []
    for k in v:
        if k % 2:
            odd.append(k)
    return odd

print(odd(numb))




# Write a Python program to replace the last element in a list with another list

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2

print(num1)



#Write a Python program to print a list of space-separated elements.

num = [1, 2, 3, 4, 5]

print(*num)



#Write a Python program to round the numbers of a given list, print the minimum and maximum numbers
# and multiply the numbers by 5. Print the unique numbers in ascending order separated by space

nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
new = list(map(round, nums))
double = []
for i in new:
    i = i * 5
    double.append(i)
    double.sort()
    
print(list(double))



#Write a Python program to count number of lists in a given list of lists.

list1 = [[1, 3], [5, 7], [9, 11]] 
list2 = [[2, 4], [6, 8], [10, 12, 14]]

new_l = list(map(list.__add__, list1, list2))

print(new_l)



#Sort each sublist of strings in a given list of lists

color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]

def soort(a):
    new_color = list(map(sorted, a))
    return(new_color)

print(soort(color1))



#Write a Python program to compute average of two given lists.

nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

def average_two_lists(nums1, nums2):
    result = sum(nums1 + nums2) / len(nums1 + nums2) 
    return result

print(average_two_lists(nums1, nums2))

nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

def ave(a, b):
    average = sum(a) + sum(b)/len(a)+len(b)
    return average

print(ave(nums1, nums2))



#Write a Python program to count integer in a given mixed list.

def count_integer(lis1):
    ctr = 0
    for i in lis1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr

lis1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]



#Write a Python program to extract a specified column from a given nested list.

a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

b =[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

def ext(c):
    extracted = []
    for num in c:
        del(num[0])
        extracted.append(num)
    return extracted

print(ext(a))

def ext(d):
    extracted = []
    for num in d:
        del(num[0])
        extracted.append(num)
    return extracted

print(ext(b))



#Write a Python program to rotate a given list by specified number of items to the right or left direction.

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

z = num1[4:] + num1[:4]

print(z)



# Write a Python program to find the item with maximum occurrences in a given list

x = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

def max_occurrences(nums):
    max_val = 0
    result = nums[0] 
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result

print(max_occurrences(x))



#Write a Python program to access multiple elements of specified index from a given list

listt = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

new = []
a = listt[0]
b = listt[3]
c = listt[5]
d = listt[7]
e = listt[10]
new.append((a, b, c, d, e))

print(new)



#Write a Python program to extract the nth element from a given list of tuples

info = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

ex = []
for i in info:
    ex.append(i[-1])
    
print(ex)



#Write a Python program to check if the elements of a given list are unique or not

nums1 = [1,2,4,6,8,2,1,4,10,12,14,12,16,17]
nums2 = [2,4,6,8,10,12,14]

def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True

print(all_unique(nums1))
print(all_unique(nums2))



#Write a Python program to remove all elements from a given list present in another list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]


new = []
for l in list1:
    if l not in list2:
        new.append(l)
        
print(new)



#Write a Python program to create a list taking alternate elements from a given list.

nums = [2,0,3,4,0,2,8,3,4,2]

def alternate_elements(list_data):
    result=[]
    for item in list_data[::2]:
        result.append(item)
    return result

print(alternate_elements(nums))



#Write a Python program to reverse strings in a given list of string values

rgb = ['Red', 'Green', 'Blue', 'White', 'Black']

n = []
for r in rgb:
    n.append(r[::-1])
    
print(n)



#Write a Python program to calculate the product of the unique numbers of a given list

nums = [10, 20, 30, 40, 20, 50, 60, 40]
new = list(set(nums))

product = 1

for n in new:
    product *= n
    
print(product)



#Write a Python program to remove words from a given list of strings containing a character or string.

list1 = ['Red color', 'Blue #', 'Green', 'Orange @', 'White']

new = []
for l in list1:
    special = l.split(" ")
    new.append(special[0])
    
print(new)


#Write a Python program to reverse each list in a given list of lists.

s = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

ss = []
for i in s:
    ss.append(i[::-1])
    
print(ss)



#Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.

nm = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]

maxv = max(nm)
minv = min(nm)
for index, value in enumerate(nm):
    if value == maxv:
        
        print(f"{index}, {maxv}")

for index, value in enumerate(nm):
    if value == minv:
        
        print(f"{index}, {minv}")
        


#Write a Python program to find the difference between two list including duplicate elements.

l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]

new = list(l1)
for o in l2:
    if o in new:
        new.remove(o)
        
print(new)



#Write a Python program to remove duplicate words from a given list of strings

x = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']

new = []
for xx in x:
    if xx not in new:
        new.append(xx)  
         
print(new)



#Write a Python program to find a first even and odd number in a given list of numbers.

q = [1, 3, 5, 7, 4, 1, 6, 8]

oddd = []
even = []

for n in q:
    if n %2!= 0:
        oddd.append(n)
    
    if n %2== 0:
        even.append(n)

print(oddd[0])
print(even[0])



d = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

inte = sorted([])
stri = sorted([])

for a in d:
    if type(a) == int:
        inte.append(a)
        
    if type(a) == str:
        stri.append(a)

print(inte + stri)



#Write a Python program to sort a given list of strings(numbers) numerically

num = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

new_num = []
for x in num:
    x = int(x)
    new_num.append(x)
    
print(sorted(new_num))



#Write a Python program to remove the specific item from a given list of lists

rgbc = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], 
        ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]

new_color = []

for r in rgbc:
    color = r[0]
    new_color.append(color)
    
print(new_color)



#Write a Python program to remove empty lists from a given list of lists.

list1 = [[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []]

list11 = []

for x in list1:
    if x:
        list11.append(x)
        
print(list11)


#Write a Python program to sum a specific column of a list in a given list of lists.

asif = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

sum = 0

for x in asif:
    first = x[0]
    sum += first
    
print(sum)



# Write a Python program to remove specific words from a given list.

color = ['red', 'green', 'blue', 'white', 'black', 'orange']

newc = []

for c in color:
    color.remove(c)
    newc.append(c)
    
print(newc)
print(color)


#Write a Python program to reverse a given list of lists

c = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]

new = []

for cc in c:
    new.append(cc[::-1])
    
print(new)



#Write a Python program to get the items from a given list with specific condition.

nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
new = []

for n in nums:
    if n > 45 and n %2==0:
        new.append(n)

print(new)



#Write a Python program to remove None value from a given list.

no = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

n = []
for item in no:
    if item is not None:
        n.append(item)

print(n)



#Write a Python program to convert a given list of strings into list of lists.

colors = ["Red", "Maroon", "Yellow", "Olive"]
new = []

for c in colors:
    new.append(list(c))
    
print(new)



#Write a Python program to display vertically each element of a given list

a = ['a', 'b', 'c', 'd', 'e', 'f']

for c in a:
    
    print(c)



#Write a Python program to convert a given list of strings and characters to a single list of characters

leetrs = ['red', 'white', 'a', 'b', 'black', 'f']

new = []
for l in leetrs:
    for i in l:
        new.append(i)
        
print(new)



#Write a Python program to add a number to each element in a given list of numbers

num = [3, 8, 9, 4, 5, 0, 5, 0, 3]
new = []

for i in num:
    newi = i + 3
    new.append(newi)

print(new)



#Write a Python program to check if a given string contains an element, which is present in a list.

str1 = "https://www.w3resource.com/python-exercises/list/"
lst = ['.com', '.edu', '.tv']

def check(a, b):
    for l in b:
        if l in a:
            return True
    return False

print(check(str1, lst))




#Write a Python program to find the indexes of all None items in a given list.

lll = [1, None, 5, 4, None, 0, None, None]
res = []

for index, l in enumerate(lll):
    if l == None:
        res.append(index)
        
        
print(res)
        # print(f"{index}", end=' ')
        


#Write a Python program to remove additional spaces in a given list

text = ['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']
res = []

for i in text:
    j = i.replace('  ', ' ')
    res.append(j)
    
print(res)


#Write a Python program to find the common tuples between two given lists.

list1 =  [('red', 'green'), ('black', 'white'), ('orange', 'pink')] 
list2 =  [('red', 'green'), ('orange', 'pink')] 

res = set(list1).intersection(list2)

print(res)



#Write a Python program to remove an element from a given list.

student = ['Ricky Rivera', 98, 'Math', 90, 'Science']

del(student[0])

print(student)



#Write a Python program to get the symmetric difference between two iterables, without filtering out duplicate values

a = [10, 20, 30]
b = [10, 20, 40]

c = set(a).symmetric_difference(b)

print(list(c))



#Write a Python program to get the weighted average of two or more numbers

nums1 = [10, 50, 40]
nums2 = [2, 5, 3]

sum_of_nums1 = 0
sum_of_nums2 = 0

weighted_ave = 0.0

for num in nums1:
    sum_of_nums1 += num
    
for n in nums2:
    sum_of_nums2 += n

weighted_ave = sum_of_nums1 / sum_of_nums2
print(weighted_ave)



nums1 = [1, 2, 4]
nums2 = [2, 4, 1]


def check(a, b):

    for num in set(nums1):
        if num in set(nums2):
            return True
    return False

print(check(num1, num2))



#Write a Python program to create a given flat list of all the keys in a flat dictionary

students = {
  'Laura': 10,
  'Spencer': 11,
  'Bridget': 9,
  'Howard ': 10,
}

def extr(a):
    return list(students.keys())

print(extr(students))



#Write a Python program to check if all the elements of a list are included in another given list.

a = [10, 20, 30, 40, 50, 60] 
b = [30, 40]

def inf(c, d):
    for aa in d:
        if aa in c:
            return True
    return False

print(inf(a, b))



#Write a Python program to get the most frequent element in a given list of numbers.

nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]


def most_frequent(a):
  return max(set(a), key = a.count) 

print(most_frequent(nums))



#Write a Python program to get a list with n elements removed from the left, right.

nums = [1, 2, 3]

def drop_left_right(a, n = 1):
  return a[n:], a[:-n] 
result = drop_left_right(nums)

print(result)

x = [3, 2, 4, 1, 5, 1]
y = [1, 1]
def inf(c, d):
    for aa in d:
        if aa in c:
            return True
    return False

print(inf(x, y))



#Write a Python program to check if there are duplicate values in a given flat list.

nums = [1, 2, 3, 4, 5, 6, 7]

def has_duplicates(lst):
  return len(lst) != len(set(lst))


print(has_duplicates(nums))



#Write a Python program to find the largest odd number in a given list of integers

nums = [0, 9, 2, 4, 5, 6]

res = 0

for num in nums:
    if num %2!=0 and num > res:
        res = num
        
        print(res)
        
        

#Write a Python program to extract the first specified number of vowels from a given string. 
# If the specified number is less than number of vowels present in the string then display 
# "n is less than number of vowels present in the string

word = "Python"
n = 2

def test(text, n):
	result_str = ''
	for i in text:
		if i in 'aioueAEIOU':
			result_str+=i
	return result_str[:n] if len(result_str) >= n else 'n is less than number of vowels present in the string.'

print(test(word, n))



#Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. 
# Return all pairs of integers in a list.


nums = [0, 3, 4, 7, 9]

def test(nums):
    result = []
    for i, x in enumerate(sorted(nums)):
        for y in nums[i+1:]:
            if y == x + 3:
                result.append([x,y])
    return result

print(test(nums))


from dic import dic3

print(dic3)