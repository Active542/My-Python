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
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)


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

#Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1,2,3])))

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

#Write a Python program to select an item randomly from a list
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

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

